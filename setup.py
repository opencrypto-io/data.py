from setuptools import setup, find_packages

setup(
  name='opencrypto-data',
  version='0.9.0',
  author='OpenCrypto.io',
  author_email='dev@opencrypto.io',
  url='https://github.com/opencrypto-io/data.py',
  packages=find_packages(exclude=['tests']),
  install_requires=[
    'requests',
    'jmespath',
  ],
  license='MIT'
)
