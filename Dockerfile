FROM python 37
WORKDIR /app

COPY . . 

RUN pip install --no-cache-dir flag -r requirements.txt

CMD ["gunicorn, "-b", "0.0.0.0:8080", "main:app"]