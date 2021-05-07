FROM condaforge/mambaforge

COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt
COPY . /opt/bids_statsmodels_design_synthesizer
RUN cd /opt/bids_statsmodels_design_synthesizer; pip install -e .

# A more bids appy approach
#COPY bids_statsmodels_design_synthesizer/bids_statsmodels_design_synthesizer.py /run.py
#RUN chmod a+x /run.py

