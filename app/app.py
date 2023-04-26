# python3 -m streamlit run app.py

import streamlit as st
from PIL import Image
import numpy as np
import yolov5
from pathlib import Path
import shutil

dirpath = Path.cwd() / 'results'
model_path = Path.cwd() / 'models'
#print(dirpath)
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)


st.title("Recycling app!")


st.markdown("""Hello, please take a picture of the object you wish to recycle. \\ 
               Make sure the lightening is good and the background isn't cluttered. \\
               I'll tell you if the object is biodegradable, cardboard, glass, metal, \\
               paper or plastic and in which bin to throw it.""")

material_dict = {
    0: ("Brown","biodegradable"),
    1: ("Blue", "cardboard"),
    2: ("Green", "glass"), 
    3: ("yellow", "metal"), 
    4: ("Blue", "paper"),
    5: ("Yellow", "plastic")  

}
    

# load model
#model = yolov5.load('keremberke/yolov5m-garbage')  
model = yolov5.load(model_path / 'best.pt') 

# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image

imgbuffer = st.camera_input('')


if imgbuffer:
    img = Image.open(imgbuffer)
    imgnp = np.array(img)
    #st.write(imgnp.shape)

    # perform inference
    results = model(img, size=640)

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4] # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    st.image(results.render()) # Render the results with the bounding boxes and the labels.

    
    if len(categories) > 0:
        st.markdown("And remember, if you are in San Sebastian:")
        for category in categories:
            st.markdown(f"{material_dict[int(category)][1].title()} objects should go to the **{material_dict[int(category)][0].title()}** bin!")
    else:
        st.markdown("No object has been recognized, try again with a better picture!")


st.markdown("By Natalia Flechas Manrique")