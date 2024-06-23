from PIL import Image
import os
import datetime

def extract_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            metadata = {
                "file_name": os.path.basename(image_path),
                "file_path": os.path.abspath(image_path),
                "format": img.format,
                "mode": img.mode,
                "size": img.size,
                "exif": img.info.get("exif"),
                "creation_date": datetime.datetime.fromtimestamp(os.path.getctime(image_path)),
                "last_modified_date": datetime.datetime.fromtimestamp(os.path.getmtime(image_path))
            }

            return metadata
    except Exception as e:
        print("An error occurred:", e)
        return None


def image (image_path):
    metadata = extract_image_metadata(image_path)
    if metadata:
        print("Image Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print("Failed to extract metadata.")
