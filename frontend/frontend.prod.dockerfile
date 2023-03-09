FROM node:18-alpine

RUN mkdir /app
WORKDIR /app

COPY package.json package-lock.json ./
COPY *.config.js *.config.cjs *.config.mjs ./
RUN npm ci

COPY ./src /app/src
COPY ./static /app/static

RUN ["npm", "run", "build"]

CMD ["node", "build"]
