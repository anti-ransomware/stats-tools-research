import argparse
import csv
import os

CSV_PATH = os.path.join(".", "results")
CSV_HEADERS = ["File-bytes","Entropy","Chi-square","Mean","Monte-Carlo-Pi","Serial-Correlation"]
POSSIBLE_DIRS = ["images", "compressed", "encrypted"]

def get_user_source():
    # Get user-specified source directory
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Which csvs to fix.")
    args = parser.parse_args()
    chosen_dir = args.target
    assert chosen_dir in POSSIBLE_DIRS
    target_path = os.path.join(".", "results", chosen_dir)

    # Return selected csv folder name and full path of csvs to fix
    return chosen_dir, target_path

def main():
    chosen, target = get_user_source()
    fixed_csv_path = os.path.join(".", "results-fixed", chosen)

    for root, subdirs, files in os.walk(target):
        for f in files:
            path = os.path.join(root, f)
            with open(path, newline='') as csvfile_r:
                csvreader = csv.reader(csvfile_r, delimiter=' ', quotechar='|')
                with open(os.path.join(fixed_csv_path, f), "w+") as csvfile_w:
                    csvwriter = csv.writer(csvfile_w, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    csvwriter.writerow(CSV_HEADERS)
                    for row in csvreader:
                        if "File-bytes" not in row[0]:
                            care = row[0][2:]
                            csvwriter.writerow(care.split(","))

main()
