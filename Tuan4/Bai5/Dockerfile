# ===== Stage 1: Build =====
FROM golang:1.26-alpine AS builder

WORKDIR /app

# Copy source code
COPY . .

# Build binary
RUN go build -o app


# ===== Stage 2: Run =====
FROM alpine:latest

WORKDIR /root/

# Copy binary từ stage build
COPY --from=builder /app/app .

# Mở cổng 8080
EXPOSE 8080

# Chạy app
CMD ["./app"]