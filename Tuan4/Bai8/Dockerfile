FROM postgres:15

# Set biến môi trường cho Postgres
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=123456
ENV POSTGRES_DB=mydb

# Copy file SQL vào thư mục init
COPY init.sql /docker-entrypoint-initdb.d/