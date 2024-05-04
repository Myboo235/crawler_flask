FROM ollama/ollama

WORKDIR /ollama

COPY ./ollama/run.sh .

RUN chmod +x run.sh \
&& ./run.sh

EXPOSE 11434
