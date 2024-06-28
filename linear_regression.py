import torch
import numpy as np
import matplotlib.pyplot as plt
import torch.nn as nn

# Step 1: Data Generation
np.random.seed(0)
x = np.random.rand(10, 1)
y = 2 * x + 1 + 0.1 * np.random.randn(10, 1)  # Linear relation with some noise

x_train = torch.tensor(x, dtype=torch.float32)
y_train = torch.tensor(y, dtype=torch.float32)

# Step 2: Model Definition
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # y = mx + c

    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()

# Step 3: Loss Function
criterion = nn.MSELoss()  # Mean Squared Error Loss

# Step 4: Optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent

# Step 5: Training Loop
num_epochs = 1000
losses = []

for epoch in range(num_epochs):
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)
    losses.append(loss.item())
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Step 6: Visualization
plt.plot(range(num_epochs), losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss over Training Iterations')
plt.show()

predicted = model(x_train).detach().numpy()
plt.scatter(x, y, label='Original data')
plt.plot(x, predicted, label='Fitted line', color='red')
plt.legend()
plt.show()
