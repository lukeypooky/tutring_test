from torch.utils.data.dataset import Dataset
import torch
from deep_learning import NkModel
from bloopblop import NkDataSet

csv_path = './test.csv'

custom_dataset = NkDataSet(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                    batch_size=1,
                                                    shuffle=False,
                                                    num_workers=1)

D_in = 30000
H = 1000
D_out = 4

model = NkModel(D_in, H, D_out)

criterion = torch.nn.CrossEntropyLoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)

for epoch in range(500):

    for i, data in enumerate(my_dataset_loader,0):

        images,label = data

        images = images.view(1,30000)
        print(images.size())
        print("label is label",label)
        y_pred = model(images)

        print(y_pred.size())
        print(label.size())

        loss = criterion(y_pred,label)

        print(epoch, loss.item())


        optimizer.zero_grad()
        loss.backward()
        optimizer.step()