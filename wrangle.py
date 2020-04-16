import json

# with open('wrangled-data.txt', 'w') as outfile:
#     json.dump(data, outfile)

with open('dataset.json') as json_file:
    data = json.load(json_file)
    # for i in range(2):
    #     print(data[i])