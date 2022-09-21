from shopping.more_shopping.shopping_cart import buy

import utils
from utils_2 import *

print(
    f"You can see how utils gets the name changed as long as it doesn't get executed: {utils.__name__}"
)
if __name__ == "__main__":  # this only runs if this is the main file and not a module.
    print(buy("apples"))

    print(divide(5, 2))
    print(multiply(5, 2))
    print(f"please run this {__name__}")
