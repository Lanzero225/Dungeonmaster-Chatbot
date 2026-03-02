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