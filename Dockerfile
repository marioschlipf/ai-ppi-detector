# ---- Base Stage ----
FROM python:3.11-slim

# Install libmagic
RUN apt-get update && apt-get install -y libmagic1 libgl1 libglib2.0-0

# Set working directory
WORKDIR /code

# Set python path
ENV PYTHONPATH=/code

# Copy requirements and install dependencies
COPY ./requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY ./app /code/app


# Expose port and run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

