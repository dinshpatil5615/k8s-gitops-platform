## Architecture Overview

This project implements a self-service deployment platform.

### Workflow
1. A developer pushes application code to Git.
2. The platform automatically builds and deploys the application.
3. Kubernetes runs in the background and is not directly accessed by the developer.

### Tools Used
- Git
- GitHub Actions
- Docker
- Kubernetes
- ArgoCD
- NGINX Ingress
- Prometheus
- Grafana
