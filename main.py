from ConverterController import ConverterController
from Merts_Image_Converter_gui import ConverterGui
import tkinter as tk

if __name__ == "__main__":
    gui = ConverterGui()
    converter_controller = ConverterController(gui)
    gui.set_controller(converter_controller)
    gui.main_window_setup()
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        gui.get_root().mainloop()