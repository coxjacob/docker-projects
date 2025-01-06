# milvus-u

This code has been adapted from the Udemy Course [Introduction to Milvus (Vector Database) Using Python](https://www.udemy.com/course/getting-started-with-milvus-vector-database). The courese showed how to implement Milvus from Jupyter Notebook. This repository places the query code in its own container with a standalone python file. 

## Getting started
- Start the Milvus Container 
  - See README.md

## Validate Milvus is Running
- Check Docker Desktop's Containers for milvus-u
- Stack contains Milvus Containers:
  - milvus-etcd
  - milvus-minio, ports 9000, 9001
  - milvus-standalone, ports 19530, 9091
- Query Container
  - query_milvus (shuts down after running)
    - Look at logs in Docker Desktop

## Shutting Down
- See README.md


## Future Work
### Enable CUDA
CUDA GPUs do not currently work on my implmentation. More work is needed to engage the GPU. 
- [Install TensorFlow with pip](https://www.tensorflow.org/install/pip)

### Data Loader
Data is currently storred in SMSSpamCollection. Need to automate the process of loading data. 

### Volumes
test_milvus.py downloads models and creates embeddings and a vector index. This data needs to be persisted beyond the codes initial run. 

### Create an API
This code is a proof of concept. An API needs to be built to support multiple search queries from a URL. Looking at routes to do it. 

## References
1. [Milvus](https://github.com/milvus-io/milvus)
2. [GPU Standalone](https://github.com/milvus-io/milvus/blob/master/deployments/docker/gpu/standalone/docker-compose.yml)