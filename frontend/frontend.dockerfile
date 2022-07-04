FROM node:16.15-bullseye as builder

# install dependencies
WORKDIR /app/
COPY package.json ./
RUN yarn install --immutable --immutable-cache --check-cache

# Copy all local files into the image.
COPY . .

RUN yarn build