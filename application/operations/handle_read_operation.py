from infrastructure.file_system import read_from_json

def handle_read_operation(file_path):
    data = read_from_json(file_path)

    return data

