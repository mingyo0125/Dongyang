from typing import Union
from Utils import Prints

# set, tuple, int, str
# Union 타입이 달라도 가능
lst: list[Union[int, str]] = [{"aa", "bb"}, (5, 50, 500), 1, 2, 3, "3.14", "str"]

print(lst)
