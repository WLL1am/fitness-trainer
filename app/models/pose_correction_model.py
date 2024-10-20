import torch
import torch.nn as nn

class PoseCorrectionModel(nn.Module):
    def __init__(self):
        super(PoseCorrectionModel, self).__init__()
        self.fc1 = nn.Linear(34, 64)
        self.fc1 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 3)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        
        return self.fc3(x)
    
model = PoseCorrectionModel()
print(model)