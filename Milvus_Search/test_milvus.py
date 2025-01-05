# pip3 install tensorflow tensorflow-hub numpy 
import os
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
import re

from pymilvus import Collection, FieldSchema, CollectionSchema, DataType, connections, utility

import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Start logging
logger.info('Connecting to Milvus Server')
# Connect to milvus database
connections.connect(
  alias="default",
  host='localhost',
  port='19530'
)


# Download the model and load the model
module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5" #@param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
model = hub.load(module_url)


def embeddings(text):
    "Function to generate embeddings"
    return np.array(model(text)).flatten().tolist()


# Dataset available at https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
# Download the dataset and extract the files before running this cell
# We will create the embeddings from this dataset using the universal-sentence-encoder model


print("*****Logging")
logger.info('***Setting File Path')
file_path = 'SMSSpamCollection'

logger.info('***Accessing  File Path')
with open(file_path) as file:
    lines = [line for line in file]

msgs = [x.split('\t')[1].replace('\n', '')   for x in lines]
embdngs = [embeddings([x]) for x in msgs]
indx = list(range(1, len(msgs)+1))

data_to_insert = [indx, msgs, embdngs]




# Field Schema
id = FieldSchema(           #index
  name="id",
  dtype=DataType.INT64,
  is_primary=True,
)
message = FieldSchema(      #text/msgs
  name="message",
  dtype=DataType.VARCHAR,
  max_length=6000,
)
message_vec = FieldSchema(  #embdngs
  name="message_embeddings",
  dtype=DataType.FLOAT_VECTOR,
  dim=512
)
# collection schema
collection_schema = CollectionSchema(
  fields=[id, message, message_vec],
  description="Spam SMS collection"
)
# Create collection
collection = Collection(
    name="Spam_Test",
    schema=collection_schema,
    using='default')
utility.list_collections()

# Insert entities;  data_to_insert = [indx, msgs, embdngs]
data_insert = collection.insert(data_to_insert)

# Create Index 
index_params = {
  "metric_type":"L2",       #Euclidean Distance, measure similarity of vectors
  "index_type":"IVF_FLAT",  #Inverted File w/ flat compression, used to accelerate the vector search
  "params":{"nlist":1024},  #Building parameter(s) specific to the index.
  "index_name": "SMS_IVF_FLAT_TEST"
}

# Index on vector field
collection.create_index(
  field_name="message_embeddings", 
  index_params=index_params
)

# Load the collection
collection.load(replica_number=1)

# test message
test_message = ["where r we meeting"]
test_message_vector = embeddings(test_message)

## Vector Similarity Search
search_params = {"metric_type": "L2", "params": {"nprobe": 64}}

results = collection.search(
	data=[test_message_vector], 
	anns_field="message_embeddings", 
	param=search_params,
	limit=5, 
	expr=None,
	output_fields=['message']
)

for result in results[0]:
    print (result)








