import argparse
import json

# 1. Returns JSON Data
def get_json(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('json_data', type=str)
    args = parser.parse_args()
    data = json.loads(args.json_data)

    return data

# 2. Convert JSON
def convert_json(data): 
    for key in data.keys: