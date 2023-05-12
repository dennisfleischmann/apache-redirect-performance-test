# Build
docker build -t apache-redirect .

# Run
docker run -d -p 80:80 apache-redirect
