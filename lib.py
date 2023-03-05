import os


def get_files_with_extension(dirPath: str, extension: str, full_path: bool = False) -> list[str]:
    files = []
    for file in os.listdir(dirPath):
        if file.endswith(extension):
            files.append(dirPath+"\\"+file if full_path else file)
    return files


def remove_parts(arr: list[str], part_to_remove: str) -> list[str]:
    return [item.removesuffix(part_to_remove) for item in arr]
