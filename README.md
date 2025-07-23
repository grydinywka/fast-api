# The Pet project for show FastAPI demonstration!  

How to deploy locally:  
- git clone git@github.com:grydinywka/fast-api.git
- cd fast-api
- mkdir nginx/certs
- openssl req -x509 -nodes -days 365   -newkey rsa:2048   -keyout nginx/certs/localhost.key   -out nginx/certs/localhost.crt   -subj "/CN=localhost"
- docker compose up -d

Check API via swagger - go to https://127.0.0.1:4434/docs
