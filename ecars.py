import json

with open('electric_cars.json') as in_file:
    parsed_json = json.load(in_file)

print(parsed_json)
print(parsed_json.keys())
print(parsed_json['meta'].keys())
print(len(parsed_json['data']))
print(parsed_json['data'][3])
