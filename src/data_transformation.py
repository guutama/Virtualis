# -*- coding: utf-8 -*-
# @Author: Gutama Ibrahim
# @Date:   2021-01-22 10:17:36
# @Last Modified by:   Gutama Ibrahim
# @Last Modified time: 2021-01-23 12:22:50
import pandas as pd
import numpy as np
import yaml

import sys
import os
from constants import DATA_TRANSFORMED_PATH
sys.path.insert(1, "../TimeSerieDataRepairSystem/src")
from preprocess_utils import read_csv, move_column


def add_noise(filepaths):
    # filepaths
    """
    Add noise to feature(s) of a dataframe.
    This method selects a given fraction of a given column of dataset and replace it with
    zeros.
    parameters:
        filepaths: list of strings containing path to datasets to be
        transformed




    """
    # create folder
    DATA_TRANSFORMED_PATH.mkdir(parents=True, exist_ok=True)

    # Load parameters
    params = yaml.safe_load(open("params.yaml"))["transform"]["add-noise"]

    features = params["features"]
    label = params["label"]
    frac = params["frac"]

    for filepath in filepaths:
        print("Processing {}".format(filepath))
        # READ RAW DATA
        df, index = read_csv(
            filepath)
        df_transformed = df.copy()
        for i in range(len(features)):

            feature = features[i]
            sample = df_transformed[feature].sample(frac=frac)

            noise = pd.Series(0, index=np.arange(
                len(sample)), name=sample.name)

            df_transformed.loc[sample.index, feature] = noise.values
            df_transformed.rename(
                columns={feature: feature + '_MD'}, inplace=True)
            df_transformed.insert(0, "label", df[label])
        df_transformed.to_csv(
            DATA_TRANSFORMED_PATH
            / (os.path.basename(filepath).replace("selected", "transformed"))
        )


if __name__ == '__main__':
    add_noise(sys.argv[1:])
