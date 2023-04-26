# 🌍 Recycle App

## Table of Contents

- [1. Description](#Description)
- [2. Installation](#Installation)
- [3. Usage](#Usage)
- [4. Model](#Model)
- [5. Data](#Data)
- [5. Contributing](#Contributing)
- [6. License](#license)

## Description

This is a simple Streamlit app that utilizes computer vision to detect and classify objects based on their material (biodegradable, cardboard, glass, metal, paper, and plastic). The app also provides information on the color of the bin in which the object should be thrown. This is based on the recycling guidelines of [San Sebastian/Donostia](https://www.donostia.eus/ataria/es/web/ingurumena/residuos/informacion-para-residentes/reciclaje), in Spain, although it could be adapted to other cities.


## 🚀 Installation

To run this app, you will need to have the following installed:

    Python 3.7+
    Streamlit
    PyTorch
    YOLOv5

To install the required Python packages, run the following command:

    ```
    pip install -r requirements.txt
    ```

## 💻 Usage

To run the app, use the following command:

    ```
    python3 -m streamlit run app/app.py
    ```

Once the app is running, you can take a picture, either from your phone or your computer. The app will then analyze the image and identify any objects in the image along with their material classification. The app will also display a bounding box around each object and indicate the color of the bin in which the object should be thrown.

## 🧠 Model

The object detection model used in this app is YOLOv5, which was fine-tuned for 30 epochs on the recycling materials dataset to classify objects into six categories. YOLOv5 was chosen for its speed and accuracy, which make it ideal for real-time applications like this one.


## 💾 Data

The dataset used in this project came from: https://universe.roboflow.com/material-identification/garbage-classification-3/dataset/. This is the size of its partitions:

|      | **Training** | **Dev** | **Test** |
|------------|--------------|---------|----------|
| **Images** | 7.3k         | 2.1k    | 1k       |


## 🤝 Contributing

We welcome contributions to this project! If you would like to contribute, please fork this repository and submit a pull request with your changes.

## 📝 License

The MIT License (MIT)
Copyright (c) 2023, Natalia Flechas Manrique