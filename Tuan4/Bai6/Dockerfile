# ===== Stage 1: Build =====
FROM node:18 AS builder

WORKDIR /app

# Copy package trước
COPY package*.json ./

RUN npm install

# Copy source code
COPY . .


# ===== Stage 2: Run =====
FROM node:18-alpine

WORKDIR /app

# Chỉ copy những gì cần từ stage 1
COPY --from=builder /app /app

# Mở cổng
EXPOSE 3000

# Chạy app
CMD ["npm", "start"]