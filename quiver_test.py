# -*- coding: utf-8 -*-
from keras.applications.vgg16 import VGG16
from quiver_engine import server
model = VGG16()

server.launch(model,
              input_folder='./sample_images/冨田鈴花', temp_folder='./tmp', port=8000)
