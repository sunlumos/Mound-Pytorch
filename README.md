# Mound-Pytorch
B站小土堆pytorch学习

## dataset
Dataset（数据集）是指训练、验证或测试模型所使用的数据的集合。Dataset通常由数据样本组成，每个样本包含一个或多个特征和相应的标签或目标值。
## dataloader
负责取出数据
## nn.Module
神经网络模型
nn中的__call__方法和forward方法在PyTorch中具有相同的作用，都用于定义模型的前向计算过程。当我们调用一个PyTorch模型对象时，Python会自动调用该对象中的__call__方法来执行前向计算，而__call__方法中会调用forward方法来实现计算过程