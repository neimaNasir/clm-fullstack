# Use official Node.js image
FROM node:18

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install --legacy-peer-deps

# Copy code and build
COPY . .
RUN npm run build

# Expose port and run the standalone server
EXPOSE 3000
CMD ["node", ".next/standalone/server.js"]
