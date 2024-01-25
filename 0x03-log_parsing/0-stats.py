#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the
line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything
for this status code
format: <status code>: <number>
status codes should be printed in ascending order"""

import sys


def print_statistics(total_size, status_counts):
    """
    Print the computed statistics.

    Args:
        total_size (int): Total file size.
        status_counts (dict):
        Dictionary containing status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        print("{}: {}".format(status_code, status_counts[status_code]))


def parse_line(line):
    """
    Parse a log line and extract relevant information.

    Args:
        line (str): Log line to parse.

    Returns:
        tuple: A tuple containing IP address, status code, and file size.
               Returns (None, None, None) if parsing fails.
    """
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None


def main():
    """
    Main function to read stdin, compute statistics, and print results.
    """
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            ip_address, status_code, file_size = parse_line(line.strip())
            if (
                ip_address is not None
                and status_code is not None
                and file_size is not None
            ):
                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        pass
    finally:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
