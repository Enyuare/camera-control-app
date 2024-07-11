# camera-control

Dependencies:
```sh
sudo apt-get update
sudo apt-get install libjsoncpp-dev
sudo apt install autoconf libtool libudev-dev gcc g++ make cmake unzip libxml2-dev
```

Get to the directory:

```sh
cd SonyARM-init
```

Build:
```sh
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```


To run the executable, open a terminal window:

```sh
./rgb-cam-init
```
Navigate to /SonyARM-init/app. Open a new terminal to send JSON commands:
```sh
cd ..
cd app
python3 commandClick.py
```
