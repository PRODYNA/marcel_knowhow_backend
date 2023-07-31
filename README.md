 ```
 __  __                    _   ____             _                  _ 
|  \/  | __ _ _ __ ___ ___| | | __ )  __ _  ___| | _____ _ __   __| |
| |\/| |/ _` | '__/ __/ _ \ | |  _ \ / _` |/ __| |/ / _ \ '_ \ / _` |
| |  | | (_| | | | (_|  __/ | | |_) | (_| | (__|   <  __/ | | | (_| |
|_|  |_|\__,_|_|  \___\___|_| |____/ \__,_|\___|_|\_\___|_| |_|\__,_|
                                                                     
```
Marcel Know How Backend Project
===============================
This projects holds the backend functionality for Marcel's know how session.


# Local Development Environment
Inside VSC hit Ctrl+Shift+P and search for _python: create environment_.
Select .venv the a Python executable with Python 3.10 or higher and choose to install the dependencies from the requirements.txt file.
You should be able to run and debug the Fast API server by hitting F5 on the main.py file.


# Docker
## Local Docker Environment
Local Docker image build:
```bash
docker buildx build -t marcel_knowhow_backend .
```

Use the docker compose file with `docker-compose up -d` to start the backend.
Browse locally to http://localhost:8080/ to see the backend running.

## Image for Azure Container Registry and Azure Container Apps Service
Build the docker image with:
```bash
docker buildx build \
	--platform linux/amd64 \
	-t jnicontainerregistry.azurecr.io/marcel_knowhow_backend \
	.
```

Push manually build image to registry
Use `docker push jnicontainerregistry.azurecr.io/marcel_knowhow_backend:latest` to push the image to the registry.
