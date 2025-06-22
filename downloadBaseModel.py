from ultralytics import YOLO

# YOLOv8n (Ultralytics Nano model) used as the base model
model = YOLO('yolov8n.pt')
model.save('models/yolov8n.pt')
