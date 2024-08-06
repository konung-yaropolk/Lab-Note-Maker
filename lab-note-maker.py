#!/usr/bin/env python3
import os
import textwrap
from datetime import datetime
#from fpdf import FPDF

DIRECTORIES = [
    # 'F:\Lab Work Files\2-photon',
    # 'F:\Lab Work Files\Patch-clamp data',
    '/run/media/lol/Yarik Data/Lab Work Files/2-photon',
    '/run/media/lol/Yarik Data/Lab Work Files/Patch-clamp data',
    ]


def find_txt_files(directory):
    txt_files = []  # To store the paths of .txt files

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith("!") and file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))

    return txt_files


def txt_catcher(directories):
    txt_files = []

    for directory in directories:

        if os.path.isdir(directory):
            
            txt_files.extend(find_txt_files(directory))
            
            if txt_files:
                print("Open path: ", directory)
            else:
                print("No .txt files found in the: ", directory)

        else:
            print("Invalid directory path: ", directory)
    
    return txt_files


def textgen(txt_files):

    date = datetime.now()
    head = "Lab Note\nGenerated: {}\n\nList of source files: \n\n\n".format(date)
    text = ""

    for file_path in txt_files:

        head += file_path[2:]+"\n"

        text += "#"*96 + "\n"
        text += "File: {}\n\n".format(file_path[2:])

        with open(file_path, "r", encoding="utf8") as f:
            text += f.read() + "\n\n\n"

    text = head + '\n\n\n' + text

    return text


# def text_to_pdf(text, filename):

#     a4_width_mm = 210
#     pt_to_mm = 0.35
#     fontsize_pt = 10
#     fontsize_mm = fontsize_pt * pt_to_mm
#     margin_bottom_mm = 10
#     character_width_mm = 7 * pt_to_mm
#     width_text = a4_width_mm / character_width_mm

#     pdf = FPDF(orientation='P', unit='mm', format='A4')
#     pdf.set_auto_page_break(True, margin=margin_bottom_mm)
#     pdf.add_page()
#     pdf.set_font(family='Courier', size=fontsize_pt)
#     splitted = text.split('\n')

#     for line in splitted:
#         lines = textwrap.wrap(line, width_text)

#         if len(lines) == 0:
#             pdf.ln()

#         for wrap in lines:
#             pdf.cell(0, fontsize_mm, wrap, ln=1)

#     pdf.output(filename, 'F')

def main():

    txt_files = txt_catcher(DIRECTORIES)
    lab_note = textgen(txt_files)

    #text_to_pdf(lab_note, 'lab_note.pdf')
    with open('lab_note.txt', 'w', encoding="utf8") as f:
        f.write(lab_note)



if __name__ == "__main__":
    main()
