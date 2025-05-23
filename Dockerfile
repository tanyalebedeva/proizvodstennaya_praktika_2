FROM python:3.9-slim

WORKDIR /usr/src/app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app/main.py"]
