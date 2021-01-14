import json

# Pulls the contents of a json file and returns it 
# as a python dictionary object
def read_from_json_file( filename ):
    with open(filename) as json_file:
        data = json.load(json_file)
    
    return data

# Converts a python dictionary object to json and
# writes it to a json file
def write_to_json_file( filename, data ):
    with open( filename, 'w' ) as outfile:
        json.dump( data, outfile )

