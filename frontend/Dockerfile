# Use Node.js as a parent image
FROM node:14

# Set environment variables
ENV NODE_ENV production

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install --production

# Copy project files
COPY . .

# Build the app
RUN npm run build

# Install a server to serve the build folder
RUN npm install -g serve

# Run the server
CMD ["serve", "-s", "build", "-l", "3000"]
