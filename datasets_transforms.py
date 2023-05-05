import torchvision

train_set = torchvision.datasets.CIFAR10(root="./datasets", train=True, download=True)
test_set = torchvision.datasets.CIFAR10(root="./datasets", train=True, download=True)

