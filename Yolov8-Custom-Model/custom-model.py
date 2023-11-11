# pls do this today
from ultralytics import YOLO

if __name__ == "__main__":
    # model = YOLO("../Yolo-Weights/yolov8n.pt")
    model = YOLO("yolov8n.yaml")
    results = model.train(data="config.yaml", epochs=50)

