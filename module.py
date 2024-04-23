import json
# Define the filename for the JSON data file
json_path = "C:\skill rank\ex5.json\ex5.json"
# Load the JSON data from the file
with open(json_path, "r") as json_file:
    JsonFile = json.load(json_file)
# Find the specific donut with name "Old Fashioned"
for donut in JsonFile :
    if donut["name"] == "Old Fashioned" and donut["type"] == "donut":
        # Add a new batter to the specified donut
        data = {"id": "1005", "type": "Tea"}  # Use a new id for the batter
        donut["batters"]["batter"].append(data)
        break  # Stop looping once we"ve updated the donut

# Write the updated JSON data back to the file
with open(json_path, "w") as json_file:
    json.dump(JsonFile, json_file, indent=4)

print(f'Updated {json_path} .')
print(json.dumps(data, indent=4))