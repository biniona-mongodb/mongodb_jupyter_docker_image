FROM nikolaik/python-nodejs:python3.8-nodejs15
WORKDIR /app
# install large pip dependencies individually to better cache build
#matplotlib install
RUN pip install Pillow
RUN pip install matplotlib  
RUN pip install numpy
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install seaborn
RUN pip install watermark
RUN pip install tqdm
RUN pip install joblib
RUN pip install tpot
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY atlas_jupyter /atlas_jupyter
RUN pip3 install -e /atlas_jupyter
RUN jupyter labextension install verdant-history
# this installs the mongoDB-esque theme for the notebooks
COPY theme-mongodb /theme-mongodb
RUN jupyter labextension install /theme-mongodb
RUN mkdir -p "/usr/local/share/jupyter/lab/settings"
# this makes the theme load as defualt
COPY overrides.json /usr/local/share/jupyter/lab/settings/overrides.json
RUN mkdir -p "/root/.jupyter/"
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
COPY images images
# delete everything that doesn't have a file extension that contains py in current directory
RUN find . -maxdepth 1 -type f ! -name '*.*py*' -delete
EXPOSE 8888
#extremely insecure, only for proof of concept
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
