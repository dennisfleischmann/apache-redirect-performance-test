docker build --build-arg NUM_REDIRECTS=100 -t my-apache-image-100 .
docker build --build-arg NUM_REDIRECTS=300000 -t my-apache-image-300000 .
docker build --build-arg NUM_REDIRECTS=550000 -t my-apache-image-550000 .
