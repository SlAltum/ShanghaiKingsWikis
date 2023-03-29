docker build -t 'shanghaikingswikis' -f DockerFile .
docker run -it --rm -p 80:80 shanghaikingswikis