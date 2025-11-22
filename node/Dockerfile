FROM node:15.1.0-alpine3.10

WORKDIR /usr/local/app

RUN npm install express

COPY . .

EXPOSE 2000

ENTRYPOINT ["node"]

CMD ["server.js"]
