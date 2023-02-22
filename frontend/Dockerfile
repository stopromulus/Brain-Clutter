FROM node:18-alpine AS build

WORKDIR /Brain-Clutter/frontend

# install dependencies
ADD package.json package-lock.json ./
RUN npm ci

# copy remaining files and build
COPY . .
RUN npm run build

FROM node:18-alpine AS deploy

WORKDIR /Brain-Clutter/frontend

RUN rm -rf ./*

# copy over necessary files from build stage
COPY --from=build /Brain-Clutter/frontend/package.json .
COPY --from=build /Brain-Clutter/frontend/package-lock.json .
COPY --from=build /Brain-Clutter/frontend/build .

# install prod dependencies
RUN npm ci --omit=dev

CMD ["node", "index.js"]
