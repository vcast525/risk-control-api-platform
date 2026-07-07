## Use the official Python runtime as the base image
FROM python:3.13-slim


## Set the working directory inside the container
WORKDIR /app


## Copy the dependency file into the container
COPY requirements.txt .


## Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


## Copy the application files into the container
COPY . .


## Expose the FastAPI application port
EXPOSE 8000


## Start the FastAPI application
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]