#!/usr/bin/env python3
""" a type-annotated function concat """


def concat(str1: str, str2: str) -> str:
    """returns str1 + str2 strings"""
    return "{}{}".format(str1, str2)
    