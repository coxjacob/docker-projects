# milvus-u

This code has been adapted from the Udemy Course [Introduction to Milvus (Vector Database) Using Python](https://www.udemy.com/course/getting-started-with-milvus-vector-database). 

## Getting started
- Start the Milvus Container 
  - docker-compose -f "docker-compose-milvus.yml" up -d 

## Validate Milvus is Running
- Check Docker Desktop's Containers for milvus-u
- Container contains:
  - milvus-etcd
  - milvus-minio, ports 9000, 9001
  - milvus-standalone, ports 19530, 9091

## Shutting Down

- Shutdown Milvus container
  - docker compose -f "milvus-standalone-docker-compose.yml" down 
- Deactivate the virtual environment
  - deactivate

Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/jacobcox1974/milvus-u.git
git branch -M main
git push -uf origin main
```

