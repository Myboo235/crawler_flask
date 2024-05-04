FROM python:3.10.12


WORKDIR /gradio

COPY ./gradio/requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY ./gradio/ .

EXPOSE 7860

CMD gradio app.py