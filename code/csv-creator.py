import subprocess
import argparse
import os

CSV_HEADERS = ["File-bytes","Entropy","Chi-square","Mean","Monte-Carlo-Pi","Serial-Correlation"]
RESULTS_FILE_NAME = "results.csv"
POSSIBLE_DIRS = ["images", "compressed", "encrypted"]


def get_user_source():
    # Get user-specified source directory
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Which files to generate statistics for.")
    args = parser.parse_args()
    chosen_dir = args.source
    assert chosen_dir in POSSIBLE_DIRS
    source_path = os.path.join(".", chosen_dir)
    results_path = os.path.join(".", "results", chosen_dir)

    # Return path of source data and path where resulting csvs should be stored
    return source_path, results_path


def main():
    source_path, results_path = get_user_source()
    for root, subdirs, files in os.walk(source_path):
        if files:
            # This directory has files in it, let's process them!
            csv_name = ("%s-%s" % (root, RESULTS_FILE_NAME)).replace("/","-")[2:]
            with open(os.path.join(results_path, csv_name), "w+") as f:
                for file in files:
                    # For each file in the directory, call ent
                    if not os.path.isdir(file):
                        subprocess.call(["ent", "-t", os.path.join(root, file)], stdout=f)


if __name__ == "__main__":
    main()
