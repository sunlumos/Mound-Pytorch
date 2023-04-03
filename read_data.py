from torch.utils.data import Dataset
from PIL import Image
import cv2

img_path = "E:\S\code\CodeTest\Mound-Pytorch\hymenoptera_data\\train\\ants\\0013035.jpg"
img = Image.open(img_path)
print(img.size)
img.show

# class MyData(Dataset):
    
#     def __init__(self):
        