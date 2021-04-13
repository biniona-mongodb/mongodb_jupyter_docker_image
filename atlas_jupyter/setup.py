from setuptools import setup

setup(name='atlas_jupyter',
      version='0.1',
      description='package for atlas jupyter project',
      url='https://github.com/biniona-mongodb/mongodb_jupyter_docker_image/atlas_jupyter',
      author='Atlas Jupyter Skunks',
      author_email='alek.binion@mongodb.com',
      license='MIT',
      install_requires=[
      'pymongo',
      'dnspython'
      ],
      packages=['atlas_jupyter'],
      zip_safe=False)