"""Run every stage of the AdSpark analysis pipeline in order."""
import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STAGES = [
    "00_prepare_data.py",
    "01_data_loading.py",
    "02_eda.py",
    "03_feature_engineering.py",
    "04_linear_regression.py",
    "05_logistic_regression.py",
    "06_regularization.py",
    "07_decision_tree.py",
    "08_ensemble.py",
]


def main() -> None:
    for stage in STAGES:
        print(f"\n{'=' * 70}\nRunning {stage}\n{'=' * 70}")
        code = subprocess.call([sys.executable, os.path.join(BASE_DIR, stage)])
        if code != 0:
            print(f"FAILED: {stage} (exit code {code})")
            sys.exit(code)
    print("\nAll stages completed successfully.")


if __name__ == "__main__":
    main()