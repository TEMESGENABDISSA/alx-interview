#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>
    (see input format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn’t appear, don’t print anything for this status
        code
        format: <status code>: <number>
        status codes should be printed in ascending order
"""
from sys import stdin


size = 0
code = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}


def print_stats(size: int, codes: dict) -> None:
    """
    Prints stats from logs
    """
    print("File size: {}".format(size))
    for key in sorted(codes.keys()):
        if codes[key] != 0:
            print("{}: {}".format(key, codes[key]))


try:
    for i, log in enumerate(stdin, 1):
        line = log.split(' ')
        if len(line) > 2:
            status = line[-2]
            f_size = int(line[-1])

            size += f_size
            if status in code.keys():
                code[status] += 1
            if i % 10 == 0:
                print_stats(size, code)
finally:
    print_stats(size, code)
