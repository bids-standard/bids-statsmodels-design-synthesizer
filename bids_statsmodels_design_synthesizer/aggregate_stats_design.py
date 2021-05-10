#! /usr/bin/env python
import argparse
import sys
from boutiques.descriptor2func import function
from boutiques.prettyprint import PrettyPrinter
import json
from pathlib import Path

from bids_statsmodels_design_synthesizer import transformations
from bids.utils import convert_JSON
from bids.variables import BIDSRunVariableCollection, SparseRunVariable
from bids.layout.utils import parse_file_entities
import pandas as pd
import numpy as np
from collections import namedtuple

# The following is a hack to avoid writing cli for now
descriptor_fname = "bids-app-bids-statsmodels-design-synthesizer.json"
IO_DESCRIPTOR_JSON = (
    Path(__file__).absolute().parent.parent / "boutiques" / descriptor_fname
)
if not IO_DESCRIPTOR_JSON.exists():
    IO_DESCRIPTOR_JSON = Path(__file__).parent / descriptor_fname
if not IO_DESCRIPTOR_JSON.exists():
    raise EnvironmentError("Cannot find the boutiques descriptor to construct the CLI")

def get_events_collection(_data,run_info,drop_na=True):
    """"
    This is an attempt to minimally implement:
    https://github.com/bids-standard/pybids/blob/statsmodels/bids/variables/io.py
    """
    colls_output = []
    if 'amplitude' in _data.columns:
        if (_data['amplitude'].astype(int) == 1).all() and \
            'trial_type' in _data.columns:
            msg = ("Column 'amplitude' with constant value 1 "
                   "is unnecessary in event files; ignoring it.")
            _data = _data.drop('amplitude', axis=1)
        else:
            msg = ("Column name 'amplitude' is reserved; "
                   "renaming it to 'amplitude_'.")
            _data = _data.rename(
                columns={'amplitude': 'amplitude_'})
            warnings.warn(msg)

    _data = _data.replace('n/a', np.nan)  # Replace BIDS' n/a
    _data = _data.apply(pd.to_numeric, errors='ignore')

    _cols = list(set(_data.columns.tolist()) -
                {'onset', 'duration'})

    # Construct a DataFrame for each extra column
    for col in _cols:
        df = _data[['onset', 'duration']].copy()
        df['amplitude'] = _data[col].values

        # Add in all of the run's entities as new columns for
        # index
#        for entity, value in entities.items():
#            if entity in ALL_ENTITIES:
#                df[entity] = value
#
        if drop_na:
            df = df.dropna(subset=['amplitude'])

        if df.empty:
            continue
        var = SparseRunVariable(
        name=col, data=df, run_info=run_info, source='events')
        colls_output.append(var)

    output = BIDSRunVariableCollection(colls_output)
    return output


def main(user_args=None):
    """Console script for bids_statsmodels_design_synthesizer."""
    if not user_args:
        desc = json.load(open(IO_DESCRIPTOR_JSON))
        p = PrettyPrinter(desc)
        user_args = p.parser.parse_args()
        user_args = vars(user_args)

    # get specified transformations
    model_file = Path(user_args["MODEL"])
    if not model_file.exists():
        model_file = Path(user_args["BIDS_DIR"]) / "models" / user_args["MODEL"]
    model = convert_JSON(json.loads(model_file.read_text()))
    model_transforms = model["steps"][0]["transformations"]

    # Get relevant collection
    coll_df = pd.read_csv(user_args["EVENTS_TSV"], delimiter="\t")
    RunInfo = namedtuple('RunInfo', ['entities','duration'],)
    run_info = RunInfo(parse_file_entities(user_args["EVENTS_TSV"]),user_args['DURATION'])
    coll = get_events_collection(coll_df,[run_info])

    # perform transformations
    colls = transformations.TransformerManager().transform(coll, model_transforms)

    # return early for now
    return 0

    # Save colls
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover""Main module."""
