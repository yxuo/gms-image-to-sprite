import argparse
import os
import json5
import shutil

class Img2spr:
    """Convert image to sprite"""
    settings: dict
    sprite: dict
    image_extension: str = ".png"

    def set_settings(self, settings: dict):
        """Set settings"""
        image_folder = settings["new_images_folder_path"]
        sprite_folder = settings["sprite_folder_path"]
        self.sprite = {}
        if(isinstance(sprite_folder, str)):
            sprite_name = sprite_folder.replace("\\", "/").split("/")[-1]
            image_files = sorted([file for file in os.listdir(image_folder) if file.endswith('.png')])
            settings_file_path = f"{sprite_folder}/{sprite_name}.yy"
            with open(settings_file_path, 'r', encoding='utf8') as file:
                settings_data = json5.load(file)
            new_sprite = {
                "sprite_name": sprite_name,
                "new_image_files": image_files,
                "settings": settings_data
            }
            self.sprite = new_sprite
        
        self.settings = settings

    def get_sorted_sprite_frames(self) -> list:
        """Gest sorted list of sprite's frames"""
        items = self.sprite["settings"]["sequence"]["tracks"][0]["keyframes"]["Keyframes"]
        items_map = {
            i["Channels"]["0"]["Id"]["name"]: i["Key"]
            for i in  items
        }
        names = items_map.keys()
        sorted_names = sorted(names, key=lambda name: items_map[name])
        return sorted_names

    def udpate_sprite(self):
        """Update existing sprite and existing frames with new images"""
        sprite_frame_images = self.get_sorted_sprite_frames()
        for i, sprite_frame in enumerate(sprite_frame_images):
            new_image_filepath = os.path.join(
                self.settings["new_images_folder_path"],
                self.sprite["new_image_files"][i],
            )
            layer = self.sprite["settings"]["layers"][0]["name"]
            sprite_frame_path = os.path.join(
                self.settings["sprite_folder_path"],
                sprite_frame + self.image_extension
            )
            sprite_layer_path = os.path.join(
                self.settings["sprite_folder_path"],
                "layers", sprite_frame,
                layer + self.image_extension
            )
            shutil.copy(new_image_filepath, sprite_frame_path)
            shutil.copy(new_image_filepath, sprite_layer_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="App Description")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("update", help="Run conversion")
    run_parser.add_argument("--images", "-i", required=True, help="Image folder source path")
    run_parser.add_argument("--sprite", "-s", required=True, help="Sprite folder destination path")

    args = parser.parse_args()

    img2spr = Img2spr()

    if args.command == "update":
        img2spr.set_settings({
            "new_images_folder_path": args.images,
            "sprite_folder_path": args.sprite,
        })
        img2spr.udpate_sprite()
    else:
        parser.print_help()
