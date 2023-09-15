#!/usr/bin/env python3
import os


DIRECTORIES = [
    'F:\Lab Work Files\\2-photon',
    'F:\Lab Work Files\Patch-clamp data',
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

    text = ""

    for file_path in txt_files:

        text += "#"*100 + "\n"
        text += "File: {}\n\n".format(file_path[2:])

        with open(file_path, "r", encoding="utf8") as f:
            text += f.read() + "\n\n\n"

    return text


def main():

    txt_files = txt_catcher(DIRECTORIES)
    lab_note = textgen(txt_files)

    with open('lab_note.txt', 'w', encoding="utf8") as f:
        f.write(lab_note)


if __name__ == "__main__":
    main()
