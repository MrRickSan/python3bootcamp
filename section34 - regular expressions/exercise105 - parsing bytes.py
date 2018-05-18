import re


def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results
