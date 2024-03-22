import json

def write_list_to_json(a_list: list, path_to_file: str):
    with open(path_to_file, "w") as fp:
        json.dump(a_list, fp)
        

# Read list to memory
def read_list_from_json(path_to_file: str) -> list:
    # for reading also binary mode is important
    with open(path_to_file, 'rb') as fp:
        n_list = json.load(fp)
        return n_list