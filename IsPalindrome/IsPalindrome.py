import re

def isPalindromeFirst(string: str) -> bool: # best
    return re.sub(r'\W+', '', string).lower() == re.sub(r'\W+', '', string).lower()[::-1]

def isPalindromeSecond(string: str) -> bool:
    return list(re.sub(r'\W+', '', string).lower()) == list(reversed(list(re.sub(r'\W+', '', string).lower())))

def isPalindromeSecondAlt(string: str) -> bool:
    return "".join(list(re.sub(r'\W+', '', string).lower())) == "".join(list(reversed(list(re.sub(r'\W+', '', string).lower()))))

def isPalindromeThird(string: str) -> bool:
    reversed_list = list(re.sub(r'\W+', '', string).lower())
    reversed_list.reverse()
    return list(re.sub(r'\W+', '', string).lower()) == reversed_list

def isPalindromeThirdAlt(string: str) -> bool:
    reversed_list = list(re.sub(r'\W+', '', string).lower())
    reversed_list.reverse()
    return "".join(list(re.sub(r'\W+', '', string).lower())) == "".join(reversed_list)

if __name__ == '__main__':
    print(isPalindromeFirst("Red roses run no risk, sir, on Nurse's order"))
    print(isPalindromeSecond("Red roses run no risk, sir, on Nurse's order"))
    print(isPalindromeSecondAlt("Red roses run no risk, sir, on Nurse's order"))
    print(isPalindromeThird("Red roses run no risk, sir, on Nurse's order"))
    print(isPalindromeThirdAlt("Red roses run no risk, sir, on Nurse's order"))
