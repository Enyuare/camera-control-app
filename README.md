# camera-control-app with Docker Compose for ARM arch

Make sure that Docker is installed on your system and port 8081 is free

Navigate to the directory:
```sh
cd SonyARM-init
```

Build with Docker:
```sh
docker compose build
```

Power cycle the camera. Run the Docker Container and wait for 5s to initialize the camera 
```sh
docker compose run -d
```
To click a picture
```sh
cd app
python3 commandClick.py
```
The image will be stored inside the docker container. You can ssh into the container in a new terminal (or existing) with the following command:
```sh
docker exec -it camera-control-app /bin/bash
```

To see the newly captured image:
```sh
ls
```
