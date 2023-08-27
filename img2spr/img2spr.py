import argparse
import os
import json5


class Img2spr:
    """Convert image to sprite"""
    settings: dict
    sprite: dict

    def set_settings(self, settings: dict):
        """Set settings"""
        new_settings = settings
        sprite_folder = new_settings.get("sprite_folder_destination")
        self.sprite = {}
        if(isinstance(sprite_folder, str)):
            folder_name = sprite_folder.replace("\\", "/").split("/")[-1]
            png_files = [file for file in os.listdir(sprite_folder) if file.endswith('.png')]
            settings_file_path = f"{sprite_folder}/{folder_name}.yy"
            with open(settings_file_path, 'r', encoding='utf8') as file:
                settings_data = json5.load(file)
            new_sprite = {
                "folder_name": folder_name,
                "png_files": png_files,
                "settings": settings_data
            }
            self.sprite = new_sprite
    



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="App Description")
    
    subparsers = parser.add_subparsers(dest="command")
    
    run_parser = subparsers.add_parser("convert", help="Run conversion")
    run_parser.add_argument("--image", "-i", required=True, help="Image folder source path")
    run_parser.add_argument("--sprite", "-s", required=True, help="Sprite folder destination path")

    args = parser.parse_args()

    img2spr = Img2spr()

    if args.command == "convert":
        img2spr.set_settings({
            "image_folder_source": args.image_folder_source,
            "sprite_folder_destination": args.sprite_folder_destination,
        })
        # Your logic for the 'run' command here
        print(f"settings: {img2spr.sprite}")
    else:
        parser.print_help()
