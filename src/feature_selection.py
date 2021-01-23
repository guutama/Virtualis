# -*- coding: utf-8 -*-
# @Author: Gutama Ibrahim
# @Date:   2021-01-23 09:10:31
# @Last Modified by:   Gutama Ibrahim
# @Last Modified time: 2021-01-23 11:05:49


import sys
import os
import glob
import pandas as pd
import yaml

from constants import DATA_SELECTED_PATH


def feature_selector(filepaths):
    """
    Select  all features spesified in params.yaml of a given dataframe and save it into a
    new dataframe. NB:All features spesified in params.yaml/select/features must
    a column of that given datafram

    parameters:
        filepaths: list of strings containing path to datasets
    """
    # Load parameters
    params = yaml.safe_load(open("params.yaml"))["select"]

    features = params["features"]
    DATA_SELECTED_PATH.mkdir(parents=True, exist_ok=True)
    for filepath in filepaths:
        print("Processing {}".format(filepath))
        # READ RAW DATA
        df = pd.read_csv(filepath)
        selected_df = df[features].copy()
        selected_df.to_csv(
            DATA_SELECTED_PATH
            / (os.path.basename(filepath).replace(".", "-selected."))
        )


if __name__ == '__main__':
    feature_selector(sys.argv[1:])
