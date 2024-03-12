# Use an official Python runtime as a parent image
FROM python:alpine

# Set the working directory in the container
WORKDIR /prediction_app

# Copy the current directory contents into the container at /app
COPY template/ .

# Install any needed dependencies specified in requirements.txt
RUN apk add --no-cache gcc g++ musl-dev
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "prediction_app.py"]
