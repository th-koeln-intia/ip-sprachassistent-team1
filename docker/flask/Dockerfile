FROM python:3.7-alpine
ADD ./api/crontab.txt /crontab.txt
WORKDIR /api
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./api .
RUN pip install -r requirements.txt && chmod 755 ./entry.sh
EXPOSE 5000
CMD ["sh", "./entry.sh"]