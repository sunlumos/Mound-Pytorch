from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter


# import cv2 


# python的用法 =》 tensor数据类型  两个问题：
# 1.如何使用transforms
# 2.为什么我们需要Tensor数据类型

img_path = "./hymenoptera_data/train/ants/0013035.jpg"
img = Image.open(img_path)
# opencv读取图像
# cv_img = cv2.imread(img_path)

writer = SummaryWriter("logs")

#! 1.如何使用transforms
# 将图像转化为tensor类型
tensor_trans = transforms.ToTensor()
# tensor_trans(img)实际上是调用了transforms.ToTensor().__call__(img)，其中img是输入参数。
tensor_img = tensor_trans(img) 

# print(tensor_img)

writer.add_image("Tensor_img", tensor_img)

writer.close() 