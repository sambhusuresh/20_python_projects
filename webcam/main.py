import cv2

imgc = cv2.VideoCapture(0)

result = True 

while(result):
    ret, frame = imgc.read()
    cv2.imwrite("test.jpg", frame)
    result = False
    print("done")

imgc.release()