import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):

    wrk_abs = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file.startswith(wrk_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_file, "r") as f:
            file_content = f.read(MAX_CHARS)
            if len(file_content) == MAX_CHARS:
                file_content += f"[...File {file_path} truncated at {MAX_CHARS} characters]"
        return file_content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read contents of a specific file within the working directory, using the file path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath of the file within the working directory that you want to read the contents of. Must be specified.",
            ),
        },
    ),
)
    