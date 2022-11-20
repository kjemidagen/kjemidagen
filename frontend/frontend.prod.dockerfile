FROM node:18

RUN mkdir /app
WORKDIR /app

COPY package.json package-lock.json ./
# At least one of these is needed to generate types
COPY svelte.config.js vite.config.js ./
RUN npm i

COPY ./src /app/src
COPY ./static /app/static

RUN ["npm", "run", "build"]

CMD ["node", "build/index.js"]
