FROM python:3.8.0


WORKDIR /gradio

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./gradio/ .

EXPOSE 7860

CMD python testchat.py