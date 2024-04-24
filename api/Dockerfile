FROM python:3.8.0


WORKDIR /flask

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./api/ .

EXPOSE 5000

CMD cd app && flask run --host=0.0.0.0 --debug