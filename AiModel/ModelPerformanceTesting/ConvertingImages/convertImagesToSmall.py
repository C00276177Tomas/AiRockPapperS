import os
from PIL import Image

input_dir = "RockPapperS2"
output_dir = "RockPapperS2Converted"
os.makedirs(output_dir, exist_ok=True)

target_size = 640
quality = 95

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.heic')):
        input_path = os.path.join(input_dir, filename)
        output_filename = f"{os.path.splitext(filename)[0]}_resized.jpg"
        output_path = os.path.join(output_dir, output_filename)

        try:
            with Image.open(input_path) as img:
                img = img.convert('RGB')

                # Step 1: resize so smaller side == target_size, keep aspect ratio
                img_ratio = img.width / img.height

                if img.width < img.height:
                    new_width = target_size
                    new_height = int(target_size / img_ratio)
                else:
                    new_height = target_size
                    new_width = int(target_size * img_ratio)

                img = img.resize((new_width, new_height), Image.LANCZOS)

                # Step 2: center-crop to target_size x target_size
                left = (new_width - target_size) // 2
                top = (new_height - target_size) // 2
                right = left + target_size
                bottom = top + target_size

                img = img.crop((left, top, right, bottom))

                # Step 3: save
                img.save(output_path, "JPEG", quality=quality)

                print(f"Processed: {filename} -> {output_filename}")

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

print("All done!")
