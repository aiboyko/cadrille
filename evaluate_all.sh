#!/bin/bash


PARENT_DIR="/home/jovyan/users/zhemchuzhnikov/boyko"
ALLGEN_DIR=$PARENT_DIR/"part_sampling_expanded/data/core_mechanical_engineering_dataset"
OUTPUTS_DIR=outputs_2

# Loop through all subfolders in the parent directory
for dir in "$ALLGEN_DIR"/*/; do
    if [ -d "$dir" ]; then
        name_i=$(basename "$dir")
        echo "Processing $name_i..."
        python evaluate.py \
        --gt-mesh-path $ALLGEN_DIR/"$name_i" \
        --pred-py-path $PARENT_DIR/cadrille/$OUTPUTS_DIR/py_files/"$name_i"
    fi
done