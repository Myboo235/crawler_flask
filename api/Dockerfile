FROM python:3.10.12


WORKDIR /flask

COPY ./flask/requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY ./api/ .

EXPOSE 5000

CMD cd app && flask run --host=0.0.0.0 --debug