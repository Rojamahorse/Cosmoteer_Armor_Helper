from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps

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

