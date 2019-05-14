# vindicating-vixens

## About
Vindicating Vixens is a small single-page application created for a class to summarize content from a book we throughout the semester. It uses Vue for the front-end, and Flask for the back-end. Data is served from an SQLite database. Docker-based containerization is included for easy deployment. Requires Nginx, Docker, and Python3.

## Development
```
# only do this once
# (pwd: vindicating-vixens/server)

python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt

# needed for every re-run of backend server
# (pwd: vindicating-vixens)

source ./run-backend.sh
```

## Production
```
# build the front end
# (pwd: vindicating-vixens)
docker build . -t vindicating-vixens
docker run -d -p 8080:80 vindicating-vixens

#build the back end
# (pwd: vindicating-vixens/server)
docker build . -t vindicating-api
docker run -d -p 5000:5000 vindicating-api

# site is hosted at <ip address of machine>:8080
```
