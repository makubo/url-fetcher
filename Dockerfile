FROM python:3.9-alpine

# Set work directory
WORKDIR /opt/fetcher

# Install requirements and create symbolic link to the future script
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt; \
    ln -s /opt/fetcher/fetcher.py /usr/sbin/fetcher

# Copy python files
COPY ./src/ ./

# Command by default
CMD [ "fetcher", "https://www.google.com/", "https://autify.com" ]
