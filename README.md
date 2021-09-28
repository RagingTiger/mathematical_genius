# TL;DR
**Quickstart On Mac with Docker:**
```
# assumes your current working directory is mathematical_genius
docker run -d \
           --rm \
           --name jupyter-math-genius \
           -e JUPYTER_ENABLE_LAB=yes \
           -p 8888:8888 \
           -v $PWD:/home/jovyan/work \
           jupyter/scipy-notebook:lab-3.1.12 && \
sleep 5 && \
docker logs jupyter-math-genius 2>&1 | grep "http://127.0.0.1" | \
  tail -n 1 | awk '{print $2}'
```

# Usage
Below we will discuss running the `JupyterLab` server.

## Docker
`Docker` will be the primary way discussed for running the `JupyterLab` server.
Please see the [Docker documentation](https://docs.docker.com/get-started/overview/)
for more info about `Docker`.

### Remove
To remove the server simply stop it
```
$ docker stop jupyter-math-genius
```

### :)
```
head -n 15 README.md
```
