FROM nikolaik/python-nodejs:python3.8-nodejs15-alpine
# this solves a problem building wheels for jupyter lab dependencies, this could probably be trimmed down
# https://www.gitmemory.com/issue/zeromq/pyzmq/1510/783219808
RUN apk update \
    && apk add gcc g++ musl-dev python3-dev py3-setuptools libffi libffi-dev openssl-dev git zeromq-dev
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY atlas_jupyter atlas_jupyter
RUN pip3 install -e atlas_jupyter/
RUN jupyter labextension install verdant-history
COPY . .
# delete everything that doesn't have a file extension that contains py
RUN find . -type f ! -name '*.*py*' -delete
EXPOSE 8888
#extremely insecure, only for proof of concept
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
