from collections import Counter

#Problem 1
def is_unique(string):
    return len(set(string)) == len(string)

#Problem 2
def is_premutation(str1,str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)

#problem 3
def replace(text1,text2):
    return text1[:text2].replace(" ","20%")

#Problem 4
def replaced(s1,s2):
    for c1,c2 in zip(s1,s2):
        if c1 != c2:
            return False
    return True 

def inserted(s1,s2):   
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            return False
        else:
            i += 1
            j += 1
    return True

def oneway(s1, s2):
    if len(s1) == len(s2):
        return replaced(s1, s2)
    elif len(s1) + 1 == len(s2) or len(s1) - 1 ==len(s2):
        return inserted(s1, s2)
    return False


        
if __name__ == '__main__':
    print(is_unique('Shirin'))
    print(is_premutation("ab" , "eidbaooo"))
    print(replace("Ms shirin Yamani",20))
    print(oneway("bake","pale"))



