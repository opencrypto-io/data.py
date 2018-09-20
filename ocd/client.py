import requests
import jmespath

class Client:
  opts = {
    'data_url': 'https://data.opencrypto.io/data.json'
  }

  def __init__(self, options={}):
    for key in options:
      print(key)
      self.opts[key] = options[key]
    self.data = None
    self.load()

  def load(self):
    if self.data is None:
      print(f'Downloading from {self.opts["data_url"]}')
      r = requests.get(self.opts["data_url"])
      if r.status_code != 200:
        print('bad status code')
      self.data = r.json()

  def query(self, q):
    return jmespath.search(q, self.data)

  def get(self, model, id, query=None):
    print('get')

