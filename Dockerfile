FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Files
COPY requirements.txt .
COPY src /app/src
COPY app.py .
COPY models /app/models

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install uvicorn
RUN pip install uvicorn

#Exposes the port
EXPOSE 8000

# Set the command to run the Python script
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]