# Atlas + Jupyter Skunkworks

This is part of a project trying to serve preconfigured Jupyter notebooks on Atlas.

Navigate into your clone of this repository and run:

`docker build --tag jupyter_skunk .`

To use this repository, set the `$MY_CONNECTION_URI`, `$MY_DB`, and `$MY_COL`
environment variables, download Docker, and run:

`docker run --env CONNECTION_URI=$MY_CONNECTION_URI --env DATABASE=$MY_DB --env
COLLECTION=$MY_COL  --publish 8888:8888 jupyter_skunk`

If the container spins up, navigate to [the load db
file](http://localhost:8888/lab/tree/load_db.ipynb) (the link will not work
unless container is running), and run the first cell to have a notebook with a
connection to your cluster. 
