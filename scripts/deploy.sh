#!/bin/bash

echo "Starting deployment..."

# Pull latest changes
git pull origin main

# Build Docker images
docker-compose build

# Start containers
docker-compose up -d

echo "Deployment complete. Application is running."