FROM redis:latest

# Copy config vào container
COPY redis.conf /usr/local/etc/redis/redis.conf

# Chạy redis với config custom
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]