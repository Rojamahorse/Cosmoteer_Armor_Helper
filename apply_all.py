from PIL import Image, ImageChops, ImageEnhance, ImageOps
import os
import re
import shutil

def apply_skin(shape_path, skin_path, output_path, alpha_threshold=100):
    print(f"Applying skin from {skin_path} to {shape_path}, saving to {output_path}...")
    
    shape = Image.open(shape_path).convert("RGBA")
    skin = Image.open(skin_path).convert("RGBA")
    
    shape_width, shape_height = shape.size
    skin_width, skin_height = skin.size
    
    extended_skin = Image.new("RGBA", (shape_width, shape_height), (0, 0, 0, 0))
    
    for y in range(0, shape_height, skin_height):
        for x in range(0, shape_width, skin_width):
            extended_skin.paste(skin, (x, y))
    
    skin = extended_skin.crop((0, 0, shape_width, shape_height))
    
    result = Image.new("RGBA", shape.size)
    shape_data = shape.getdata()
    skin_data = skin.getdata()
    result_data = []
    
    for i in range(len(shape_data)):
        shape_pixel = shape_data[i]
        skin_pixel = skin_data[i]
        
        if shape_pixel[3] < alpha_threshold:
            result_data.append((0, 0, 0, 0))
        else:
            result_data.append(skin_pixel)
            
    result.putdata(result_data)
    result.save(output_path)
    print(f"Saved to {output_path}")

def create_blueprint(image_path, output_path, min_blue=200, max_blue=255, contrast_factor=2.0):
    img = Image.open(image_path).convert("RGBA")
    img_data = img.getdata()
    new_data = []

    # Calculate average brightness
    avg_brightness = sum([sum(pixel[:3]) / 3.0 for pixel in img_data]) / len(img_data)

    for item in img_data:
        r, g, b, a = item

        # Calculate brightness of the original pixel
        brightness = (r + g + b) // 3

        # Adjust brightness around the average brightness
        delta_brightness = brightness - avg_brightness
        adjusted_brightness = avg_brightness + (delta_brightness * contrast_factor)

        # Clip values to be in [0, 255]
        adjusted_brightness = min(255, max(0, int(adjusted_brightness)))

        # Scale the blue value based on adjusted brightness
        scaled_blue = int(min_blue + (max_blue - min_blue) * (adjusted_brightness / 255.0))

        new_data.append((0, 0, scaled_blue, a))

    img.putdata(new_data)
    img.save(output_path)

def create_icon_and_blueprint_copies(directory):
    for subdir, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename == "armor.png":
                source = os.path.join(subdir, filename)
                icon_dest = os.path.join(subdir, "icon.png")
                
                shutil.copy2(source, icon_dest)
                
                blueprint_output_path = os.path.join(subdir, "blueprints.png")
                create_blueprint(icon_dest, blueprint_output_path)

# Paths
armor_skin_path = "armor_skin.png"
roof_skin_path = "roof_skin.png"
normals_skin_path = "normals_skin.png"

base_dir = "shapes"
output_base_dir = "output"

if not os.path.exists(output_base_dir):
    os.makedirs(output_base_dir)

for subdir, _, filenames in os.walk(base_dir):
    for filename in filenames:
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Skipping {filename} as it is not a supported image type.")
            continue

        rel_dir = os.path.relpath(subdir, base_dir)
        output_subdir = os.path.join(output_base_dir, rel_dir)
        
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        shape_path = os.path.join(subdir, filename)
        
        file_root, file_extension = os.path.splitext(filename)
        match = re.match(r'armor_(\d+)?', file_root)
        suffix = match.group(1) if match else ""
        underscore = "_" if suffix else ""
        
        armor_output_path = os.path.join(output_subdir, f"armor{underscore}{suffix}{file_extension}")
        roof_output_path = os.path.join(output_subdir, f"roof{underscore}{suffix}{file_extension}")
        normals_output_path = os.path.join(output_subdir, f"roof_normals{underscore}{suffix}{file_extension}")
        
        apply_skin(shape_path, armor_skin_path, armor_output_path)
        apply_skin(shape_path, roof_skin_path, roof_output_path)
        apply_skin(shape_path, normals_skin_path, normals_output_path)

create_icon_and_blueprint_copies(output_base_dir)
