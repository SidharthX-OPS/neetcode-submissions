from typing import List

def read_integers() -> List[int]:
    smth = input()

    int_li = [int(x) for x in smth.split(",")]
    return int_li

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())