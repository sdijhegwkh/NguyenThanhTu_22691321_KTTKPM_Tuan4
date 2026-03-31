# Base image
FROM node:18

# Tạo thư mục trong container
WORKDIR /app

# Copy package.json 
COPY package.json .

# Cài dependencies 
RUN npm install

# Copy toàn bộ source code
COPY . .

# Mở cổng 3000
EXPOSE 3000

# Chạy app
CMD ["npm", "start"]