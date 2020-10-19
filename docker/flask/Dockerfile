FROM python:3.7-alpine
WORKDIR /api
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./api .
RUN pip install -r requirements.txt && python init.py
EXPOSE 5000
CMD ["flask", "run"]