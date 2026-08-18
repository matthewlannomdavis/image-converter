from image_converter import ImageConverter
from tkinter import filedialog as fd

class ConverterController:
    def __init__(self, gui):
        self.converter = ImageConverter()
        self.selected_folder = None
        self.gui = gui
    #search and select directory
    def find_directory(self):
        folder =  fd.askdirectory()

        if folder:
            print(f'Selected folder: {folder}')
            self.converter.set_path(folder)
            self.gui.set_directory_to_convert(folder)

    def run_conversion(self):
        self.converter.convert_images(on_message=self.file_converted)

    def file_converted(self, message):
        self.gui.add_message(message)
    def set_delete(self):
        if self.converter.get_deletion_state():
            self.converter.set_deletion(False)
        else:
            self.converter.set_deletion(True)
