from PIL import Image

img_path = "D:\S\start\code\CodeTest\Mound-Pytorch\hymenoptera_data\\val\\ants\800px-Meat_eater_ant_qeen_excavating_hole.jpg"

img = Image.open(img_path)

print(img.size, img.format)
img.show()