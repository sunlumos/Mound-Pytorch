import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# 准备的测试集
test_data = torchvision.datasets.CIFAR10(root="./datasets", train=False, transform= torchvision.transforms.ToTensor(), download=False)

# dataset=test_data：指定要加载的数据集为test_data。
# batch_size=4：指定每个batch的大小为4。每次取4个数据进行打包
# shuffle=True：指定在每个epoch中对数据进行混洗操作。
# num_workers=0：指定数据加载的进程数目，0表示在主进程中加载数据。
# drop_last=False：如果数据集大小不能被batch大小整除，是否丢弃最后的不足一个batch的数据。这里设置为False表示不丢弃，保留不足一个batch的数据。
test_loader = DataLoader(dataset=test_data, batch_size=4, shuffle=True, num_workers=0, drop_last=False)

# 测试数据集中的第一张图片
img, target = test_data[0]
print(img.shape)
print(target)

# SummaryWriter函数的参数"dataloader"指定了日志文件的保存目录，所有的日志数据都将保存在这个目录下。
writer = SummaryWriter("dataloader")
step = 0
for data in test_loader:
    imgs, targets = data
    # print(imgs.shape)
    # print(targets)
    writer.add_images("test_data", imgs, step)
    step+=1
    
writer.close()
    
    