import json

with open('output/output_manually_crop.json', 'r') as f:
    data = json.load(f)

# defend and believe
print("defend v believe: " + str(set(data["defend"] + data["believe"])))

print("think & understand: " + str(set(data["think"]) & set(data["understand"])))

print("believe - understand: " + str(set(data["believe"]) - set(data["understand"])))