# Build
docker build -t apache-redirect .

# Run
docker run -d -p 80:80 apache-redirect

# Test

ab -n 1000 -c 10 -r http://localhost/