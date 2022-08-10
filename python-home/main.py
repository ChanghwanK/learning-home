def return_none():
  print("hello")
  return None


def check():
  data = return_none()
  
  if data is None:
    print("None")
  else:
    print("머고")
    
  if not data:
    print("None 2")
  else:
    print("머고")
    
check()