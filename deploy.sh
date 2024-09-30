#!/bin/bash

# Stash any local changes and pull the latest code
echo "Stashing local changes and pulling the latest code..."
sudo git stash
sudo git pull

# Build and run the Docker containers
echo "Building and running Docker containers..."
sudo docker compose build
sudo docker compose up -d

# Restart Nginx to apply any changes
echo "Restarting Nginx..."
sudo systemctl restart nginx

# Remove unused Docker images to free up space
echo "Removing unused Docker images..."
sudo docker image prune -f

# Optional: Remove dangling volumes
echo "Removing dangling Docker volumes..."
sudo docker volume prune -f

echo "Deployment tasks completed successfully!"
