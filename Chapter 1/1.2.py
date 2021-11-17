from collections import Counter
def check_permutation(str1,str2):
  if len(str1) != len(str2):
    return False
return Counter(str1) == Counter(str2)
