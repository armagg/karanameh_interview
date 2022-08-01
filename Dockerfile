FROM python:3.9-alpine

COPY ./main.py /app/main.py
COPY ./src/* /app/src/
COPY ./scripts /app/scripts/
COPY ./.env /app/.env
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

EXPOSE 8000
RUN pip install -r requirements.txt

# CMD [ "tail", "-f", "/dev/null" ]
CMD [ "gunicorn", "-w4","--bind=0.0.0.0:8000", "main:app"]
