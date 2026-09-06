# Base image: lightweight Python
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (this layer gets cached if requirements don't change)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Document which port the container listens on
EXPOSE 5000

# Command to run when container starts
CMD ["python", "app.py"]