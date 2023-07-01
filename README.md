:smile: 

# **FACE DETECTION with YOLOv5, YOLOv7 AND YOLOv8.**

------------
`Linux OS` `pytorch==1.12.1 ` `torchvision==0.13.1`  `torchaudio==0.12.1` 

`cudatoolkit=11.3 -c pytorch` ` labelImg` 

:fa-tags: ***Other requirements may change according to the versions of the tools of YOLOs.***


- If we want to use `comet` vizualization tool for any Yolo versions, **Don't forget, open comet account first and use comet API to train the YOLO model **and we can get good vizualization results. For more check this link :

[https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb](https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb)

 ## **YOLOv5 Face Detection** :tw-35-20e3:

Check this link to learn about YOLOv5 : [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)

1.**TRAIN: **  

    python train.py --batch 4 --epochs 50 --data data/mix_data.yaml --weights yolov5n6.pt

- `train.py ` (available in official YOLOv5 git repo or you can find in YOLOv5 folder in this repo)

- `batch size`  can be modify in my case **GPU 3060 **with **12GB** memory, so I used 4. 
-   `epoch ` can be change in my case dataset and pre trained model is not big so I used 50.

-  `mix_data.yaml` (learn how to create from official YOLO repos. my one is available in my 

      repo.)
- ` yolov5n6.pt` (pre trained YOLOv5 model can be download from [https://github.com

  /ultralytics/yolov5](https://github.com/ultralytics/yolov5) or **request me)**
  
  
 :tw-1f352: ** You can check results.jpg to see results(YOLOv5 folder in repo).** 
 
 

------------


  ## **YOLOv7 Face Detection**  :tw-37-20e3:

Check this link to learn about YOLOv7 : [https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)

1.**TRAIN: **  

    python train.py --batch 4 --epochs 50 --data data/mix_data.yaml --weights yolov7-w6.pt

- `train.py ` (available in official YOLOv7 git repo or you can find in YOLOv7 folder in this repo)

- `batch size`  can be modify in my case **GPU 3060 **with **12GB** memory, so I used 4. 
-   `epoch ` can be change in my case dataset and pre trained model is not big so I used 50.

-  `mix_data.yaml` (learn how to create from official YOLO repos. my one is available in my 

      repo.)
- ` yolov7-w6.pt` (pre trained YOLOv7 model can be download from [https://github.com

 /WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7) or **request me)**
  
  
 :tw-1f352: ** You can check results.jpg to see results(YOLOv7 folder in repo).** 
 
 ------------


  ## **YOLOv8 Face Detection**  :tw-38-20e3:

Check this link to learn about YOLOv8 : [https://github.com/ultralytics](https://github.com/ultralytics)

1.**TRAIN: **  

    python train.py --batch 4 --epochs 50 --data data/mix_data.yaml --weights yolov8m.pt

- `train.py ` (available in official YOLOv8 git repo or you can find in YOLOv8 folder in this repo)

- `batch size`  can be modify in my case **GPU 3060 **with **12GB** memory, so I used 4. 
-   `epoch ` can be change in my case dataset and pre trained model is not big so I used 50.

-  `mix_data.yaml` (learn how to create from official YOLO repos. my one is available in my 

      repo.)
- ` yolov8m.pt` (pre trained YOLOv7 model can be download from  [https://github.com/ultralytics](https://github.com/ultralytics) or **request me)**
  
  
 :tw-1f352: ** You can check results.jpg to see results(YOLOv8 folder in repo).** 
 
 
 

------------


:tw-26a0: **SUGER TRICKS : **  :tw-26a0: 

1.  When trying to train YOLOv7, please check `loss.py `  file and check device and change it 

 to `cuda.`
 
2. If your training data is big use `train.py` in** YOLOv7**, if it is small use `train_aux.py`

3. ALL YOLO use strick dataset format:

 **Dataset**
 |
 |----------------**images_folder** (load all images one by one)
 |
 |
 |----------------**labels** (load all labels .txt files here)
 
1.  `labelImg` data labeling can be use in **Windows and MacOS OS not in LINUX**
 
 
 

------------
### **RESULT: **


I used` run_OpenCV.py `file to run live stream face detection with is powered with YOLOv8.

Check repo there is that file. 


:tw-1f4fa:  **LIVE DEMO : ** [https://youtu.be/xZDQq-44Euk](https://youtu.be/xZDQq-44Euk)


------------


### REFERENCES:

- [https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)-
- https://github.com/ultralytics/yolov5
- https://github.com/ultralytics/ultralytics
- https://docs.ultralytics.com/
- https://github.com/heartexlabs/labelImg

------------


# Thank You :tw-1f381: :tw-1f381: :tw-1f381:
