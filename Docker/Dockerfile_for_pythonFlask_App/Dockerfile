FROM python:latest

# Metadata
LABEL MAINTAINER="srtechops <srtechopsofficial@gmail.com>"

# Set working directory
WORKDIR /usr/src/app

# Copy and install dependencies
COPY requirements.txt  .
RUN pip install -r requirements.txt

# Copy application code
COPY app.py  .

# Expose the application port
EXPOSE 80

# Set the default command
CMD ["python", "app.py"]
