#python -m streamlit run app.py

import streamlit as st
from PIL import Image
import numpy as np
import yolov5
from pathlib import Path
import shutil

dirpath = Path.cwd() / 'results'
#print(dirpath)
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)

# give a title to our app
st.title("Welcome to Natalia's fabulous recycling app!")

st.text('Hello, please take a picture of the object you wish to recycle.')
st.text("Make sure the lightening is good and the background isn't cluttered.")
st.text("I'll tell you if the object is biodegradable, cardboard, glass, metal, ")
st.text("paper or plastic and in which bin to throw it.")

material_dict = {
    0: ["Brown","biodegradable"],
    1: ["Blue", "cardboard"],
    2: ["Green", "glass"], 
    3: ["yellow", "metal"], 
    4: ["Blue", "paper"],
    5: ["Yellow", "plastic"]

}
    

# load model
model = yolov5.load('keremberke/yolov5m-garbage')
  
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image

imgbuffer = st.camera_input('')
#print(type(imgbuffer))
if imgbuffer:
    img = Image.open(imgbuffer)
    imgnp = np.array(img)
    #st.write(imgnp.shape)

    # perform inference
    results = model(img, size=640)

    # inference with test time augmentation
    #results = model(img, augment=True)

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4] # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    #print(categories)

    # show detection bounding boxes on image
    #results.show()

    results.save(save_dir='results/')

    st.image('results/image0.jpg')

    st.text("And remember, if you are in San Sebastian:")
    for category in categories:
        st.text(f"{material_dict[int(category)][1].title()} objects should go to the {material_dict[int(category)][0]} bin!")