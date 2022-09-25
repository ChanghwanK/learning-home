nums = [1,2,3,2,5]

def two_pointer():
  target = 5
  combinations = []
  end = 0
  result = 0 # 누적합
  cnt = 0
  
  for start in range(len(nums)):
    while end < len(nums) and result < target:
      result += nums[end]
      end+=1
      
    if result == target:
      cnt+=1
    
    result -= nums[start]

  print(f"cnt: {cnt}")
  
two_pointer()


def leet_code_two_pointer(nums, target):
  start, end = 0, len(nums) - 1
  while not start == end:
    if nums[start] + nums[end] < target:
      start += 1
    elif nums[start] + nums[end] > target:
      end -= 1
    else:
      return [start, end]
  