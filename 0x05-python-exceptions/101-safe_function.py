#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None

# Example usage:
def example_function(x, y):
    return x / y

result = safe_function(example_function, 10, 2)
print(f"Result: {result}")

