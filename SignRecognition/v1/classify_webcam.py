import cv2
import numpy as np
from keras.models import load_model

IMG_SIZE = 64

def x3():
    if result[0][0] == 1:
          return '0'
    elif result[0][1] == 1:
          return '1'
    elif result[0][2] == 1:
          return '2'
    elif result[0][3] == 1:
          return '3'
    elif result[0][4] == 1:
          return '4'
    elif result[0][5] == 1:
          return '5'
    elif result[0][6] == 1:
          return '6'
    elif result[0][7] == 1:
          return '7'
    elif result[0][8] == 1:
          return '8'
    elif result[0][9] == 1:
          return '9'





model = load_model('Trained_model_vgg16.h5')
print (model.summary())
print("")
print("")
print("")
print("")

cap = cv2.VideoCapture(0)



while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    
    if ret:
        print (img.shape)

        x1, y1, x2, y2 = 800, 100, 1200, 500
        img_cropped = img[y1:y2, x1:x2]

        
        #cv2.imwrite("_ori.jpg",img)
     
        test_image  = cv2.resize(img_cropped, (IMG_SIZE, IMG_SIZE)) 
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        tmp = str(x3())
        print ("Predict Result ==> "+ tmp )

        cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
        cv2.putText(img, tmp, (900,90), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255),5)

        cv2.imshow('sequenddce', img)
        a = cv2.waitKey(1) 
        if a == 27: 
                break     
    else:
        print("kamera hatasi")

cv2.destroyAllWindows() 
cv2.VideoCapture(0).release()
