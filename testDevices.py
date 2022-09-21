import cv2 as cv 

def testDevice(source):
    cap = cv.VideoCapture(source) 
    print('Testing Source: ', source)

    if cap is None or not cap.isOpened():
       print('Warning: unable to open video source: ', source)
    else:
        print('Source Found: ', source)
        

for i in range(5):
    testDevice(i)