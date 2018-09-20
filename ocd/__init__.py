from ocd import client

__version__ = '0.9.0'

instance = None

def query(*args):
  return ocd_global().query(*args)

def get(*args):
  return ocd_global().get(*args)

def ocd(*args):
  return client.Client(*args)

def ocd_global(*args):
  global instance
  if instance is None:
    instance = ocd(*args)
  return instance
  
