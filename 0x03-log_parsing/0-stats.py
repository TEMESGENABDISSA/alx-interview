#!/usr/bin/python3
''' script for processing requests logs '''
from sys import stdin
import re


def print_logs(status_codes, total_size):
    ''' prints the logs '''
    print('File size: {}'.format(total_size), flush=True)
    for key, val in sorted(status_codes.items(), key=lambda v: v[0]):
        if val:
            print('{}: {}'.format(key, val), flush=True)


def calc(line, total_size, status_codes):
    ''' calculates metrics '''
    parts = line.strip().split(' ')
    if len(parts) >= 2:
        status_code = parts[-2]
        file_size = parts[-1]
        total_size += int(file_size)
        if status_code in status_codes.keys():
            status_codes[status_code] += 1
    return total_size


def main():
    ''' logs network requests '''
    count = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    try:
        while True:
            line = input()
            total_size = calc(line, total_size, status_codes)
            count += 1
            if count % 10 == 0:
                print_logs(status_codes, total_size)
    except (KeyboardInterrupt, EOFError):
        print_logs(status_codes, total_size)


if __name__ == '__main__':
    main()
