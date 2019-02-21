import torch
import torch.utils.data
import torchvision.datasets.cifar as cifar


class MyData(torch.utils.data.Dataset):
    def __init__(self):
        super(MyData, self).__init__()

    def __getitem__(self, item):
        return item

    def __len__(self):
        return 10


dataset = MyData()
dataloader = torch.utils.data.DataLoader(dataset, 4, True)
for i, item in enumerate(dataloader):
    print(i, '  ', item)
