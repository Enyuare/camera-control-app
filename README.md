# camera-control-app with Docker Compose for ARM arch

Make sure that Docker is installed on your system and port 8081 is free

Navigate to the directory:
```sh
cd SonyARM-init
```

In order for the image files to appear in the local directory and not just exist in the container some configuration change to the yaml file must be made. Otherwise, the image files will disappear when the docker container exits (each power cycle). Edit the docker-compose.yaml file in the SonyARM-init directory. In the section under volumes, add this on a seperate line:
 - /home/your-username/your-working-directory-with-dockerfiles:/home/your-username/your-working-directory-with-dockerfiles

Substitute your username and working directory in the line. For example:

- /home/enyuare/Code/flogistix/camera-control-app/SonyARM-init:/home/enyuare/Code/flogistix/camera-control-app/SonyARM-init

Change the permission of the docker working directory so docker has permission to copy the files to that directory
```sh
chmod 666 working-directory
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
The camera image will be stored inside the docker container and in an outside directory (the working directory). To see the image inside the docker container, you can ssh into the container in a new terminal (or existing) with the following command:
```sh
docker exec -it camera-control-app /bin/bash
```

To see the newly captured image:
```sh
ls
```
