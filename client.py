# -*- coding: utf-8 -*-
import requests
import json
import numpy as np
# import cv2
import base64

def getByte(path):
    with open(path, 'rb') as f:
        img_byte = base64.b64encode(f.read())
    img_str = img_byte.decode('ascii')
    return img_str


img_str = getByte('./willSendPicture.jpg')


datas = {'file': img_str, 'classes': ['wcgz', 'wcaqm' ], 'vis_thresh':0.3}

print('datas')
print(datas)

req = json.dumps(datas)
r = requests.post("http://127.0.0.1:8000", data = req)


print(r.text)