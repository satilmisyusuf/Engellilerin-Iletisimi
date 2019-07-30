import cv2
import cv2
import numpy as np
from keras.models import load_model
from keras.models import model_from_json


save_dir1='./model1'
save_dir2='./model2'
save_dir3='./model3'
IMG_SIZE = 150



class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

        with open(save_dir1+"/model_json.json", 'r') as f:
            self.model1 = model_from_json(f.read())
        self.model1.load_weights(save_dir1+"/model.h5")

        with open(save_dir2+"/model_json.json", 'r') as f:
            self.model2 = model_from_json(f.read())
        self.model2.load_weights(save_dir2+"/model.h5")


        with open(save_dir3+"/model_json.json", 'r') as f:
            self.model3 = model_from_json(f.read())
        self.model3.load_weights(save_dir3+"/model.h5")

    
    def __del__(self):
        self.video.release()



    
    def get_frame(self):
        success, image = self.video.read()
        image  = cv2.resize(image, (640, 480)) 
        image = cv2.flip( image, 1 )
        x1, y1, x2, y2 = 201, 251, 440, 480
        img_cropped = image[y1:y2, x1:x2]

        
        #cv2.imwrite("_ori.jpg",img)
     
        
        test_image  = cv2.resize(img_cropped, (IMG_SIZE, IMG_SIZE)) 
        test_image = np.expand_dims(test_image, axis = 0)
        result1 = self.model1.predict(test_image)
        result2 = self.model2.predict(test_image)
        result3 = self.model3.predict(test_image)

        tmp1 = '='
        if result1[0][0] == 1:
            tmp1 =  '0'
        elif result1[0][1] == 1:
            tmp1 =  '1'
        elif result1[0][2] == 1:
            tmp1 =  '2'
        elif result1[0][3] == 1:
            tmp1 =  '3'
        elif result1[0][4] == 1:
            tmp1 =  '4'
        elif result1[0][5] == 1:
            tmp1 =  '5'
        elif result1[0][6] == 1:
            tmp1 =  '6'
        elif result1[0][7] == 1:
            tmp1 =  '7'
        elif result1[0][8] == 1:
            tmp1 =  '8'
        elif result1[0][9] == 1:
            tmp1 =  '9'
        elif result1[0][10] == 1:
            tmp1 =  '10'
        elif result1[0][11] == 1:
            tmp1 =  '11'
        elif result1[0][12] == 1:
            tmp1 =  '12'
        elif result1[0][13] == 1:
            tmp1 =  '13'
        elif result1[0][14] == 1:
            tmp1 =  '14'
        elif result1[0][15] == 1:
            tmp1 =  '15'
        elif result1[0][16] == 1:
            tmp1 =  '16'
        elif result1[0][17] == 1:
            tmp1 =  '17'
        elif result1[0][18] == 1:
            tmp1 =  '18'
        elif result1[0][19] == 1:
            tmp1 =  '19'

        
        tmp2 = '='
        if result2[0][0] == 1:
            tmp2 =  '0'
        elif result2[0][1] == 1:
            tmp2 =  '1'
        elif result2[0][2] == 1:
            tmp2 =  '2'
        elif result2[0][3] == 1:
            tmp2 =  '3'
        elif result2[0][4] == 1:
            tmp2 =  '4'
        elif result2[0][5] == 1:
            tmp2 =  '5'
        elif result2[0][6] == 1:
            tmp2 =  '6'
        elif result2[0][7] == 1:
            tmp2 =  '7'
        elif result2[0][8] == 1:
            tmp2 =  '8'
        elif result2[0][9] == 1:
            tmp2 =  '9'
        elif result2[0][10] == 1:
            tmp2 =  '10'
        elif result2[0][11] == 1:
            tmp2 =  '11'
        elif result2[0][12] == 1:
            tmp2 =  '12'
        elif result2[0][13] == 1:
            tmp2 =  '13'
        elif result2[0][14] == 1:
            tmp2 =  '14'
        elif result2[0][15] == 1:
            tmp2 =  '15'
        elif result2[0][16] == 1:
            tmp2 =  '16'
        elif result2[0][17] == 1:
            tmp2 =  '17'
        elif result2[0][18] == 1:
            tmp2 =  '18'
        elif result2[0][19] == 1:
            tmp2 =  '19'

        
        tmp3 = '='
        if result3[0][0] == 1:
            tmp3 =  '0'
        elif result3[0][1] == 1:
            tmp3 =  '1'
        elif result3[0][2] == 1:
            tmp3 =  '2'
        elif result3[0][3] == 1:
            tmp3 =  '3'
        elif result3[0][4] == 1:
            tmp3 =  '4'
        elif result3[0][5] == 1:
            tmp3 =  '5'
        elif result3[0][6] == 1:
            tmp3 =  '6'
        elif result3[0][7] == 1:
            tmp3 =  '7'
        elif result3[0][8] == 1:
            tmp3 =  '8'
        elif result3[0][9] == 1:
            tmp3 =  '9'
        elif result3[0][10] == 1:
            tmp3 =  '10'
        elif result3[0][11] == 1:
            tmp3 =  '11'
        elif result3[0][12] == 1:
            tmp3 =  '12'
        elif result3[0][13] == 1:
            tmp3 =  '13'
        elif result3[0][14] == 1:
            tmp3 =  '14'
        elif result3[0][15] == 1:
            tmp3 =  '15'
        elif result3[0][16] == 1:
            tmp3 =  '16'
        elif result3[0][17] == 1:
            tmp3 =  '17'
        elif result3[0][18] == 1:
            tmp3 =  '18'
        elif result3[0][19] == 1:
            tmp3 =  '19'

     
                
        
        
        print ("Predict Result ==> ", tmp1,tmp2,tmp3 )

        cv2.rectangle(image, (x1, y1), (x2, y2), (255,0,0), 2)
        cv2.putText(image, tmp1, (500,90), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255),5)
        
        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes(), "Predict Result ==> "+ tmp1 