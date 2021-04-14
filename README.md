# Atlas + Jupyter Skunkworks POC

Pawel and Alek's skunkworks project.

![atlas jupyter silly logo](https://github.com/biniona-mongodb/mongodb_jupyter_docker_image/blob/master/logo/atlas_jupyter_cc0_background.png)

This is part of a project trying to serve preconfigured Jupyter notebooks on Atlas.

To use this repository, set the `$MY_CONNECTION_URI`, `$MY_DB`, and `$MY_COL`
environment variables, download Docker, and set up an Atlas cluster. If you use
the `direnv` tool, run `direnv allow` in this repository to set the `$MY_DB` and
`$MY_COL` environment variables to point to the sample dataset. 

Set the `$MY_CONNECTION_URI` environment variable to your connection. If you
include a database in your connection URI, the `mongorestore` command written
below will not work, so remove it if present.

Navigate into your clone of this repository and run the following commands.

The following command will create or rebuild the `skunkworks_demo` database in
your atlas cluster.

`mongorestore --drop --uri $MY_CONNECTION_URI$MY_DB`

To build the docker image, run the following command in the root directory of
this repository:

`docker build --tag jupyter_skunk .`

To start run a docker container from the `jupyter_skunk` image, run the
following command. This will map the `8888` port from the container to the
`8888` port on the host machine, and pass in the your MongoDB connection
information as environment variables:

`docker run --env CONNECTION_URI=$MY_CONNECTION_URI --env DATABASE=$MY_DB --env
COLLECTION=$MY_COL  --publish 8888:8888 jupyter_skunk`

If the container spins up, navigate to [the demo notebook](http://localhost:8888/lab/tree/demo.ipynb) (the link will not work
unless container is running), and run the first cell to have a notebook with a
connection to your cluster. 

# This is super insecure. This is a proof of concept, not production code!
