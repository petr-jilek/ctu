import os
import shutil
from pathlib import Path

ROOT_FOLDER_PATH = Path(__file__).parent.parent

SUBJECTS = "subjects"
SUBJECTS_FOLDER_PATH = ROOT_FOLDER_PATH / SUBJECTS

TEX = "tex"
TEX_FOLDER_PATH = ROOT_FOLDER_PATH / TEX


def copy_to_subjects(relative_path: str):
    path = TEX_FOLDER_PATH / relative_path

    dirs = [d for d in os.listdir(path) if os.path.isdir(path / d)]
    for dir in dirs:
        copy_to_subjects(relative_path / dir)

    pdfs = [f for f in os.listdir(path) if f.endswith(".pdf")]
    for pdf in pdfs:
        source = path / pdf
        destination = SUBJECTS_FOLDER_PATH / relative_path / pdf

        if not os.path.exists(SUBJECTS_FOLDER_PATH / relative_path):
            os.makedirs(SUBJECTS_FOLDER_PATH / relative_path)

        shutil.copy(source, destination)


if __name__ == "__main__":
    copy_to_subjects(Path(""))
