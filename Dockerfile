FROM condaforge/mambaforge

COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt
COPY bids_statsmodels_design_synthesizer/bids_statsmodels_design_synthesizer.py /run.py
RUN chmod a+x /run.py

