"""
Passing Single arguments with the sys module.
Example:
    py .\mlops_playground\jformat.py .\mlops_playground\examples\example.json
"""
import os
import sys
import json

def formatter(string, sort_keys=True, indent=4):
    #load incoming string into JSON
    loaded_json = json.loads(string)
    #dump as string
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(path):
    with open(path, 'r') as _f:
        print(
            formatter(_f.read())
        )

if __name__ == '__main__':
    main(sys.argv[-1])