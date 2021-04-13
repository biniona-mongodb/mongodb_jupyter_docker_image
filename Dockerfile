FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY atlas_jupyter atlas_jupyter
RUN pip3 install -e atlas_jupyter/ 
COPY . .
# delete everything that doesn't have a .py file extension
RUN find . -type f ! -name '*.*py*' -delete
EXPOSE 8888
#extremely insecure, only for proof of concept 
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
