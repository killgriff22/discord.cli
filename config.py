def token():
  import os
  return os.environ['TOKEN']
class config:
  class settings:
    devmode = True
  TOKEN = token()