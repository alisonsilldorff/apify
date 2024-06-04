# Author: Alison Silldorff
# Date: 6/4/24
# apify_tests.py
# Play Around with Apify

#import apify_client
#%%
from apify_client import ApifyClient

apify_client = ApifyClient('apify_api_UEbgaqiEUnKroL3SaOXMMQHxfWFuCa1bfvDs')


actor_client = apify_client.actor('apify/instagram-hashtag-scraper')

input_data = { 'hashtags': ['rainbow'], 'resultsLimit': 20 }

# Run the Actor and wait for it to finish up to 60 seconds.
# Input is not persisted for next runs.
run_data = actor_client.call(run_input=input_data, timeout_secs=60)

# %%
actor_runs = actor_client.runs()
actor_datasets = actor_runs.list(limit=20)
print(actor_datasets.items)

# also when I do get() I get "None"... so somehow there are no datasets?
print(apify_client.dataset(dataset_id=actor_datasets.items[0]['id']).get())
# it seems like the list_items() funciton is what's causing trouble.
print(apify_client.dataset(dataset_id=actor_datasets.items[0]['id']).list_items(limit=1000))


#%%
for dataset_item in actor_datasets.items:
    # Dataset items can be handled here. Dataset items can be paginated
    dataset_items = apify_client.dataset(dataset_id=dataset_item['id']).list_items(limit=1000)

dataset_data = actor_client.last_run().dataset().list_items()
# Start an actor and wait for it to finish
actor_call = apify_client.actor('apify/instagram-scraper').call()

#defaultDatasetId = actor_call['defaultDatasetId']
#print(actor_call[defaultDatasetId])

# Get dataset
dataset_client = apify_client.dataset(actor_call['defaultDatasetId'])
print(dataset_client)

# Lists items from the Actor's dataset
dataset_items = dataset_client.list_items().items
print(dataset_items)



# how do we incorporate the actor_call component in a way that is valid??

# Fetch results from the actor run's default dataset
#dataset_items = apify_client.dataset(actor_call[defaultDatasetId]).list_items().items


# Get dataset
#dataset_client = apify_client.dataset('dataset-id')

# Lists items from the Actor's dataset
#dataset_items = dataset_client.list_items().items
# %%
