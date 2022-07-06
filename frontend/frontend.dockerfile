FROM node:18 as builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

# Copy all the silly config files because i cant be bothered to bind mount
COPY *.js *.json *.cjs .env ./