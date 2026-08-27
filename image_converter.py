from pathlib import Path
from PIL import Image

class ImageConverter:
    def __init__(self):
        self.converted = 0
        self.failed = 0
        self.dir_path = None
        self.delete_originals = False

#getters and setters 
    def set_path(self, folder_path: str):
        self.dir_path = Path(folder_path).expanduser().resolve()       

    def set_deletion(self, delete_files: bool):
        self.delete_originals = delete_files
        print(f"Files will be deleted: {self.delete_originals}")
    def get_deletion_state(self) -> bool:
        return self.delete_originals

#test path
    def test_path(self):
        if self.dir_path is None:
            print(f'Directory is currently set')
            return False
        elif not self.dir_path.exists():
            raise FileNotFoundError(f'Folder does not exist: {self.dir_path}')
        elif not self.dir_path.is_dir():
            raise NotADirectoryError(f'Path is not a folder: {self.dir_path}')
        return True

#delete file function
    def unlink_file(self, file_path: Path):
        try:
            if file_path.exists():
                file_path.unlink()
                print(f"Deleted: {file_path.name}")
                return True
            else:
                print(f"File not Found: {file_path.name}")
                return False
        except Exception as error:
                print(f"Could not delete {file_path.name}: {error}")
                return False

#conversion function
    def convert_images(self, on_message=None):
        if not self.test_path():
            return

        files = self.dir_path.iterdir()
        webp_files = []

        for file in files:
            if file.is_file() and file.suffix.lower() == ".webp":
                webp_files.append(file)

        if not webp_files:
            if on_message:
                on_message('No Webp Files found')
            print("No webp files found.")
            return
            
        self.converted = 0
        self.failed = 0

        for webp_file in webp_files:
            png_file = webp_file.with_suffix(".png")

            try:
                with Image.open(webp_file) as image:
                    if image.mode in ("RGBA", "LA") or "transparency" in image.info:
                        image = image.convert("RGBA")
                    else:
                        image = image.convert("RGB")

                    image.save(png_file, "PNG")
                self.converted += 1
                print(f"Converted: {webp_file.name} -> {png_file.name}")
                if on_message:
                    on_message(f"Converted: {webp_file.name} -> {png_file.name}")
                if png_file.exists() and self.delete_originals:
                    self.unlink_file(webp_file)
            except Exception as error:
                    self.failed += 1
                    if on_message:
                        on_message(f"Failed: {webp_file.name}: {error}")
                    print(f"Failed: {webp_file.name}: {error}")

            print(f"\nFinished. Converted:{self.converted}, Failed:{self.failed}")
            if on_message:
                on_message(f"\nFinished. Converted:{self.converted}, Failed:{self.failed}")

#function to convert a single image
    def reset_converted(self):
        self.converted = 0
    def reset_failed(self):
        self.failed
    def get_webp_files(self, message):
        if not self.test_path():
            return
        
        files = self.dir_path.iterdir()
        webp_files = []
        
        for file in files:
            if file.is_file() and file.suffix.lower() == ".webp":
                webp_files.append(file)
        
        if not webp_files:
            if message:
                message('No Webp Files found')
            print("No webp files found.")
            return
        return webp_files
    def convert_image(self, file_to_convert, message=None):
        if not self.test_path():
            return
        png_file = file_to_convert.with_suffix(".png")
        try:
            with Image.open(file_to_convert) as image:
                if image.mode in ("RGBA", "LA") or "transparency" in image.info:
                    image = image.convert("RGBA")
                else:
                    image = image.convert("RGB")
                
                image.save(png_file, "PNG")
                self.converted += 1
                print(f"Converted: {file_to_convert.name} -> {png_file.name}")
                if message:
                    message(f"Converted: {file_to_convert.name} -> {png_file.name}")
                if png_file.exists() and self.delete_originals:
                    self.unlink_file(file_to_convert)
        except Exception as error:
            self.failed += 1
            if message:
                message(f"Failed: {file_to_convert.name}: {error}")
            print(f"Failed: {file_to_convert.name}: {error}")



if __name__ == "__main__":
    folder_to_convert = input("Enter the folder path: ").strip().strip('"')
    converter = ImageConverter()
    converter.set_path(folder_to_convert)
    print("Would you to delete the original files? Yes = 1 NO = 0")
    if input() == "1":
        converter.set_deletion(True)
    converter.convert_images()