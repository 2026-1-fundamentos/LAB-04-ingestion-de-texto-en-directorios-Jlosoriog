# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import pandas as pd


def pregunta_01():

    zip_path = "files/input.zip"
    extract_dir = "files"

    # Descomprime el archivo (crea files/input/...)
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(extract_dir)

    input_dir = os.path.join(extract_dir, "input")
    output_dir = os.path.join(extract_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    for split in ("train", "test"):
        split_dir = os.path.join(input_dir, split)
        rows = []
        for sentiment in sorted(os.listdir(split_dir)):
            sentiment_dir = os.path.join(split_dir, sentiment)
            if not os.path.isdir(sentiment_dir):
                continue
            for fname in sorted(os.listdir(sentiment_dir)):
                fpath = os.path.join(sentiment_dir, fname)
                with open(fpath, encoding="utf-8") as f:
                    phrase = f.read().strip()
                rows.append({"phrase": phrase, "sentiment": sentiment})

        df = pd.DataFrame(rows, columns=["phrase", "sentiment"])
        df.to_csv(os.path.join(output_dir, f"{split}_dataset.csv"), index=False)