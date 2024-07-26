path="/camera-control-app"

# Chnage the destination path to the desired location to save images
destination="/home/enyuarelab01/camera-control-app/SonyARM-init"

for file in $(docker exec camera-control-app sh -c "ls ${path}/*.JPG"); do
        docker cp camera-control-app:${file} $destination
        docker exec camera-control-app sh -c "rm ${file}"
done
