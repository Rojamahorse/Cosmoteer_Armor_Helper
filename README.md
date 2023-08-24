
# Cosmoteer Armor Helper

## Overview
The Cosmoteer Armor Helper streamlines the creation of armor for the game Cosmoteer. It uses base shape images, applies different textures, and produces armor, roof, and normals images. It also generates icons and blueprints.

## Features
- **Texture Mapping:** Applies different textures to base shapes.
- **Auto Cropping:** Matches applied skin to base shape dimensions.
- **Alpha Thresholding:** Uses the alpha channel for improved texture application.
- **Dynamic Blueprint Creation:** Adjusts blueprints' contrast based on armor image brightness.

## Prerequisites
- Python 3.x
- PIL (Pillow): Install using `pip install Pillow`

## Quick Start
1. Clone this repository.
2. Add base shape images in `shapes/`. (Kroom's Armor Mod shapes included)
3. Add textures: `armor_skin.png`, `roof_skin.png`, `normals_skin.png`.
4. Run a script, e.g., `python apply_all.py`.

## Usage
1. Add shape files (.png, .jpg, .jpeg) to `shapes/`. (Includes Kroom's Armor & Armor Expanded Mod shapes)
2. Add skin files to the root directory.
3. Run the script. Skinned shapes will be in `output/`.

## Customization
Adjust the `alpha_threshold` in `apply_skin()` to change alpha transparency. Default is 100.

## Scripts
- **apply_blueprint.py:** Creates a blueprint based on the provided image path.
  ```bash
  python apply_blueprint.py
  ```
- **apply_all.py:** Applies all skins, creates icons and blueprints.
  ```bash
  python apply_all.py
  ```
- **apply_skin.py:** Applies armor, roof, and normals textures.
  ```bash
  python apply_skin.py
  ```
- **create_icon.py:** Generates an icon from the armor file.
  ```bash
  python create_icon.py
  ```

## Included Skins and Shapes
Repository includes sample textures and Kroom's Armor Mod shapes.

## Contributing
Welcome contributions via pull requests. For major changes, open an issue first.

## License
MIT
