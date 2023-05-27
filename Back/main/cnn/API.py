import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import base64
import io
import matplotlib.image as mpimg
import cv2
import numpy as np
from keras.models import load_model
from PIL import Image


app = FastAPI()

image_x, image_y = 64,64

classifier = load_model('/Users/tejada/Documents/GitHub/cnn-libras/models/other_models/model_epoch_48_98.6_final.h5')

classes = 21
letras = {'0' : 'A', '1' : 'B', '2' : 'C', '3': 'D', '4': 'E', '5':'F', '6':'G', '7': 'I', '8':'L', '9':'M', '10':'N', '11': 'O', '12':'P', '13':'Q', '14':'R', '15':'S', '16':'T', '17':'U', '18':'V', '19':'W','20':'Y'}

def base64_to_image(imagem64):
    i = base64.b64decode(imagem64)
    i = io.BytesIO(i)
    i = mpimg.imread(i, format='JPG')
    
    return i


def predictor(test_image):          
       test_image = image.img_to_array(test_image)
       test_image = np.expand_dims(test_image, axis = 0)
       result = classifier.predict(test_image)
       maior, class_index = -1, -1

       for x in range(classes):      
           
           if result[0][x] > maior:
              maior = result[0][x]
              class_index = x
       
       return [result, letras[str(class_index)]]


class MyData(BaseModel):
    letter: str

@app.post("/getLetter")
def getLetter(data: MyData):
        img_text = ['','']
        print(data.letter)
            
        i = base64.b64decode(data.letter)
        i = io.BytesIO(i)
        i = mpimg.imread(i, format='JPG')

        frame = i
        print("frame" )
        # try:
        img_text = ['','']

        frame = cv2.flip(frame,1)
        print("flip" )

        output = np.ones((150, 150, 3)) * 255 #imagem 150x150, com fundo branco e 3 canais para as cores

        cv2.putText(output, str(img_text[1]), (15, 130), cv2.FONT_HERSHEY_TRIPLEX, 6, (255, 0, 0))

        cv2.imshow("ROI", frame)
        cv2.imshow("FRAME", frame)
        cv2.imshow("PREDICT", output)

        imggray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        save_img = cv2.resize(imggray, (image_x, image_y))
        # cv2.imwrite(save_img)
        print("resize")

        img_text = predictor(save_img)
        print("predictor")

        return(str(img_text[1]))
        
        # except:
        #     return "Não encontrei"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
