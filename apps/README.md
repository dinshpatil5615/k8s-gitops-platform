# k8s-gitops-platform

In real companies, developers often struggle with Kubernetes complexity.  
This project aims to build a small **Internal Developer Platform (IDP)** where developers can deploy applications using a Git push, without directly interacting with Kubernetes.

The platform will eventually handle CI/CD, deployment, ingress, and monitoring automatically, following real-world DevOps and GitOps practices.

---

## Project Status

This project is being built **step by step**, focusing on understanding *why* tools are used, not just *how* they work.

### Completed
- FastAPI application with production-style endpoints
- Dockerized application

### Planned (Upcoming)
- Kubernetes Deployment and Service
- GitOps-based deployment flow
- CI/CD using GitHub Actions
- Ingress, monitoring, and observability

---

## Application Overview

The current application is a simple FastAPI service designed to behave like a real production backend service that can run inside containers and Kubernetes.

---

## Available Endpoints

| Endpoint | Description |
|--------|------------|
| `/` | Welcome message |
| `/health` | Health check endpoint (used by Docker/Kubernetes) |
| `/version` | Application version endpoint (useful during deployments) |

---

## Tech Stack (Current)

- Python
- FastAPI
- Uvicorn
- Docker

---

## Run Locally Using Docker

### Build the image
```bash
docker build -t dineshpatil0908/platform-app:v1 .
docker run --name container-1 -p 8000:8000 dineshpatil0908/platform-app:v1

open in browser - localhost:8000 , localhost:8000/health and localhost:8000/version
