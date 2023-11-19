#Stage 1
FROM node:21-alpine3.17 as builder
WORKDIR /app
COPY package.json .
COPY yarn.lock .
RUN yarn install
COPY . .

# ONLY FOR DEVELOPMENT!!! CHANGE FOR PRODUCTION
RUN yarn force_build 
# ONLY FOR DEVELOPMENT!!! CHANGE FOR PRODUCTION

FROM nginx:1.19.0-alpine
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/dist .
COPY nginx.conf /etc/nginx/conf.d/default.conf
ENTRYPOINT ["nginx", "-g", "daemon off;"]
