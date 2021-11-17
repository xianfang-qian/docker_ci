pip install -r requirements.txt
docker pull openvino/ubuntu18_data_dev
docker run -it --device /dev/dri:/dev/dri --device-cgroup-rule='c 189:* rmw' -v /dev/bus/usb:/dev/bus/usb --rm openvino/ubuntu18_data_dev:latest 
