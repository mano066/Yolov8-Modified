# itrash-recycling-detection


How to use:

"capture image"

```
python image_capture.py
```

"Train"

```
yolo task=detect mode=train epochs=100 data=data_custom.yaml model=best.pt imgsz=640 batch=6
```

yolov8x.

1> prediction 1-18
2> train - 1- 13
3> val 1- 24.

yolov8n

1> train 14-