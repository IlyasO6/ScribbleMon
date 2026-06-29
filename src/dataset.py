"""
Dataset downloading and preprocessing module for the Diffusion Transformer.

This script handles the acquisition of the raw image dataset from Hugging Face
and applies the necessary preprocessing pipeline (resizing, data augmentation,
and tensor conversion) to prepare the data for training.

Usage from the command line:
    # To download and save only the raw dataset:
    $ python src/dataset.py -r

    # To run the full pipeline and generate the clean/processed dataset:
    $ python src/dataset.py
"""

import argparse
from datasets import load_dataset
from config import RAW_DATA_DIR, CLEAN_DATA_DIR
from utils import get_logger

def create_data_dir():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_raw_dataset():
    
    dataset = load_dataset("huggan/pokemon")

    print("Dataset structure")
    print(dataset)

    #  We extract only the train split because there is only this one
    return dataset["train"]

def process_dataset(): #  future implementation
    pass

def download_dataset(dataset, path):
    dataset.save_to_disk(path)


def main() -> None:
    parser = argparse.ArgumentParser(prog="dataset.py",
                                     description= "Dataset downloading and preprocessing module for the Diffusion Transformer.")
    parser.add_argument("-r", "--raw", action="store_true", help="Download the raw dataset.")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Verbosity level")  #  future implementation

    args = parser.parse_args()

    logger = get_logger(__name__, args.verbose)
    
    create_data_dir()

    raw_dataset = load_raw_dataset()
    
    if args.raw:
        download_dataset(raw_dataset, path = RAW_DATA_DIR)
        return

if __name__ == '__main__':
    main()