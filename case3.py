import tkinter as tk
from tkinter import filedialog
import logomaker
import pandas as pd
import matplotlib.pyplot as plt

def generate_logo():
    sequences = entry.get().split(",")
    counts_dict = {char: [0]*len(sequences[0]) for char in 'ACGT'}  #要增加字母
    for seq in sequences:
        for i, char in enumerate(seq):
            counts_dict[char][i] += 1
    counts_df = pd.DataFrame(counts_dict)
    logo = logomaker.Logo(counts_df)
    plt.savefig("mylogo.png")
    plt.savefig("mylogo.jpg")
    plt.savefig("mylogo.svg")
    
    

def save_logo():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG File", "*.png"), 
                                                        ("JPG File", "*.jpg"),
                                                        ("SVG File", "*.svg")])
    plt.savefig(file_path)

root = tk.Tk()
label = tk.Label(root, text="Please enter your sequences, separated by commas:")
label.pack()
entry = tk.Entry(root)
entry.pack()
logo_button = tk.Button(root, text="Generate Logo", command=generate_logo)
logo_button.pack()
# save_button = tk.Button(root, text="Save Logo", command=save_logo)
# save_button.pack()
root.mainloop()
