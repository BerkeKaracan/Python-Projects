import os
from PIL import Image
target = input("Enter the file path : ").strip('"')
goal = os.path.join(target, "converted_wb")
if not os.path.exists(goal):
    os.makedirs(goal)
files = os.listdir(target)
print(f"Scanning files in: {target}...\n")
for image in files:
    if image.lower().endswith((".jpg", ".jpeg", ".png")) :
        try:
            name, extension = os.path.splitext(image)
            last_name = f"{name}.{'webp'}"
            input_path = os.path.join(target, image)
            output_path = os.path.join(goal, last_name)
            with Image.open(input_path) as path:
                path.save(output_path, quality=80)
                print(f"Converted: {image}")
        except Exception as e:
            print(f"❌ Error converting {image}: {e}")

print("\nProcess Completed.")