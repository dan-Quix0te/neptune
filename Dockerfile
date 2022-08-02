FROM python:3.10-slim-bullseye

# Get the version from the build arguments:
#  --build-arg VERSION=1.2.0
ARG VERSION
ENV VERSION=$VERSION
MAINTAINER dan-Quxi0te

# Create a regular user for production
RUN groupadd -g 1001 prod && \
    useradd -r -u 1001 -g prod prod

# Set up the development environment
WORKDIR /neptune

# Install dependencies
COPY requirements.txt .
RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY config.py wsgi.py ./
COPY app ./app

# Expose any ports the app is expecting in the environment
ENV PORT 5000
EXPOSE $PORT

# Become a regular user that owns the app folder 
RUN chown -R prod:prod /neptune
USER prod

# Run the service with gunicorn
ENV GUNICORN_BIND 0.0.0.0:$PORT
CMD ["gunicorn", "--workers=4", "--log-level=info", "wsgi:app"]
