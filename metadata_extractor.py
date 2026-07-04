"""
=========================================================
Project Title : Metadata Extractor (EXIF)
Author        : avinash mandal
Internship    : Cyber Security Internship
Language      : Python 3.x

Description
-----------
This application extracts EXIF metadata from image files.

Features
--------
1. Reads image metadata.
2. Displays camera information.
3. Displays capture date.
4. Displays GPS information (if available).
5. Handles images without EXIF metadata.

=========================================================
"""

from PIL import Image
from PIL.ExifTags import TAGS


def extract_metadata(image_path):
    """
    Extract EXIF metadata from an image.
    """

    try:

        image = Image.open(image_path)

        exif_data = image.getexif()

        if not exif_data:
            print("\nNo EXIF metadata found.")
            return

        print("\n========== IMAGE METADATA ==========\n")

        for tag_id, value in exif_data.items():

            tag = TAGS.get(tag_id, tag_id)

            print(f"{tag:25}: {value}")

    except FileNotFoundError:
        print("\nImage file not found.")

    except Exception as e:
        print("\nError:", e)


def main():

    print("=" * 45)
    print("      IMAGE METADATA EXTRACTOR")
    print("=" * 45)

    image_path = input("Enter image path: ")

    extract_metadata(image_path)


if __name__ == "__main__":
    main()