# Vision 2022
Rebuild of the 2021 version, this variant contains an updated YOLOv5 root and updated dependencies. Furthermore, this version contains a few new features compared to the previous version, such as detection of which sources are actively being utilized.

# YOLOv5 Object Detection Information / Docs
[YOLOv5](https://github.com/ultralytics/yolov5) is an AI object detection library used for real time object detection.

## Resources
[YOLOv5 Information (training + getting data)](https://blog.roboflow.com/how-to-train-yolov5-on-a-custom-dataset/)\
[Installing Pytorch on Raspberry Pi](https://github.com/marcusvlc/pytorch-on-rpi)

## Usage
**NOTE: ALL Packages and Modules Sit In the Virtual Environment using virtualenv. To run any commands for this repo you must enter the venv.** 
FROM THE YOLOv5_trained_model DIRECTORY Type:
- ON MAC / LINUX: `source venv/bin/activate` to start the environment
- ON WINDOWS: `venv\Scripts\activate` to start the environment

*Note: Roboflow is used for the creation of the yolov5 format. As per YOLOv5s docs*

To get (or update) the trained model *[see this guide for more details](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)*:
1. collect training images (pictures of what you want to detect)
2. create a roboflow account and create a roboflow dataset following the prompts
3. after creating a dataset and labeling the images in roboflow, generate the set in the YOLOv5 format and select the view code option on the download page.
4. download the code and place it into the data directory in this project 
5. select a model based on the type of dataset
    ![models](https://github.com/ultralytics/yolov5/releases/download/v1.0/model_comparison.png)
    - For smaller datasets, it's best to pick YOLOv5s and then YOLOv5l for larger datasets
6. run the command  `python train.py --img 640 --batch 16 --epochs 10 --data <YAML FROM ROBOFLOW> --weights <MODEL SELECTED>`

To test against images clone this repository and then put the testing images into the test_imgs dir and type `python3 detect.py --weights ./best.pt  --source ./test_imgs` in a terminal to run a detection. It will output the resulted images into the runs directory.
To run against a webcam in real time run this command `python3 detect.py --weights ./best.pt  --source 0` changing the source to be 0.

### To create a venv (Using python 3.10+)
[*Guide for more help*](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
1. download virtualenv with pip3 (`pip3 install virtualenv`)
2. run `virtualenv <NAME OF VENV>`
3. enter the venv with
 - MAC/ LINUX: `source <NAME OF VENV>/bin/activate`. On 3.9 just run `source bin/activate`
 - WINDOWS: `<NAME OF VENV>\Scripts\activate`
4. install the required dependancies in the virtual environment using the requirments.txt (on x86 computers only, see below for ARM based machines) file: `pip3 install -r requirements.txt`

Close venv by typing `deactivate` into the terminal.

### Installing Dependancies on ARM

**IMPORTANT** *NOTE if you are on raspberry pi (or other ARMv7l - 32bit arch) you will need to install most of these manually...*
1. Install PyTorch [Here](https://github.com/ljk53/pytorch-rpi/blob/master/torch-1.6.0a0%2Bb31f58d-cp37-cp37m-linux_armv7l.whl) from [source](https://github.com/ljk53/pytorch-rpi) once downloading the .whl file run `pip install <PATH TO .whl FILE>`
2. Install OpenCV `pip install opencv-contrib-python==4.1.0.25` (this may take a while... up to 2 hours total)
3. Install TorchVision [Here](https://github.com/radimspetlik/pytorch_rpi_builds/blob/master/vision/torchvision-0.8.0a0%2B190a5f8-cp38-cp38-linux_armv7l.whl) Then change the file name to be `torchvision-0.8.0a0+190a5f8-cp37-cp37m-linux_armv7l.whl` (this ensures armv7l arch installable)

## To install packages on Nvidia Jetson Nano -- aarch64 see steps below

*See the .sh files to execute these easily*
1. Download Nvidia Docker container by running `sudo docker pull nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3`
2. Start the docker container with `sudo docker run -it --device=/dev/video0 --runtime nvidia --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3`
3. Clone this repository in the docker image `git clone https://github.com/cavineers/Vision2021.git`
5. Remove all unwanted folders and packages (everything but the YOLOv5_Trained_Model folder)
4. cd into the YOLOv5_Trained_Model directory.
5. Update pip and install packages: `python3 -m pip install --upgrade pip`, `python3 -m pip install --upgrade setuptools`, `pip install -r requirements.txt` (these will take several minutes to finish)
6. In a new terminal find the container id for your docker image using `sudo docker ps -a`
7. Still in the new terminal save the docker container using `sudo docker commit [CONTAINER ID] [IMAGE NAME]` (example image name would be yolov5/cavs:version1)
8. Run docker instance later `sudo docker run -it --device=/dev/video0 --runtime nvidia --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" [NEW IMAGE NAME]` (use -rm in the run command if you are not making any changes to the docker image to save space)

*Note: [Static IP](https://stackoverflow.com/questions/66384210/how-te-set-a-static-ip-for-a-jetson-nano) resources.*

## To Make Jetson Nano Run open.sh on boot use the following
In a new terminal type `sudo nano /etc/rc.local`
Enter this into the nano:

#!/bin/bash

exec > /tmp/rc-local.out 2>&1;set -x

sudo sh /path/to/sh/open.sh

*To install these packages on ARMarch - 64bit (not raspi or jetson) arch see steps below*
1. Visit [this site to find packages](http://mathinf.com/pytorch/arm64/)

### Credits
*Roboflow*
*YOLOv5*
