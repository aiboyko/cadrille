#!/bin/bash

PARENT_DIR="/home/jovyan/users/zhemchuzhnikov/boyko/part_sampling_expanded/data/core_mechanical_engineering_dataset/"
OUTPUTS_DIR=outputs_2

# Loop through all subfolders in the parent directory
for dir in "$PARENT_DIR"/*/; do
    if [ -d "$dir" ]; then
        name_i=$(basename "$dir")
        echo "Processing $name_i..."
        #python test.py --data "$name_i" --output_folder "./outputs/$name_i"
        python test.py --data-path ../part_sampling_expanded/data/core_mechanical_engineering_dataset/ \
        --split "$name_i" --n-samples 5 --py-path "./$OUTPUTS_DIR/py_files/$name_i"
    fi
done