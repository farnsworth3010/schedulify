#Stage 1
FROM node:18.18.0-alpine@sha256:d51f2f5ce2dc7dfcc27fc2aa27a6edc66f6b89825ed4c7249ed0a7298c20a45a as builder
WORKDIR /app
COPY package.json .
COPY yarn.lock .
RUN yarn install
COPY . .

# ONLY FOR DEVELOPMENT!!! CHANGE FOR PRODUCTION
RUN yarn force_build 
# ONLY FOR DEVELOPMENT!!! CHANGE FOR PRODUCTION

FROM nginx:1.19.0-alpine@sha256:2fa12030ffb0224e0b2e17bc4b1f1479e191e2fd65869fc60d09a8efa5b6d879
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/dist .
COPY nginx.conf /etc/nginx/conf.d/default.conf
ENTRYPOINT ["nginx", "-g", "daemon off;"]