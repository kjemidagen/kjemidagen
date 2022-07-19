FROM node:18 as builder

WORKDIR /app

COPY package.json package-lock.json ./
# At least one of these is needed to generate types
COPY svelte.config.js vite.config.js ./
RUN npm i

# Copy all the silly config files because i cant be bothered to bind mount
COPY postcss.config.cjs tsconfig.json tailwind.config.cjs .env ./