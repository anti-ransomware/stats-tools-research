import os

POSSIBLE_DIRS = ["images", "compressed", "encrypted"]
RESULTS_DIR = "results"


def main():
    res_path = os.path.join(".", RESULTS_DIR)
    if not os.path.exists(res_path):
        os.mkdir(res_path)

    for d in POSSIBLE_DIRS:
        path = os.path.join(".", d)
        res_path = os.path.join(".", RESULTS_DIR, d)
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(res_path):
            os.mkdir(res_path)


if __name__ == "__main__":
    main()
