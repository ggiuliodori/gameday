from google.cloud import bigquery

client = bigquery.Client()
datasets = list(client.list_datasets())

print("Datasets:")
for dataset in datasets:
    print(dataset.dataset_id)