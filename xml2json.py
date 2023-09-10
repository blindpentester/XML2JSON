#!/usr/bin/env python3

import sys
import json
from lxml import etree
import argparse
from collections import defaultdict


def main():

    try:
        parser = argparse.ArgumentParser(description='Convert any XML input to JSON format')
        parser.add_argument('-o', '--output', help="Output file name (default: - for stdout)", default='-')
        args = parser.parse_args()

        if args.output == '-':
            output_file = sys.stdout
        else:
            output_file = open(args.output, 'w')

        context = etree.iterparse(sys.stdin.buffer, events=('end',), tag='*')

        for _, elem in context:
            elem_data = etree_to_dict(elem)
            json_data = json.dumps(elem_data, indent=4)
            output_file.write(json_data)
            output_file.write("\n")
            elem.clear()

        if args.output != '-':
            output_file.close()
            print(f"JSON output saved to {args.output}")

    except KeyboardInterrupt:
        print("\nExecution interrupted by user. Have a nice day!")
        sys.exit(0)
    except Exception as e:
        print(f"Error processing XML file: {e}")
        sys.exit(1)

def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

if __name__ == "__main__":
    main()
