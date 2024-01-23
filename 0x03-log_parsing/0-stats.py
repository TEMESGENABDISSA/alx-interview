#!/usr/bin/python3
import sys
import signal

def print_statistics(total_size, status_codes):
    print("Total file size: File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, status_codes):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            if status_code not in status_codes:
                status_codes[status_code] = 1
            else:
                status_codes[status_code] += 1

        return file_size

    except (IndexError, ValueError):
        return 0

def main():
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            file_size = parse_line(line.strip(), status_codes)
            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()

