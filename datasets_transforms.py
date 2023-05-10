import torchvision

train_set = torchvision.datasets.CIFAR10(root="./datasets", train=True, download=False)
test_set = torchvision.datasets.CIFAR10(root="./datasets", train=False, download=False)

print(test_set[0])
print(test_set.classes)

img, target = test_set[0]
print(img)
print(target)
# 展示类别
print(test_set.classes[target])

img.show()