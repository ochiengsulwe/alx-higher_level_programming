#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    def extract_value(t, index):
        return t[index] if len(t) > index else 0

    result = (
        extract_value(tuple_a, 0) + extract_value(tuple_b, 0),
        extract_value(tuple_a, 1) + extract_value(tuple_b, 1)
    )
    return result
