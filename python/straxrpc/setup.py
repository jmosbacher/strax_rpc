from setuptools import setup

setup(name='straxrpc',
      version='0.1alpha',
      description='An RPC service for strax',
      url='http://github.com/jmosbacher/straxrpc',
      author='Yossi Mosbacher',
      author_email='joe.mosbacher@gmail.com',
      license='MIT',
      packages=['straxrpc'],
      install_requires=[
          'grpcio',
          'numpy',
          'pandas',
        #   'fnmatch',
      ],
      zip_safe=False)