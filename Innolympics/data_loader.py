from datasets import load_from_disk

def sync_bills_to_memory():
    try:
        ds = load_from_disk("local_dataset")
        sample = ds["train"].shuffle(seed=42).select(range(10))
        # Return a dictionary for the app to consume
        return {row['id']: row for row in sample}
    except:
        return {} # Early return if dataset is missing