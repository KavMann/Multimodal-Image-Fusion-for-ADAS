from ultralytics import YOLO
print("--Starting!!--")
model = YOLO("yolov8n.yaml")
results = model.train(data="./Multimodal-Image-Fusion/data-train-ir.yaml",epochs=100)
print("\n--End--")