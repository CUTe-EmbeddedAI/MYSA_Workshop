import cv2
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from torchvision import datasets

# load the model
model= models.resnet18(pretrained=True)
model.eval()

# load text file
class_label_path = 'imagenet_classes.txt'

with open(class_label_path) as f:
    class_labels = [line.strip() for line in f.readlines()]

# model = torch.load('spectacles.pt')
# model.eval()

# model.to('cpu')

# class_labels = ['specs', 'nospecs']

def preprocess_image(frame):
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485,0.456,0.406], [0.229,0.224,0.225])
    ])

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = transform(frame)
    frame = frame.unsqueeze(0) # add batch dimension

    return frame

# reading the image
capture = cv2.VideoCapture(0)

while True:

    isTrue, frame = capture.read()
    
    frame_tensor = preprocess_image(frame)

    # feedforward/ inference
    with torch.no_grad():
        output = model(frame_tensor)

    # postprocess output/ label
    _,predicted_class = output.max(1)
    predicted_class = predicted_class.item()

    predicted_class_name = class_labels[predicted_class]

    # label = f"Class: {predicted_class}"
    cv2.putText(frame,predicted_class_name,(10,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)

    cv2.imshow('video saya', frame)

    cv2.waitKey(1)


capture.release()

cv2.destroyAllWindows()

