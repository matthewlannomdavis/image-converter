import tkinter as tk
from tkinter import ttk

#Create main window
root = tk.Tk()
root.title("Mert's Image Converter")
#Set window size and opening location
root.geometry('600x500+50+50')

#Directory search bar
ttk.Label(root, text='Directory to convert').pack()
directoryToConvert = ttk.Label(root, text=f'../folder/file')
directoryToConvert.pack()

#box to display conversion information
informationOutput = tk.Text(root, height="15")
informationOutput.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

informationOutputScroll = ttk.Scrollbar(
    informationOutput,
    orient=tk.VERTICAL,
    command=informationOutput.yview
)
informationOutputScroll.pack(side=tk.RIGHT, fill=tk.Y)

#Delete Option
deleteOriginal = tk.BooleanVar()
deleteOption = ttk.Checkbutton(
    root,
    text= "Delete?",
    variable= deleteOriginal
)
deleteOption.pack()

#Run conversion
convertButton = ttk.Button(
    root,
    text="Convert Images"
)
convertButton.pack()


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()