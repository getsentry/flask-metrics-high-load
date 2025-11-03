
# Running the app

```bash
flask --app hello run
```

# Running the app in docker

```bash
docker build . -t flask-metrics
docker run --rm -it -v "$PWD":/app -p 5001:5000 --memory=100m flask-metrics \
  flask --app app/hello run --host=0.0.0.0
```


```bash
seq 1 50000 | xargs -Iname -P100 curl "http://127.0.0.1:5001"
```
