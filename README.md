# Cyclone tracking
The next step in this project  to track the using an 3d Convolutional LSTM model to generate predict cyclone movement over time but as there aren't many datasets available for this purpose we cannot continue further and have put this project on hold.

## 1. Cyclone eye Detection

This repository contains code for a model that predicts the x-y pixel location of the cyclone eye in an infrared satellite image. The model is trained on infrared satellite images (taken from https://www.kaggle.com/datasets/sshubam/insat3d-infrared-raw-cyclone-images-20132021, Korean Metereological Administration  and a few other sources). This project includes training VGG19, DenseNet, Xception and ResNet to predict a point on an image and creating a simple GUI to make it more accessible for non-technically oriented users to easily compare their output themselves. On average, the most accurate of all these turned out to be VGG19 with an averager error of 0.02, closely followed by Xception, whereas DenseNet was usually off by a magnitude of 10 pixels and ResNet was highly inaccurate.

## How to Use
To use the code, ensure you have Python 3.7 or higher and clone this repo. Then simply install the requirements by running
``` pip install -r requirements.txt``` 
or you can install the following yourself
```
tensorflow==2.10 # A machine learning framework
numpy # A library for scientific computing
Pillow # A library for image processing
pandas # A library for data analysis
matplotlib # A library for data visualization
seaborn # A library for statistical data visualization
glob # A module for pathname pattern matching
tkinter # A standard Python interface to the Tk GUI toolkit (should be present by default)
```
After installing the above, download the models from the link available in the next section. To use the GUI, simply run the following command in the terminal.
```
python3 UI_zoom.py
```
or
```
python3 UI_WithLoad.py
```
*Note the above commands mioght not run in windows. In that case replace ```python3``` by ```python``` .
Also if ```pip``` doesn't work try ```pip3```.

To try training the Models yourself you can use the cyclonev1-0.ipynb file.
All you need to do is uncomment import statement for the required model and set the base_model as it.

## Trained Models
All the trained models are available at https://drive.google.com/drive/folders/1_SyshvdaHpnMJFS67Nxkr3w2Xib48tFk?usp=sharing

## GUI
There are two UI files:

### UI Load
This UI contains a separate load button for loading the model which makes it so that each time you load an image you don't reload the image everytime you use upload an image
so you can run more predictions before running out of memory.

![image](https://github.com/hercules2209/Cyclone/assets/106009563/9e7ebac6-1b5d-4e20-83c7-2afc576b1d77)

![image](https://github.com/hercules2209/Cyclone/assets/106009563/441a7a0c-aa6a-4de4-9eee-0523e9d03662)

### UI Zoom
In this we try to zoom on the cyclone eye by simply cropping the image around it and then resizing it. It is not perfect but works well enough.

![image](https://github.com/hercules2209/Cyclone/assets/106009563/47a33299-f17e-40e5-90c2-e8cb72997c78)
![image](https://github.com/hercules2209/Cyclone/assets/106009563/0a4df3e9-a2e8-438f-8677-39d0ba33cbee)


