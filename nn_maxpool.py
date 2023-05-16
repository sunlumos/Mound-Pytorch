import torch
from torch import nn
from torch.nn import MaxPool2d

input = torch.tensor([[1,2,0,3,1],
[0,1,2,3,1],[1,2,1,0,0],[5,2,3,1,1],[2,1,0,1,1]])

input = torch.reshape(input,(-1,1,5,5))
print(input.shape)

# 搭建神经网络
class Tudui(nn. Module):
    # 神经网络初始化，__init__方法是nn.Module类中的一个特殊方法，用于初始化模型的各个组件，例如卷积层、池化层、全连接层等
    def __init__(self):
        # Tudui类是一个自定义的类，它继承自某个父类（例如nn.Module类）。当定义Tudui类时，我们需要通过调用父类的构造函数来初始化Tudui类的实例。因此，在Tudui类的__init__()方法中，通常需要调用super(Tudui, self).init()来首先调用父类的构造函数，以确保父类的属性和方法能够被正确地初始化
        super(Tudui,self).__init__()
        self.maxpool1 = MaxPool2d(kernel_size=3,ceil_mode=True)

    def forward(self, input) :
        output = self.maxpool1(input)
        return output
    

