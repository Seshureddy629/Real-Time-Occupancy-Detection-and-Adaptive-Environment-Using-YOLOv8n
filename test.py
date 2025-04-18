import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np

model=YOLO('best.pt')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
  
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
            
        



cap=cv2.VideoCapture('testvideo.mp4')


my_file = open("coco1.txt.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)



count=0
area1=[(640,164),(970,160),(995,383),(621,406)]
area2=[(625,174),(565,475),(120,460),(365,170)]
area3=[(350,162),(110,460),(2,440),(10,117)]

while True:    
    ret,frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,500))
    results=model.predict(frame)
    #print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
   

    #print(px)
    list1=[]
    list2=[]
    list3=[]
    for index,row in px.iterrows():
       # print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        cx=int(x1+x2)//2
        cy=int(y1+y2)//2
        w,h=x2-x1,y2-y1
        result=cv2.pointPolygonTest(np.array(area1,np.int32), ((cx,cy)),False)
        if result>=0:
#        cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),-1)
           cvzone.cornerRect(frame,(x1,y1,w,h),3,2)
           cv2.circle(frame,(cx,cy),4,(255,0,0),-1)
           cvzone.putTextRect(frame,f'Head',(x1,y1),1,1)
           list1.append(cx)
        result1=cv2.pointPolygonTest(np.array(area2,np.int32), ((cx,cy)),False)
        if result1>=0:
#        cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),-1)
           cvzone.cornerRect(frame,(x1,y1,w,h),3,2)
           cv2.circle(frame,(cx,cy),4,(255,0,255),-1)
           cvzone.putTextRect(frame,f'Head',(x1,y1),1,1)
           list2.append(cx)
        result2=cv2.pointPolygonTest(np.array(area3,np.int32), ((cx,cy)),False)
        if result2>=0:
#        cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),-1)
           cvzone.cornerRect(frame,(x1,y1,w,h),3,2)
           cv2.circle(frame,(cx,cy),4,(255,0,255),-1)
           cvzone.putTextRect(frame,f'Head',(x1,y1),1,1)
           list3.append(cx)
        
        
        cr1=len(list1)
        cr2=len(list2)
        cr3=len(list3)
        cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,0,255),2)
        cv2.polylines(frame,[np.array(area2,np.int32)],True,(0,0,255),2)
        cv2.polylines(frame,[np.array(area3,np.int32)],True,(0,0,255),2)
        cvzone.putTextRect(frame,f'Zone1:-{cr1}',(30,50),1,1)
        cvzone.putTextRect(frame,f'Zone2:-{cr2}',(30,90),1,1)
        cvzone.putTextRect(frame,f'Zone3:-{cr3}',(30,140),1,1)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
