#! /usr/bin/env python
import argparse
import sys
from boutiques.descriptor2func import function
from boutiques.prettyprint import PrettyPrinter
import json
from pathlib import Path

# The following is a hack to avoid writing cli for now
descriptor_fname = "bids-app-bids-statsmodels-design-synthesizer.json"
IO_DESCRIPTOR_JSON = Path(__file__).absolute().parent.parent / "boutiques" / descriptor_fname
if not IO_DESCRIPTOR_JSON.exists():
    IO_DESCRIPTOR_JSON = Path(__file__).parent / descriptor_fname
if not IO_DESCRIPTOR_JSON.exists():
    raise EnvironmentError("Cannot find the boutiques descriptor to construct the CLI")

def main():
    """Console script for bids_statsmodels_design_synthesizer."""
    desc = json.load(open(IO_DESCRIPTOR_JSON))
    p = PrettyPrinter(desc)
    user_args = p.parser.parse_args()


    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover""Main module."""
