docker build -t flaskapp .
docker stop flaskapp
docker rm flaskapp
docker run -p 80:80 -d --name flaskapp --link some-mysql:some-mysql acobley/flaskapp