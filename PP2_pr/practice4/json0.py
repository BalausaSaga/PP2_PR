import json

# Open the JSON file for reading
with open('sample-data.json', 'r') as file:
    # Load the JSON data into a Python dictionary
    data = json.load(file)

# Print the table headers by the exercise
print("Interface Status")
print("=" * 80)
# Use f-strings with alignment <50 means 50 characters width
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 7 + " " + "-" * 6)

# Iterate through the list of interfaces in 'imdata'
for item in data['imdata']:
    # Navigate through the nested structure: l1PhysIf -> attributes
    attributes = item['l1PhysIf']['attributes']
    
    # Extract specific values using their keys
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    
    # Print the row with the same column widths as the header
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")