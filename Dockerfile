FROM python:3.9-alpine

COPY ./* /app/

WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "gunicorn", "-w4", "main:app"]
