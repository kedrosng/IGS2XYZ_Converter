import os
import ezdxf
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm

def dxf_to_xyz():
    root = tk.Tk()
    root.withdraw()
    dxf_file_path = filedialog.askopenfilename(title="Select DXF file", filetypes=[("DXF Files", "*.dxf")])
    if not dxf_file_path:
        print("No DXF file selected.")
        return
    dxf_folder_path = os.path.dirname(dxf_file_path)
    xyz_file_path = os.path.join(dxf_folder_path, "output.xyz")
    
    print("Loading...")
    dxf = ezdxf.readfile(dxf_file_path)
    msp = dxf.modelspace()
    point_count = sum(1 for entity in msp if entity.dxftype() == 'POINT')
    with open(xyz_file_path, 'w') as xyz_file:
        for entity in tqdm(msp, total=point_count):
            if entity.dxftype() == 'POINT':
                x, y, z = entity.dxf.location
                xyz_file.write(f"{x} {y} {z}\n")
    print(f"Conversion complete! XYZ file saved at {xyz_file_path}")

dxf_to_xyz()