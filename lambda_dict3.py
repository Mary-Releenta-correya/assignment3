# List of dictionaries
lst_dicts = [
    {'id': 1, 'name': 'red'},
    {'id': 2, 'name': 'yellow'},
    {'id': 3, 'name': 'orange'},
]

# Specific ID to filter
req_id = 3

# Using filter with lambda function to filter dictionaries
filter_dict = list(filter(lambda x: x['id'] == req_id, lst_dicts))

# Display the result
print("Filtered dictionary:", filter_dict)