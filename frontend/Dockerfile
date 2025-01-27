FROM node:alpine

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm install -g @angular/cli

RUN npm install

expose 4200

CMD ["ng", "serve", "--host", "0.0.0.0"]

