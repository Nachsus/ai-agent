import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        items_with_info = {}
        items = [i for i in os.listdir(target_dir)]
        for item in items:
            items_with_info[item] = {}
            items_with_info[item]['file_size'] = os.path.getsize(os.path.join(target_dir, item))
            items_with_info[item]['is_dir'] = not os.path.isfile(os.path.join(target_dir, item))

        info_str = ""
        for file_name in items_with_info:
            info_str += "- " + file_name + ":" + " "
            info_str += "file_size=" + str(items_with_info[file_name]['file_size']) + ","
            info_str += "is_dir=" + str(items_with_info[file_name]['is_dir']) + "\n"

        return info_str

    except Exception as e:
        return f"Error: {e}"