N = int(input())

def fibo(N):
  if N == 0:
    return 0
  
  if N == 1:
    return 1
  
  return fibo(N-1) + fibo(N-2)


# result = fibo(N)
# print(f"result {result}")


N = int(input())

def fibo_v2(N):
  a, b = 0, 1
  while N > 0:
    a, b = b, a + b
    N -= 1
    
  return a

print(fibo_v2(N))