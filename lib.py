import os
import re

def get_files_with_extension(dirPath: str, extension: str, full_path: bool = False) -> list[str]:
    files = []
    for file in os.listdir(dirPath):
        if file.endswith(extension):
            files.append(dirPath+"\\"+file if full_path else file)
    return files


def remove_parts(arr: list[str], part_to_remove: str) -> list[str]:
    return [item.removesuffix(part_to_remove) for item in arr]


def get_extension(file: str) -> tuple[str, str | None]:
    extension_start_index = file.rfind(".") + 1
    if extension_start_index != 0:
        file_name = file[:extension_start_index - 1]
        extension = file[extension_start_index:]
        return (file_name, extension.lower())
    else:
        return (file, None)


def get_srcs(s: str):
    matches = re.findall(r'src=[\'"]?([^\'" >]+)', s, flags=re.IGNORECASE)
    print(matches)


if __name__ == "__main__":
    pass
