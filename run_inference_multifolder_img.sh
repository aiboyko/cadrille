#!/bin/bash

PARENT_DIR="/home/jovyan/users/zhemchuzhnikov/boyko/part_sampling_expanded/data/core_mechanical_engineering_dataset/"
OUTPUTS_DIR=outputs_2_img

# Loop through all subfolders in the parent directory
for dir in "$PARENT_DIR"/*/; do
    if [ -d "$dir" ]; then
        name_i=$(basename "$dir")
        echo "Processing $name_i..."
        #python test.py --data "$name_i" --output_folder "./outputs/$name_i"
        python test.py --data-path $PARENT_DIR \
        --split "$name_i" --mode img --n-samples 1 --py-path "./$OUTPUTS_DIR/py_files/$name_i"
    fi
done