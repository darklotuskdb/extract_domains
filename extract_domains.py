#!/usr/bin/env python3

import argparse
import tldextract

def extract_root_domains(lines):
    domains = set()
    for line in lines:
        line = line.strip()
        if line:
            ext = tldextract.extract(line)
            if ext.domain and ext.suffix:
                root_domain = f"{ext.domain}.{ext.suffix}"
                domains.add(root_domain)
    return domains

def main():
    parser = argparse.ArgumentParser(description="Extract root domains from a file.")
    parser.add_argument('-f', '--file', required=True, help='Input file name')
    parser.add_argument('-o', '--output', required=True, help='Output file name')
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
        return

    root_domains = extract_root_domains(lines)

    with open(args.output, 'w') as outfile:
        for domain in sorted(root_domains):
            outfile.write(domain + '\n')

    print(f"Extracted {len(root_domains)} root domain(s) and saved to '{args.output}'.")

if __name__ == '__main__':
    main()

