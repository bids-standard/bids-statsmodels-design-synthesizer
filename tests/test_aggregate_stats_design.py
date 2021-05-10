#!/usr/bin/env python

"""Tests for `bids_statsmodels_design_synthesizer` package."""

import pytest
import subprocess as sp
from pathlib import Path

SYNTHESIZER = "aggregate_stats_design.py"
from bids_statsmodels_design_synthesizer import aggregate_stats_design as synth_mod

# from bids_statsmodels_design_synthesizer import Path(SYNTHESIZER).stem as synth_mod


def test_cli_help():
    with pytest.raises(sp.CalledProcessError):
        output = sp.check_output([SYNTHESIZER, "-h"])
    with pytest.raises(sp.CalledProcessError):
        output = sp.check_output([SYNTHESIZER, "--non-existent"])


def test_design_aggregation_function():
    user_args = {
        "BIDS_DIR": "data/ds000003",
        "OUTPUT_DIR": "outputdir",
        "MODEL": "model-001_smdl.json",
        "PARTICIPANT_LABEL": None,
        "SESSION_LABEL": None,
    }

    synth_mod.main(user_args)


def test_minimal_cli_functionality():
    """
    We roughly want to implement the equivalent of the following:
    from bids.analysis import Analysis
    from bids.layout import BIDSLayout

    layout = BIDSLayout("data/ds000003")
    analysis = Analysis(model="data/ds000003/models/model-001_smdl.json",layout=layout)
    analysis.setup()

    more specifically we want to reimplement this line
    https://github.com/bids-standard/pybids/blob/b6cd0f6787230ce976a374fbd5fce650865752a3/bids/analysis/analysis.py#L282
    """
    bids_dir = Path(__file__).parent / "data/ds000003"
    model = "model-001_smdl.json"

    cmd = f"""
        {SYNTHESIZER}
            --model {model}
            {bids_dir}
            output_min_cli_test
         """
    output = sp.check_output(cmd.split())


@pytest.mark.xfail(reason="Container not setup for boutiques yet")
def test_minimal_cli_functionality_using_boutiques():
    """This might be nice to do. boutiques sets /bin/sh as the entrypoint for the contain to /bin/sh so this should be tweaked to have the conda env and the pip installed package working correctly"""
    boutiques_dir = Path(__file__).parent.parent / "boutiques"
    cmd = f"""
        bosh
            exec
            launch
            {boutiques_dir}/bids-app-bids-statsmodels-design-synthesizer.json
            {boutiques_dir}/invocation.json
        """
    output = sp.check_output(cmd.split())
