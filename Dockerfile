FROM python:3.12.9-slim

# RUN apt-get update
# RUN apt-get install --no-install-recommends -y netcat-traditional nano curl python3-dev default-libmysqlclient-dev gcc pkg-config

# Set environment variables
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc curl build-essential libpq-dev && \
    pip install pipenv && \
    apt-get clean

# Set working directory
WORKDIR /app

# WORKDIR /opt/app
# ADD Pipfile* /opt/app/
# RUN pip install pipenv && pipenv install

# RUN apt -y remove gcc && apt -y autoremove && apt -y autoclean
# Copy Pipenv files first (for better Docker caching)
COPY Pipfile Pipfile.lock ./

# Install Python dependencies using pipenv
RUN pipenv install --system --deploy

COPY ./app ./app

# Set PYTHONPATH to ensure `app` is importable
ENV PYTHONPATH=/app

# COPY . /opt/app
EXPOSE 8004

# CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "127.0.0.1:8004"]
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8004"]
