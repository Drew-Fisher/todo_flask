FROM python:3-alpine3.10

COPY app /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN apk add --no-cache bash
#CMD ["python", "app.py"]

EXPOSE 5000

CMD ["bash", "scripts/app_run.sh"]