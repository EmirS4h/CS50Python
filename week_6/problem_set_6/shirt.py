import sys
from PIL import Image
import os


def main():
    args = sys.argv

    if len(args) == 3:
        before, after = args[1:]
        before_name, before_extension = get_extension(before)
        after_name, after_extension = get_extension(after)

        if before_extension != "jpg" and before_extension != "jpeg" and before_extension != "png" or after_extension != "jpg" and after_extension != "jpeg" and after_extension != "png":
            sys.exit(
                f"Extensions should be one of these [jpg, jpeg, png]. Current extensions are '{before_name}.{before_extension.upper()}' and '{after_name}.{after_extension.upper()}'")
        elif before_extension != after_extension:
            sys.exit(
                f"Extensions does not match. Current extensions are '{before_name}.{before_extension.upper()}' and '{after_name}.{after_extension.upper()}'")
        else:
            overlay_image(before, after)
    elif len(args) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def get_extension(file: str) -> tuple[str, str | None]:
    """Given a file name returns a tuple containing (file_name, extension)

    Arguments:
        file -- file name

    Returns:
        a tuple with file_name and extension if exists or None
    """
    extension_start_index = file.rfind(".") + 1
    if extension_start_index != 0:
        file_name = file[:extension_start_index - 1]
        extension = file[extension_start_index:]
        return (file_name, extension.lower())
    else:
        return (file, None)


def overlay_image(img1: str, output_image_name: str):
    try:
        # Open the first image
        photo = Image.open(img1)

        # Open the second image
        img2 = Image.open("shirt.png")

        # Get the size of the second image
        width, height = photo.size

        # Paste the first image onto the second image
        img2.paste(photo, (0, 0))
        img2 = img2.convert("RGB")
        # Save the new image
        img2.save(output_image_name)
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
