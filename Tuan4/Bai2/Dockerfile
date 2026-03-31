# Base image
FROM python:3.9

# Tạo thư mục làm việc
WORKDIR /app

# Copy file requirements 
COPY requirements.txt .

# Cài thư viện
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code
COPY . .

# Mở cổng 5000
EXPOSE 5000

# Chạy app
CMD ["python", "app.py"]