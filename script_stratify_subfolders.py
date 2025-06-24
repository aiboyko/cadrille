"""this script takes a folder with subfolders like: shaft, fork, etc.
each subfolder contains files like:
1.stl, 2.stl or 1+0.stl, 1+1.stl, 1+2.stl, 2+1.stl etc.
the script should take the files and put them in a new folder.
The files must be prepended with a name of the subfolder.
"""

import os
import shutil
import argparse
from tqdm import tqdm


def get_all_files_in_folder(folder_path):
    return [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
        and (f.endswith(".stl") or f.endswith(".ply") or f.endswith(".obj"))
    ]


def get_all_subfolders_in_folder(folder_path):
    return [
        f
        for f in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, f))
    ]


def stratify_subfolders(
    input_megafolder_path, output_path, remove_original_files=False
):

    subfolders = get_all_subfolders_in_folder(input_megafolder_path)
    for subfolder in subfolders:
        files = get_all_files_in_folder(os.path.join(input_megafolder_path, subfolder))
        for file in tqdm(files):
            new_file_name = subfolder + "_" + file
            if not os.path.exists(output_path):
                os.makedirs(output_path, exist_ok=True)
            if not os.path.exists(os.path.join(output_path, new_file_name)):
                shutil.copy(
                    os.path.join(input_megafolder_path, subfolder, file),
                    os.path.join(output_path, new_file_name),
                )
            else:
                print(f"File {new_file_name} already exists. Skipping.")
            if remove_original_files:
                os.remove(os.path.join(input_megafolder_path, subfolder, file))


def create_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_megafolder_path", type=str, help="Path to the input megafolder")
    parser.add_argument("output_path", type=str, help="Path to the output folder")
    parser.add_argument("--remove-original-files", action="store_true")
    return parser


if __name__ == "__main__":
    args = create_argparser().parse_args()
    stratify_subfolders(
        args.input_megafolder_path, args.output_path, args.remove_original_files
    )
