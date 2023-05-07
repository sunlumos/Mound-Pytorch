import torchvision

train_set = torchvision.datasets.CIFAR10(root="./datasets", train=True, download=False)
test_set = torchvision.datasets.CIFAR10(root="./datasets", train=False, download=False)

print(test_set[0])