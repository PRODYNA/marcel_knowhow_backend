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

The backend provides an API to query general knowledge questions to be used in a quiz game.



# Local Development Environment

## Using Visual Studio Code
Inside VSC hit Ctrl+Shift+P and search for `python: create environment`.
Select `.venv`, a Python executable with Python 3.10 or higher and choose to install the dependencies from the requirements.txt file.
You should be able to run and debug the Fast API server by hitting F5 on the main.py file.

## Without Visual Studio Code
It is recommened to create a virtual environment with Python 3.10 or higher.
Given you have Python installed run run the following command in the project's root:
```bash
python3 -m venv .venv
```
Activate the virtual environment with:
```bash
source .venv/bin/activate
```
Install the dependencies with:
```bash
pip install -r requirements.txt
```


# Shipping
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

## Continuous Integration and Deployment with GitHub Actions
The project comes with a GitHub Actions workflow to build and push the image to the Azure Container Registry (see `./.github/workflows/backend.yaml`).


# Database
The backend projects relies on a neo4j database to store the questions and answering results.
All database related files are located in the `./db` folder.

## Collecting questions
The collect questions a python script is querying questions from the OpenAI GPT-4 model.
To run the script you have to provide a valid OpenAI API key in a `.env` file in the project's root.

Example:
```
openai.api_key=<YOUR_KEY>
```

## Docker Setup

### Local Docker Environment
cd into `./db/docker_image`.

Build a local Docker image with:
```bash
docker buildx build -t marcel_knowhow_db .
```

Use the docker compose file with `docker-compose up -d` to start the backend.
Connect to local neo4j browser with `http://localhost:7474/browser/`.


### Image for Azure Container Registry and Azure Container Apps Service
Build the docker image with:
```bash
docker buildx build \
	--platform linux/amd64 \
	-t jnicontainerregistry.azurecr.io/marcel_knowhow_db \
	.
```

Push manually build image to registry
Use `docker push jnicontainerregistry.azurecr.io/marcel_knowhow_db:latest` to push the image to the registry.

### Continuous Integration and Deployment with GitHub Actions
TODO This is not yet implemented.
The project comes with a GitHub Actions workflow to build and push the image to the Azure Container Registry (see `./.github/workflows/db.yaml`).
