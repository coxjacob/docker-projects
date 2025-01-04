# Select Image
FROM python:3

WORKDIR /app

# OCI Labels
LABEL org.opencontainers.image.authors="Jacob Cox"
LABEL org.opencontainers.image.title="Milvus Search"
LABEL org.opencontainers.image.description="TBD"
LABEL org.opencontainers.image.version="1.0"

# Copy files to image and add requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 19530

# Lauch the Python App after the container starts
CMD [ "python", "./test_milvus.py" ]






