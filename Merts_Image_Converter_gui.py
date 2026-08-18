import tkinter as tk
from tkinter import ttk
from ConverterController import ConverterController



class ConverterGui:
    def __init__(self):
        self.converter_controller = None
        self.root = tk.Tk()
        self.root.title = ("Mert's Image Converter")
        #self.root.geometry('600x500+50+50')
        self.directory_to_convert = None
        self.search_bttn = None
        self.information_output = None
        self.information_output_scroll = None
        self.del_switch = None
        self.del_bool = tk.BooleanVar()
        self.convert_bttn = None
        
    def set_controller(self, ctrl):
        self.converter_controller = ctrl
    def set_directory_to_convert(self, directory):
        self.directory_to_convert.config(text=directory)
    def add_message(self, message):
        self.information_output.insert(
            tk.END,
            message + '\n'
        )
        self.information_output.see(tk.END)
    def main_window_setup(self):
        ttk.Label(self.root, text='Directory to convert').grid(row=0, column=0, sticky="nw")
        #create widgets
        self.directory_to_convert = ttk.Label(self.root, text='')
        self.search_bttn = tk.Button(
            self.root,
            text='Select',
            command=self.converter_controller.find_directory
        )
        self.information_output = tk.Text(self.root, width='60', height='15')
        self.information_output_scroll = ttk.Scrollbar(
            self.information_output,
            orient="vertical",
            command=self.information_output.yview
        )
        self.del_switch = ttk.Checkbutton(
            self.root, 
            text='Delete Original Files', 
            variable=self.del_bool, 
            command=self.converter_controller.set_delete
            )
        self.convert_bttn = tk.Button(
            self.root,
            text='Convert',
            command=self.converter_controller.run_conversion
        )

        #arrange window.
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=2)
        self.directory_to_convert.grid(row=0, column=0, sticky="n", padx=10, pady=5)
        
        self.search_bttn.grid(row=0, column=0, sticky="ne", padx=2, pady=5)
        self.del_switch.grid(row=1, column=0, pady=5, sticky="w")
        self.information_output.grid(row=2, column=0, padx=10, pady=10)
        self.convert_bttn.grid(row=3, column=0, sticky="nesw", padx=15, pady=15)

    def get_root(self):
        return self.root