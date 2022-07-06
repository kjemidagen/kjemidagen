FROM node:18

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

# Copy all the silly config files because i cant be bothered to bind mount
COPY *.js *.json *.cjs .env ./