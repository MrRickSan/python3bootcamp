import re


def parse_name(input):
    # ?P<first> is a label to easy get a group
    name_regex = re.compile(
        r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input)
    print(matches.group())
    print(matches.group('first'))
    print(matches.group('last'))


parse_name("Mrs. Tilda Swinton")
