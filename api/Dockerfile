FROM python:3.8.0


WORKDIR /flask

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD python -u crawl.py && flask run --host=0.0.0.0 --debug