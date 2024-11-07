import os
import shutil
from pathlib import Path

from shared import path_consts


def copy_to_subjects(relative_path: str):
    path = path_consts.TEX_FOLDER_PATH / relative_path

    dirs = [d for d in os.listdir(path) if os.path.isdir(path / d)]
    for dir in dirs:
        copy_to_subjects(relative_path / dir)

    pdfs = [f for f in os.listdir(path) if f.endswith(".pdf")]
    for pdf in pdfs:
        source = path / pdf
        destination = path_consts.SUBJECTS_FOLDER_PATH / relative_path / pdf

        if not os.path.exists(path_consts.SUBJECTS_FOLDER_PATH / relative_path):
            os.makedirs(path_consts.SUBJECTS_FOLDER_PATH / relative_path)

        shutil.copy(source, destination)


if __name__ == "__main__":
    copy_to_subjects(Path(""))
