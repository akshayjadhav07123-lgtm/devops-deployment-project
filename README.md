# DevOps Deployment Project

My first end-to-end DevOps deployment project.

## Technologies

- Git and GitHub
- Jenkins
- Python and Flask
- Docker
- Rocky Linux

## Application

A simple Flask application with:

- `/` - Application homepage
- `/health` - Health check endpoint

## Run with Docker

```bash
docker build -t devops-python-app .
docker run -d -p 5000:5000 --name devops-app devops-python-app
