FROM python:alpine

EXPOSE 80

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

RUN pip install gunicorn
RUN pip install falcon
RUN pip install qrcode[pil]

COPY ./app /app
WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0:80", "-w", "3", "main:app"]
