from typing import List

def contains_duplicate(words: List[str]) -> bool:
    k = words
    myk_set = set(k)
    myk_list = list(myk_set)
    

    if len(words) > len(myk_list):
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
