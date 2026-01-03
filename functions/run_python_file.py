import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target = os.path.commonpath([working_dir_abs, target]) == working_dir_abs

        if not valid_target:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path[-3:] == ".py":
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target]

        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=working_directory
        )

        output = ""
        if result.returncode != 0:
            output += "Process exited with code X"

        if not result.stdout and not result.stderr:
            output += "No output produced"

        if result.stdout:
            output += "STDOUT:" + result.stdout
        if result.stderr:
            output += "STDERR:" + result.stderr

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"