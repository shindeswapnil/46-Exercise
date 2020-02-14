#The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively.
#But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? 
#Write a function max_in_list() that takes a list of numbers and returns the largest one.

def max_in_list(l):
  big=0
  for n in l:
    if n>big:
      big=n
  return big

print(max_in_list([1,3,4,5,6,7,9,10]))
print(max_in_list([46,2,3,4]))
print(max_in_list([5,2,3,4,99]))






