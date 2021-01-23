
# Virtualis


A tool to make virtual sensors for data quality assessment 


## Dependencies

- Python 3.8
    - matplotlib
    - numpy 
    - pandas
    - plotly
    - scikit-learn
    - Tensorflow 2.0
    - pyyaml
    - scipy
    - dvc



## Experiment pipeline

Stages:

1. **Select**: Selects usefule features of raw data into a new dataframes.
2. **Transform**: Transforms dataset (at the moment add zeros).



## Usage

### Run experiment

All stages are defined in the file `dvc.yaml`, and the parameters to be used
are saved in `params.yaml`.

To run/reproduce an experiment with any given parameters specified in
`params.yaml`, run:

```
dvc repro
```
