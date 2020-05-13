import os
import csv
import argparse
from natsort import natsorted, ns

POSSIBLE_DIRS = ["images", "compressed", "encrypted"]
THRESHOLDS = [(126.23,128.78), (3.11,3.17), (-0.01,0.01)]
CSV_HEADERS = ["file-name", "mean", "pi", "correlation"]
OUTPUT = os.path.join(".", "output")

def write_to_csv(data):
    with open(os.path.join(OUTPUT, "fpn2.csv"), "a", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(data)

def thresh_checker(data, title, index):
    threshold = THRESHOLDS[index]
    i_count = 0
    o_count = 0
    for point in data:
        if threshold[0] <= point <= threshold[1]:
            i_count += 1
        else:
            o_count += 1

    # print("%s" % title)
    # print("Above: %s, Below: %s, Equal: %s" % (a_count, b_count, e_count))

    # In, out
    return("%s/%s/  %.2f/%.2f" % (i_count, o_count, (i_count/len(data)*100), (o_count/len(data)*100)))

def main():
    # Get user input
    parser = argparse.ArgumentParser()
    parser.add_argument("res_dir", help="Choose which results to calculate FP/FNs for.")
    args = parser.parse_args()

    # Verify user input
    chosen_dir = args.res_dir
    assert chosen_dir in POSSIBLE_DIRS

    relevant_path = os.path.join(".", "results-fixed", chosen_dir)

    # Walk through results directories and read the statistics
    for root, subdirs, files in os.walk(relevant_path):
        for i in range(len(files)):
            means = []
            pis = []
            corrs = []
            current_path = os.path.join(root, natsorted(files)[i])
            with open(current_path, newline='') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                next(csvreader)
                for row in csvreader:
                    data = row[0].split(",")
                    means.append(float(data[3]))
                    pis.append(float(data[4]))
                    corrs.append(float(data[5]))

            tuple_m = thresh_checker(means, "Mean", 0)
            tuple_p = thresh_checker(pis, "Pi", 1)
            tuple_co = thresh_checker(corrs, "Correlation", 2)

            write_to_csv([current_path, tuple_m, tuple_p, tuple_co])

write_to_csv(CSV_HEADERS)
main()
