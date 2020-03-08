"""
Given an array of integergs, return a new array such that each element at index i of 
the new aaray is the product of all the numbers except i
"""
def products(nums):
  # List before i
  prefix_products = []
  for num in nums:
    if prefix_products:
      prefix_products.append(prefix_products[-1] * num)
    else:
      prefix_products.append(num)
  
  # list after i
  suffix_products = []
  for num in reversed(nums):
    if suffix_products:
      suffix_products.append(suffix_products[-1] * num)
    else:
      suffix_products.append(num)
    
  suffix_products = list(reversed(suffix_products))

  # product of list before and after i
  result = []
  for i in range(len(nums)):
    if i == 0:
      result.append(suffix_products[i + 1])
    elif i == len(nums) - 1:
      result.append(prefix_products[i-1])
    else:
      result.append(
        prefix_products[i-1] * suffix_products [i+1]
      )
    
  return result

print(products([3,2,1]))