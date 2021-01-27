# -*- coding: utf-8 -*-
# @Author: Gutama Ibrahim
# @Date:   2021-01-23 09:47:06
# @Last Modified by:   Gutama Ibrahim
# @Last Modified time: 2021-01-24 09:02:41

import sys
from pathlib import Path


DEPOT_PATH = Path("./Depot")
DATA_PATH = DEPOT_PATH / "data"
"""Path to data."""

DATA_RAW_PATH = DATA_PATH / "raw"
"""Path to raw data"""
CNC_PATH = DATA_RAW_PATH / "CNC_Milling_dataset"
DATA_SELECTED_PATH = DATA_PATH / "selected"
"""Path to the data that is selected from raw data."""

DATA_TRANSFORMED_PATH = DATA_PATH / "transformed"
"""Path to data that is cleaned and has added features."""

DATA_SEQUENTIALIZED_PATH = DATA_PATH / "sequentialized"
"""Path to data that is split into sequences."""

DATA_SPLIT_PATH = DATA_PATH / "split"
"""Path to data that is split into train and test set."""

DATA_SCALED_PATH = DATA_PATH / "scaled"
"""Path to scaled data."""

DATA_COMBINED_PATH = DATA_PATH / "combined"
"""Path to combined data, ready for training."""

MODELS_PATH = DEPOT_PATH / "models"
"""Path to models."""

MODELS_FILE_PATH = MODELS_PATH / "model.h5"
"""Path to model file."""

METRICS_PATH = DEPOT_PATH / "metrics"
"""Path to folder containing metrics file."""

METRICS_FILE_PATH = METRICS_PATH / "metrics.json"
"""Path to file containing metrics."""

PLOTS_PATH = DEPOT_PATH / "plots"
"""Path to folder plots."""

PREDICTION_PLOT_PATH = PLOTS_PATH / "prediction.png"
"""Path to file containing prediction plot."""

TRAININGLOSS_PLOT_PATH = PLOTS_PATH / "trainingloss.png"
"""Path to file containing training loss plot."""
