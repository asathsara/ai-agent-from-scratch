import os

from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: File {file_path} is not a file within {working_directory}"
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a file"

    file_content_str = ""
    try:
        with open(abs_file_path, "r") as f:
            file_content_str = f.read(MAX_CHARS)
            if len(file_content_str) < MAX_CHARS:
                file_content_str += (
                    f'[...File "{file_path}" truncated to {MAX_CHARS} characters]'
            )
            return file_content_str
    except Exception as e:
        return f"Error reading file {file_path}: {e}"
    
    