FROM python3.7-slim
WORKDIR /app

COPY . . 

RUN pip install --no-cache-dir flag -r requirements.txt

CMD ["gunicorn, "-b", "0.0.0.0:8080", "main:app"]