import cv2    
import time
cpt = 0
maxFrames = 500 # if you want 5 frames only.

count=0
cap=cv2.VideoCapture('video1.mp4')
while cpt < maxFrames:
    ret, frame = cap.read()
    if not ret:
        break 
#    count += 1
#    if count % 3 != 0:
#        continue
    frame=cv2.resize(frame,(1080,500))
    cv2.imshow("test window", frame) # show image in window
    cv2.imwrite(r"C:\Users\sidda\Downloads\Yolov8-Counting-People-in-Queue-main\Yolov8-Counting-People-in-Queue-main\images\person_%d.jpg" %cpt, frame)
    time.sleep(0.01)
    cpt += 1
    if cv2.waitKey(5)&0xFF==27:
        break
cap.release()   
cv2.destroyAllWindows()
