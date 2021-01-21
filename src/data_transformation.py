import pandas as pd
import numpy as np


def add_noise(df, features, frac):
    """
    Add noise to feature(s) of a dataframe.
    This method selects a given fraction of a given column of dataset and replace it wit
    zeros.

    Parameters:
        df: A dataframe you want to noise
        features: list of string containing names of dataframe columns that
                    you want to add noise(zeros) to
        frac:float value that tells percentage of the columns values to be
        replaced by zero




    """
    for i in range(len(features)):

        feature = features[i]
        sample = df[feature].sample(frac=frac)

        noise = pd.Series(0, index=np.arange(
            len(sample)), name=sample.name)

        df.loc[sample.index, feature] = noise.values
        df.rename(columns={feature: feature + '_MD'}, inplace=True)

    return df


if __name__ == '__main__':
    pass
