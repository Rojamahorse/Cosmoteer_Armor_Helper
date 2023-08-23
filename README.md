# Texture Mapping for 2D Shapes

This script applies different textures (skins) to a set of 2D shapes stored in PNG or JPEG format. It works recursively through a directory tree to find all shapes and apply the skins to them. The textures are also expected to be in PNG format. The script currently supports applying three types of skins: armor, roof, and normals.

## Prerequisites

- Python 3.x
- PIL (Pillow)
  ```bash
  pip install Pillow
  ```

## Project Structure
```
|-- shapes/             # Folder containing shapes (supports nested folders)
|   |-- example1.png
|   |-- example2.jpg
|   |-- ...
|-- output/             # Folder where the skinned shapes will be saved (auto-created)
|-- armor_skin.png      # Skin for armor
|-- roof_skin.png       # Skin for roof
|-- normals_skin.png    # Skin for normals
|-- script.py           # Main script
|-- README.md           # This file
```

## Usage

1. Place your shape files (.png, .jpg, .jpeg) in the `shapes/` directory. This directory can have nested folders. (Please Note it currently includes shapes based of of Krooms Armor & Armor Expanded Mods)
2. Place your skin files (`armor_skin.png`, `roof_skin.png`, `normals_skin.png`) in the root directory. It will not create roof or normals; you will need to provide these (custom normals are always a better option).
3. Run the script:
   ```bash
   python script.py
   ```
   This will generate skinned shapes and save them in the `output/` directory, preserving the folder structure of the `shapes/` directory.
4. Check the `output/` directory for the skinned shapes.

## Customization

You can customize the alpha transparency threshold by changing the `alpha_threshold` parameter in the `apply_skin()` function. Default value is 100.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
```