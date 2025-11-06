# ---- Builder Stage ----
# This stage installs dependencies using Poetry
FROM python:3.10-slim as builder

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the necessary files for dependency installation
COPY pyproject.toml poetry.lock ./

# Install dependencies, without creating a virtual environment inside the image
# --no-root is optional, it skips installing the project itself
RUN poetry install --no-dev --no-root


# ---- Final Stage ----
# This stage builds the final, lean image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy your application code
COPY ./app /app

# Expose port and run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

