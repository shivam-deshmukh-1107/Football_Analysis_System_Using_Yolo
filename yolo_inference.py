from ultralytics import YOLO

# Initial Training
# model = YOLO('yolov8x')
 
# results = model.predict('Input_Data/08fd33_4.mp4', save=True)

# print(results[0])
# print('------------------------------------------------------------------')
# for box in results[0].boxes:
#     print(box)

# Results saved in predict 

# --------------------------------------------------------------------------------------------------

# Prediction using weights using final training
model = YOLO('models/best.pt')
 
results = model.predict('Input_Data/08fd33_4.mp4', save=True)

print(results[0])
print('------------------------------------------------------------------')
for box in results[0].boxes:
    print(box)

# --------------------------------------------------------------------------------------------------