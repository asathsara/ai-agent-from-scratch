import os 

def write_file(working_directory: str, file_path: str, content: str):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: File {file_path} is not a file within {working_directory}"

    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"Error creating directory {parent_dir}: {e}"

    try:
        with open(abs_file_path, "a") as f:
            f.write(content)
        return f"File {file_path} written successfully"
    except Exception as e:
        return f"Error writing file {file_path}: {e}"