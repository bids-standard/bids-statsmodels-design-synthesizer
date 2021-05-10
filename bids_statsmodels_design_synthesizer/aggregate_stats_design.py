#! /usr/bin/env python
import argparse
import sys
from boutiques.descriptor2func import function
from boutiques.prettyprint import PrettyPrinter
import json
from pathlib import Path

from bids_statsmodels_design_synthesizer import transformations
from bids.utils import convert_JSON

# The following is a hack to avoid writing cli for now
descriptor_fname = "bids-app-bids-statsmodels-design-synthesizer.json"
IO_DESCRIPTOR_JSON = (
    Path(__file__).absolute().parent.parent / "boutiques" / descriptor_fname
)
if not IO_DESCRIPTOR_JSON.exists():
    IO_DESCRIPTOR_JSON = Path(__file__).parent / descriptor_fname
if not IO_DESCRIPTOR_JSON.exists():
    raise EnvironmentError("Cannot find the boutiques descriptor to construct the CLI")


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
    coll = NotImplemented

    # return early for now
    return 0
    # perform transformations
    colls = transformations.Transformermanger().transform(coll, model_transforms)

    # Save colls
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover""Main module."""
