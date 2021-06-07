# ELI
Extracting entities and relations from medical abstracts

This repository contains the code necessary to run a pre-trained version of the models described in our publication [Trialstreamer: Mapping and Browsing Medical Evidence in Real-Time](https://www.aclweb.org/anthology/2020.acl-demos.9/).

Processing your own documents:
* Download the pre-trained models [here]()
* Move the model checkpoints into the corresponding directories in this repo
* Save your documents as a `.json` file that contains a list of records in the format `{"pmid": XXX, "text": "..."}`
* `cd` to `scripts` and run `python run_pipeline.py $INPUT_FNAME $OUT_FNAME`
