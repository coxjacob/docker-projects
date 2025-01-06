# Working with Docker

This respository contains examples of software using docker containers. 

This code is executed on Docker Desktop

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended 
next steps.

## Folders
### 1. Docker_Volumes

This folder demonstrates the use of volumes with a single container. This code uses a Dockerfile and docker-compose.yml file to create a container and two volumes. The container reads from one volume, input_files, and rights 
to another, export_files.

To Start the Container
```
docker-compose -f docker-compose-dv.yml up -d
```
To Remove the Containers
```
docker-compose -f docker-compose-dv.ym down
```
To Stop and Keep the containers
```
docker-compose -f docker-compose-dv.ym stop
```

### 2 Milvus_Search

This folder demonstrates the use of networking, syncing, and more. Milvus search requires three containers and a volume. Another container is used to create embedding, build an index, and submit queries to Milvus. 

To Start the Container
```
docker-compose -f docker-compose-m-cuda.yml up -d
```
To Remove the Containers
```
docker-compose -f docker-compose-m-cuda.yml down
```
To Stop and Keep the containers
```
docker-compose -f docker-compose-m-cuda.yml stop
```