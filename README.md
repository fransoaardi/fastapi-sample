# fastapi-sample

## introduction

sample repository using `fastapi` and `poetry`. 

## how to run

```bash
# setup python env with local-installed python3
$ poetry env use python3

$ poetry install
$ poetry run start

$ curl localhost:8000/predict
*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /predict HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.78.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Sat, 28 Aug 2021 13:28:16 GMT
< server: uvicorn
< content-length: 17
< content-type: application/json
<
* Connection #0 to host localhost left intact
{"Hello":"World"}%
```