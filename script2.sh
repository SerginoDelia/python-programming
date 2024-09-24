# brew install --cask docker

open -a Docker; sleep 2; docker run -d -p 80:80 serge716/lizzo:v2; open -n http://localhost:80
