rm -rf ./deployment

mkdir -p ./deployment/frontend
mkdir -p ./deployment/backend

cp -r pages ./deployment/frontend
cp -r public ./deployment/frontend
cp ./frontend.py ./deployment_template/config.toml ./deployment/frontend
cp ./deployment_template/frontend_requirements.txt ./deployment/frontend/requirements.txt
cp ./deployment_template/frontend_Dockerfile ./deployment/frontend/Dockerfile

cp ./backend.py ./deployment/backend
cp ./deployment_template/backend_requirements.txt ./deployment/backend/requirements.txt
cp ./deployment_template/backend_Dockerfile ./deployment/backend/Dockerfile

docker build -t sample-app-backend ./deployment/backend -f ./deployment/backend/Dockerfile
docker build -t sample-app-frontend ./deployment/frontend -f ./deployment/frontend/Dockerfile

docker compose up