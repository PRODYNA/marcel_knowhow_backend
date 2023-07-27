# marcel_knowhow_backend
This projects hold the backend functionality for Marcel's know how session.


# Manual build

## Docker image build
Run `docker buildx build --platform linux/amd64 -t jnicontainerregistry.azurecr.io/marcel_knowhhow_backend .` in the local build directory.

## Push manually build image to registry
Use `docker push jnicontainerregistry.azurecr.io/marcel_knowhhow_backend:latest` to push the image to the registry.

## Run
Use the docker compose file with `docker-compose up -d` to start the backend.
Browse locally to http://localhost:8080/ to see the backend running.
