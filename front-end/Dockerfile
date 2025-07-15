# Use official Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY package*.json ./
RUN npm install --legacy-peer-deps

# Copy the rest of the code and build
COPY . .
RUN npm run build

# Prepare production image
FROM node:18

WORKDIR /app

# Copy the standalone build output
COPY --from=0 /app/.next/standalone ./
COPY --from=0 /app/public ./public
COPY --from=0 /app/.next/static ./.next/static
COPY --from=0 /app/node_modules ./node_modules
COPY --from=0 /app/package.json ./package.json

EXPOSE 3000

CMD ["node", "server.js"]
