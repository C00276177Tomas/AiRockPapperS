from PIL import Image
import os

output_dir = "MyDataset"

for filename in os.listdir(output_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(output_dir, filename)

        try:
            with Image.open(path) as img:
                # Rotate 90 degrees clockwise to fix orientation
                rotated = img.rotate(-90, expand=True)
                rotated.save(path, quality=80, optimize=True)
                print(f"Rotated: {filename}")

        except Exception as e:
            print(f"Failed to rotate {filename}: {e}")
