# Use the official Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements first to leverage Docker caching
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy the .env file BEFORE copying everything else
COPY .env /app/.env

# Copy the rest of the application code
COPY . .

# Expose port 8000 (Django default)
EXPOSE 8000

# Run Django server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
