# Select Image
FROM python:3

WORKDIR /app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

# Copy files to image
COPY ./input_files ./input_files
COPY ./export_files ./export_files
COPY read_write.py .

# OCI Labels
LABEL org.opencontainers.image.authors="Jacob Cox"
LABEL org.opencontainers.image.title="Demo: Working with Python"
LABEL org.opencontainers.image.description="TBD"
LABEL org.opencontainers.image.version="1.0"

# Lauch the Python App after the container starts
CMD [ "python", "read_write.py" ]
