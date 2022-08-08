import requests
  
  
def send_message(msg):
  url='https://hooks.slack.com/services/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'
  data = {'text':msg}
  resp = requests.post(url=url, json=data)
  return resp

send_message('hello world!')
