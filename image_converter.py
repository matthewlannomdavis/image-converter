from pathlib import Path
from PIL import Image


def convert_webp_to_png(folder_path: str, include_subfolders: bool = False, deletion: bool = False) -> None:
    folder = Path(folder_path).expanduser().resolve()
    if not folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder}")
    
    if not folder.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {folder}")
    
    if include_subfolders:
        files = folder.rglob("*")
    else:
        files = folder.iterdir()
    
    webp_files = []

    for file in files:
        if file.is_file() and file.suffix.lower() == ".webp":
            webp_files.append(file)

    if not webp_files:
        print("No webp files found.")
        return
    
    converted = 0
    failed = 0

    for webp_file in webp_files:
        png_file = webp_file.with_suffix(".png")

        try:
            with Image.open(webp_file) as image:
                if image.mode in ("RGBA", "LA") or "transparency" in image.info:
                    image = image.convert("RGBA")
                else:
                    image = image.convert("RGB")

                image.save(png_file, "PNG")
                if png_file.exists() and deletion:
                    delete_file(webp_file)

            converted += 1
            print(f"Converted: {webp_file.name} -> {png_file.name}")
        except Exception as error:
            failed += 1
            print(f"Failed: {webp_file.name}: {error}")

    print(f"\nFinished. Converted:{converted}, Failed:{failed}")

def delete_file(file_path: Path) -> bool:
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

if __name__ == "__main__":
    folder_to_convert = input("Enter the folder path: ").strip().strip('"')

    print("Would you to delete the original files? Yes = 1 NO = 0")
    if input() == "1":
        convert_webp_to_png(folder_to_convert, include_subfolders=False, deletion=True)
    else:
        convert_webp_to_png(folder_to_convert, include_subfolders=False, deletion=False)