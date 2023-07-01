from ultralytics import YOLO
import cv2
import time

model = YOLO('/home/suger01/Desktop/YOLOv8_FD/ultralytics/runs/detect/train9/weights/merged_data.pt')

my_camera = cv2.VideoCapture(0)

if not my_camera.isOpened():
    raise("No Camera")

while True:
    ret, image = my_camera.read()
    if not ret:
        break
    
    _time_mulai = time.time()
    
    result = model.predict(image, show=True)
    
    print('Urinov Azizbek', time.time()-_time_mulai)
    
    _key = cv2.waitKey(1)
    
    if _key == ord('q'):
        
        break
    
my_camera.release()
cv2.destroyAllWindows()
