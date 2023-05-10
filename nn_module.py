import torch
from torch import nn

class Tudui(nn.Module):
    def __init__(self):
        super().__init__()
        
# __call__方法和forward方法在PyTorch中具有相同的作用，都用于定义模型的前向计算过程。当我们调用一个PyTorch模型对象时，Python会自动调用该对象中的__call__方法来执行前向计算，而__call__方法中会调用forward方法来实现计算过程
# 重写nn.module中的forward()方法 
    def forward(self, input):
        output = input + 1
        return output

tudui = Tudui()
# 创建了一个值为1.0的标量张量（Tensor），并将其赋值给变量x
x = torch.tensor(1.0)
output = tudui(x)
print(output)