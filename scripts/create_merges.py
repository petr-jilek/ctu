import os
from pathlib import Path

from pypdf import PdfWriter
from shared import path_consts


def create_merges(relative_path: str, out_relative_path: str, out_name: str):
    path = path_consts.SUBJECTS_FOLDER_PATH / relative_path

    pdfs = [f for f in os.listdir(path) if f.endswith(".pdf")]
    pdfs = sorted(pdfs)

    pdf_writer = PdfWriter()

    for pdf in pdfs:
        pdf_writer.append(str(path / pdf))

    pdf_writer.write(
        str(path_consts.SUBJECTS_FOLDER_PATH / out_relative_path / (out_name + ".pdf"))
    )


if __name__ == "__main__":
    create_merges(Path("en3") / "cv", Path("en3"), "cv_all")
