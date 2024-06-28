# Use the official PyTorch image with Python 3.8
FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Run the script
CMD ["python", "linear_regression.py"]
