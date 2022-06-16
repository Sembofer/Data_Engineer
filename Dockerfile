FROM python:3.10-alpine3.16

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip \
    && pip --no-cache-dir install -r requirements.txt

CMD ["python", "pipeline/app.py"]