#python -m streamlit run app.py

import streamlit as st
from PIL import Image
import numpy as np
import yolov5
from pathlib import Path
import shutil

dirpath = Path.cwd() / 'results'
print(dirpath)
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)

# give a title to our app
st.title("Welcome to Natalia's fabulous recycling app!")

st.text("Hello, please take a picture of the object you wish to recycle. Make sure the lightening is good and the background isn't cluttered.")


# load model
model = yolov5.load('keremberke/yolov5m-garbage')
  
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image

imgbuffer = st.camera_input('cam')
print(type(imgbuffer))
if imgbuffer:
    img = Image.open(imgbuffer)
    imgnp = np.array(img)
    st.write(imgnp.shape)

# perform inference
results = model(img, size=640)

# inference with test time augmentation
#results = model(img, augment=True)

# parse results
predictions = results.pred[0]
boxes = predictions[:, :4] # x1, y1, x2, y2
scores = predictions[:, 4]
categories = predictions[:, 5]

# show detection bounding boxes on image
#results.show()

results.save(save_dir='results/')

st.image('results/image0.jpg')