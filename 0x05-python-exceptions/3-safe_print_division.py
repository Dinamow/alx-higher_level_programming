#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = float(a / b)
        try:
            return result
        finally:
            print("Inside result: {:.1f}".format(float(a / b)))
    except ZeroDivisionError:
        try:
            return None
        finally:
            print("Inside result: None")
