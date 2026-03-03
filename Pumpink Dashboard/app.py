import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Pumpink Dashboard", layout="wide")
st.title("📦 Pumpink Inventory Dashboard")

@st.cache_data
def load_data():
    data = pd.read_csv("data.csv")
    data['movements/movement_date'] = pd.to_datetime(
        data['movements/movement_date']
    )
    return data

df = load_data()


#Sidebar Filters
st.sidebar.header("Filters")

#Brand filter
brands = df['items/brand'].unique()
selected_brands = st.sidebar.multiselect(
    "Select Brand",
    brands,
    default=brands
)

min_date = df['movements/movement_date'].min()
max_date = df['movements/movement_date'].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

filtered_df = df[
    (df['items/brand'].isin(selected_brands)) &
    (df['movements/movement_date'] >= pd.to_datetime(date_range[0])) &
    (df['movements/movement_date'] <= pd.to_datetime(date_range[1]))
]

#KPIs
total_released = filtered_df['movements/released'].sum()
total_items = filtered_df['movements/item_id'].nunique()
total_stock = filtered_df['movements/new_stock'].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Released", total_released)
col2.metric("Unique Items", total_items)
col3.metric("Total Current Stock (Sum)", total_stock)

st.divider()

# ========================
# Sales Over Time
# ========================
st.subheader("📈 Sales Over Time")

sales_over_time = (
    filtered_df
    .groupby('movements/movement_date')['movements/released']
    .sum()
    .reset_index()
)

fig_time = px.line(
    sales_over_time,
    x='movements/movement_date',
    y='movements/released',
    markers=True
)

from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare data
sales_over_time['date_ordinal'] = sales_over_time[
    'movements/movement_date'
].map(datetime.toordinal)

X = sales_over_time[['date_ordinal']]
y = sales_over_time['movements/released']

model = LinearRegression()
model.fit(X, y)

# Create future dates
future_dates = pd.date_range(
    sales_over_time['movements/movement_date'].max(),
    periods=30
)

future_ordinals = future_dates.map(datetime.toordinal)
future_pred = model.predict(np.array(future_ordinals).reshape(-1, 1))

future_df = pd.DataFrame({
    'movements/movement_date': future_dates,
    'forecast': future_pred
})

fig_time.add_scatter(
    x=future_df['movements/movement_date'],
    y=future_df['forecast'],
    mode='lines',
    name='30 Day Forecast'
)


st.plotly_chart(fig_time, use_container_width=True)

# ========================
# Top Selling Designs
# ========================
st.subheader("🏆 Top Selling Designs")

top_designs = (
    filtered_df
    .groupby(['items/brand', 'items/design_name'])['movements/released']
    .sum()
    .reset_index()
    .sort_values(by='movements/released', ascending=False)
    .head(10)
)

fig_top = px.bar(
    top_designs,
    x='movements/released',
    y='items/design_name',
    color='items/brand',
    orientation='h'
)

st.plotly_chart(fig_top, use_container_width=True)

# ========================
# Current Stock Table
# ========================
st.subheader("📋 Current Stock by Item")

latest_stock = (
    filtered_df
    .sort_values('movements/movement_date')
    .groupby(['items/brand', 'items/design_name'])
    .tail(1)
    [['items/brand', 'items/design_name', 'movements/new_stock']]
    .sort_values(by='movements/new_stock')
)

st.dataframe(latest_stock, use_container_width=True)



#====
st.subheader(" Stock Depletion PRediction")
avg_daily_sales = (
    filtered_df
    .groupby(['items/brand', 'items/design_name'])
    ['movements/released']
    .mean()
    .reset_index()
    .rename(columns={'movements/released': 'avg_daily_sales'})
)

stock_df = latest_stock.merge(
    avg_daily_sales,
    on=['items/brand', 'items/design_name']
)

stock_df['days_until_stockout'] = (
    stock_df['movements/new_stock'] /
    stock_df['avg_daily_sales']
)

st.dataframe(
    stock_df.sort_values('days_until_stockout')
)

#====
# ========================
# Demand Trend Classification
# ========================

st.subheader("📊 Demand Trend (Last 30 vs Previous 30 Days)")

max_date = filtered_df['movements/movement_date'].max()

# Last 30 days
recent = filtered_df[
    filtered_df['movements/movement_date'] >
    max_date - pd.Timedelta(days=30)
]

# Previous 30 days
previous = filtered_df[
    (filtered_df['movements/movement_date'] <= max_date - pd.Timedelta(days=30)) &
    (filtered_df['movements/movement_date'] > max_date - pd.Timedelta(days=60))
]

# Aggregate sales
recent_sales = (
    recent
    .groupby(['items/brand', 'items/design_name'])['movements/released']
    .sum()
    .reset_index()
    .rename(columns={'movements/released': 'recent_sales'})
)

previous_sales = (
    previous
    .groupby(['items/brand', 'items/design_name'])['movements/released']
    .sum()
    .reset_index()
    .rename(columns={'movements/released': 'previous_sales'})
)

# Merge both periods
trend_df = pd.merge(
    recent_sales,
    previous_sales,
    on=['items/brand', 'items/design_name'],
    how='outer'
).fillna(0)

# Calculate growth
trend_df['growth_rate'] = (
    (trend_df['recent_sales'] - trend_df['previous_sales']) /
    trend_df['previous_sales'].replace(0, 1)
)

# Classify trend
def classify_trend(growth):
    if growth > 0.2:
        return "🔥 Rising"
    elif growth < -0.2:
        return "📉 Declining"
    else:
        return "➖ Stable"

trend_df['trend'] = trend_df['growth_rate'].apply(classify_trend)

# Sort by growth
trend_df = trend_df.sort_values(by='growth_rate', ascending=False)

st.dataframe(trend_df, use_container_width=True)