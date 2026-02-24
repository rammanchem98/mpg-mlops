FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of your local app folder into the container's /app folder
COPY app/ .

# Since we are already IN the /app folder (from WORKDIR), 
# we just need to point to the file 'app.py' and the variable 'app'
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
