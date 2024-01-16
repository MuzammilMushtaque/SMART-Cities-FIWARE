# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Run Python_code_VS_DataEconomy.py when the container launches
CMD ["python", "./parking_manager.py"]
