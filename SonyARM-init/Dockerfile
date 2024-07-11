# Use the official Ubuntu 22.04.4 LTS image as a parent image
FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /camera-control-app

# Update the package list and install some packages
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libjsoncpp-dev \
    autoconf \
    libtool \
    libudev-dev \
    gcc \
    g++ \
    make \
    cmake \
    unzip \
    libxml2-dev \
    
    # Add any other dependencies you need
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /camera-control-app

# Change directory to /app
RUN cd /camera-control-app

    
RUN mkdir -p /camera-control-app/build && cd /camera-control-app/build && \
    cmake -DCMAKE_BUILD_TYPE=Release .. && \
    cmake --build .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run rgb-cam-init when the container launches
CMD ["./build/rgb-cam-init"]
