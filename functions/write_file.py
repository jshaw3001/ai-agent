import os
from google.genai import types

def write_file(working_directory, file_path, content):

    wrk_abs = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file.startswith(wrk_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        try:
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(target_file) and os.path.isdir(target_file):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a specific file in the working directory or create a new file in potentially new directories in the working directory, using the file path and content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath of the file within the working directory that you want to write to or the filepath of a new file to be created to write to. Must be specified.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content you wish to write to the current or new file",
            ),
        },
    ),
)