# ===== Stage 1: Build React =====
FROM node:18-alpine AS build

WORKDIR /app

# Copy package trước để cache
COPY package.json package-lock.json ./

RUN npm install

# Copy source code
COPY . .

# Build production
RUN npm run build


# ===== Stage 2: Serve bằng nginx =====
FROM nginx:alpine

# Copy build từ stage 1 sang nginx
COPY --from=build /app/build /usr/share/nginx/html

# Mở cổng 80
EXPOSE 80

# Chạy nginx
CMD ["nginx", "-g", "daemon off;"]