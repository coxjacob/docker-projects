# Working with Docker

This respository contains examples of software using docker containers. 

This code is executed on Docker Desktop

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended 
next steps.

To run: 
```
cd directory
docker compose up -d --build
```

## Folders
### Docker_Volumes

This folder demonstrates the use of volumes with a single container. This code uses a Dockerfile and docker-compose.yml file to create a container and two volumes. The container reads from one volume, input_files, and rights 
to another, export_files.