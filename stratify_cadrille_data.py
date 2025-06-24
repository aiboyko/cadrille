import os
import sys
import argparse
from script_stratify_subfolders import stratify_subfolders


def stratify_cadrille_data(
    gt_parts_dir="CAD_DATASETS/cadrille_domains_img/gt",
    generated_parts_dir="outputs_2",
    stratified_output_dir="CAD_DATASETS/cadrille_img_stratified",
    remove_original_files=False,
):
    """
    Stratify both ground truth and generated data for Cadrille dataset.

    Args:
        outputs_dir (str): Directory containing generated outputs
    """

    # Define paths
    gt_input_path = gt_parts_dir
    gen_input_path = generated_parts_dir

    gt_output_path = os.path.join(stratified_output_dir, "gt")
    gen_output_path = os.path.join(stratified_output_dir, "gen")

    print("Stratifying ground truth data...")
    print(f"Input: {gt_input_path}")
    print(f"Output: {gt_output_path}")

    # Stratify ground truth data
    stratify_subfolders(
        input_megafolder_path=gt_input_path,
        output_path=gt_output_path,
        remove_original_files=remove_original_files,
    )

    print("\nStratifying generated data...")
    print(f"Input: {gen_input_path}")
    print(f"Output: {gen_output_path}")

    # Stratify generated data
    stratify_subfolders(
        input_megafolder_path=gen_input_path,
        output_path=gen_output_path,
        remove_original_files=remove_original_files,
    )

    print("\nStratification complete!")


def create_argparser():
    parser = argparse.ArgumentParser(description="Stratify Cadrille dataset")
    parser.add_argument(
        "-gt",
        "--gt-parts-dir",
        type=str,
        default="CAD_DATASETS/cadrille_domains_img/gt",
        help="Directory containing ground truth parts (default: CAD_DATASETS/cadrille_domains_img/gt)",
    )
    parser.add_argument(
        "-gen",
        "--generated-parts-dir",
        type=str,
        default="outputs_2",
        help="Directory containing generated outputs (default: outputs_2)",
    )
    parser.add_argument(
        "-out",
        "--stratified-output-dir",
        type=str,
        default="CAD_DATASETS/cadrille_img_stratified",
        help="Directory to save the stratified data (default: CAD_DATASETS/cadrille_img_stratified)",
    )
    parser.add_argument(
        "-rm",
        "--remove-original-files",
        action="store_true",
        help="Remove original files after stratification (default: False)",
    )
    return parser


if __name__ == "__main__":
    parser = create_argparser()
    args = parser.parse_args()
    stratify_cadrille_data(
        gt_parts_dir=args.gt_parts_dir,
        generated_parts_dir=args.generated_parts_dir,
        stratified_output_dir=args.stratified_output_dir,
        remove_original_files=args.remove_original_files,
    )
