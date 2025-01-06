# Select Image
FROM python:3.10

WORKDIR /app

# OCI Labels
LABEL org.opencontainers.image.authors="Jacob Cox"
LABEL org.opencontainers.image.title="Milvus Search"
LABEL org.opencontainers.image.description="TBD"
LABEL org.opencontainers.image.version="1.0"

RUN echo "python --version"
# Copy files to image and add requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY test_milvus.py ./
COPY SMSSpamCollection ./

EXPOSE 8080

# Lauch the Python App after the container starts
CMD [ "python", "./test_milvus.py" ]






