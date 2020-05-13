# Needed: CSV, Matplotlib

# INDEX REMINDER:
# 0 = File-bytes
# 1 = Entropy
# 2 = Chi-square
# 3 = Mean
# 4 = Monte-Carlo Pi
# 5 = Serial-Correlation

import os
import csv
import random
import argparse
import seaborn as sns
import matplotlib.pyplot as plt
from natsort import natsorted, ns

POSSIBLE_DIRS = ["images", "compressed", "encrypted"]
POSSIBLE_STATS = ["ent", "chi", "mean", "pi", "corr"]
GRAPH_OUTPUT = os.path.join(".", "output")
plt.rcParams.update({"font.size": 20})
plt.rcParams.update({"legend.title_fontsize": 10})
plt.rcParams.update({"legend.fontsize": 10})

"""
===== PLOT CONFIGURATION START =====
"""
# Verticle line x-coordinates for group visualisation
def xthresholdswitch(index):
    switch = {
        "images": [1004, 1000, 1000, 6024, 6000, 6024, 6000],
        "compressed": [8874, 8901, 8874, 8901, 9860, 9890],
        "encrypted": [986, 0]
    }
    return switch.get(index)

# Title and axes labels
def titleswitch(index):
    switch = {
        "ent": "Entropy",
        "chi": "Chi-Square",
        "mean": "Arithmetic Mean",
        "pi": "Monte Carlo Value for Pi",
        "corr": "Serial Byte Correlation Coefficient"
    }
    return switch.get(index)

# Y-Axis limits
def ylimswitch(index):
    switch = {
        "ent": (7.8,8.0),
        "chi": (175,350),
        "mean": (0, 255),
        "pi": (3.0, 3.5),
        "corr": (-1.0, 1.0)
    }
    return switch.get(index)

# Y-Coordinate of ythreshold line
def ythresholdswitch(index):
    switch = {
        "ent": [7.99],
        "chi": [293.25],
        "mean": [126.23, 128.78],
        "pi": [3.11, 3.17],
        "corr": [-0.01, 0.01]
        # "mean": 127.5,
        # "pi": 3.14,
        # "corr": 0.00
    }
    return switch.get(index)

# Index of each statistic in the csvs
def statswitch(index):
    switch = {
        "ent": 1,
        "chi": 2,
        "mean": 3,
        "pi": 4,
        "corr": 5
    }
    return switch.get(index)

"""
===== PLOT CONFIGURATION END =====
"""

def thresholdsum(li):
    return sum(li)

def main():
    # Get user input
    parser = argparse.ArgumentParser()
    parser.add_argument("res_dir", help="Choose which results to generate graphs for.")
    parser.add_argument("stat", help="ent, chi, mean, pi, corr")
    args = parser.parse_args()
    # Verify user input
    chosen_dir = args.res_dir
    chosen_stat = args.stat
    assert chosen_dir in POSSIBLE_DIRS
    assert chosen_stat in POSSIBLE_STATS

    # Pull appropriate graph config
    statindex = statswitch(chosen_stat)
    ythreshold = ythresholdswitch(chosen_stat)
    ylim = ylimswitch(chosen_stat)
    lab = titleswitch(chosen_stat)
    xthreshold = xthresholdswitch(chosen_dir)

    relevant_path = os.path.join(".", "results-fixed", chosen_dir)

    labels = []
    offset = 0
    plt.figure(figsize=(20.0, 12.0))

    # Walk through results directories and read relevant statistic into list
    for root, subdirs, files in os.walk(relevant_path):
        for i in range(len(files)):
            natsortfiles = natsorted(files)
            if chosen_dir == "images":
                natsortfiles_corrected = natsortfiles[:2]
                natsortfiles_corrected.append(natsortfiles[len(natsortfiles)-1])
                natsortfiles_corrected.extend(natsortfiles[2:len(natsortfiles)-1])
            else:
                natsortfiles_corrected = natsortfiles
            labels.append(natsortfiles_corrected[i])
            stat = []
            current_path = os.path.join(root, natsortfiles_corrected[i])
            with open(current_path, newline='') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                next(csvreader)
                for row in csvreader:
                    data = row[0].split(",")
                    stat.append(float(data[statindex]))

            xs = range(0 + offset, len(stat) + offset)

            # Give the graph a nice (non-repeating) colour scheme
            colours = sns.color_palette("hls", len(files))
            plt.scatter(xs, stat, c=colours[i])

            offset += len(stat)

    # Finalise plot
    plt.ylim(ylim)
    # plt.legend(labels, loc=2, bbox_to_anchor=(1.05, 1), shadow=True, ncol=2, borderaxespad=0.)
    # plt.title("%s for %s Files" % (lab, offset))
    plt.xlabel("File Count")
    plt.ylabel(lab)

    # Plot the horizontal and vertical lines
    for thresh in ythreshold:
        plt.axhline(thresh, c='r')
    for i in range(len(xthreshold)-1):
        plt.axvline(thresholdsum(xthreshold[0:i+1]), c="#000000", linestyle='dashed')

    # Show the graph
    # plt.show()

    # Save the graph (if applicable)
    plt.savefig(os.path.join(GRAPH_OUTPUT, "%s-%s" % (chosen_dir, chosen_stat)), bbox_inches='tight', format='eps')


main()
