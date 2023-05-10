import torchvision
from torch.utils.tensorboard import SummaryWriter
dataset_transform = torchvision.transforms.Compose([
torchvision.transforms .ToTensor()
])
train_set = torchvision.datasets.CIFAR10(root="./datasets", train=True, transform= dataset_transform, download=False)
test_set = torchvision.datasets.CIFAR10(root="./datasets", train=False, transform= dataset_transform, download=False)

print(test_set[0])

writer = SummaryWriter("p10")
for i in range(10):
    img, target = test_set[i]
    writer.add_image("test_set", img, i)
    
writer.close()

# print(test_set.classes)

# img, target = test_set[0]
# print(img)
# print(target)
# # 展示类别
# print(test_set.classes[target])

# img.show()