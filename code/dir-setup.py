import os

POSSIBLE_DIRS = ["images", "compressed", "encrypted"]
RESULTS_DIR = "results"
RESULTS_FIXED_DIR = "results-fixed"


def main():
    res_path = os.path.join(".", RESULTS_DIR)
    fixed_res_path = os.path.join(".", RESULTS_FIXED_DIR)
    if not os.path.exists(res_path):
        os.mkdir(res_path)
    if not os.path.exists(fixed_res_path):
        os.mkdir(fixed_res_path)

    for d in POSSIBLE_DIRS:
        path = os.path.join(".", d)
        res_path = os.path.join(".", RESULTS_DIR, d)
        fixed_res_path = os .path.join(".", RESULTS_FIXED_DIR, d)
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(res_path):
            os.mkdir(res_path)
        if not os.path.exists(fixed_res_path):
            os.mkdir(fixed_res_path)


if __name__ == "__main__":
    main()
