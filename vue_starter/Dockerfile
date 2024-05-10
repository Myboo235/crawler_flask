# build stage
FROM --platform=linux/amd64 node:lts-alpine

WORKDIR /app

COPY ./vue_starter/package*.json /app

RUN cd /app && npm install --loglevel verbose

COPY ./vue_starter /app

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]