FROM mhart/alpine-node:16.4.2

# install dependencies
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --immutable --immutable-cache --check-cache

# Copy all local files into the image.
COPY . .

RUN yarn build

###
# Only copy over the Node pieces we need
# ~> Saves 35MB
###
FROM mhart/alpine-node:slim-16.4.2

WORKDIR /app
COPY --from=0 /app .
COPY . .

EXPOSE 3000
CMD ["node", "./build"]