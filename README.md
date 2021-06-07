# ELI
Extracting entities and relations from medical abstracts

This repository contains the code necessary to run a pre-trained version of the models described in our publication [Trialstreamer: Mapping and Browsing Medical Evidence in Real-Time](https://www.aclweb.org/anthology/2020.acl-demos.9/).

Further details about the models and implementations are published in [Understanding Clinical Trial Reports: Extracting Medical Entities and Their Relations](https://arxiv.org/pdf/2010.03550.pdf).

Processing your own documents:
* Download the pre-trained models [here](https://drive.google.com/file/d/1nQRVRhSri3scktTFlEPmvmbdbPFc9ten/view?usp=sharing)
* Move the model checkpoints into the corresponding directories in this repo
* Save your documents as a `.json` file that contains a list of records in the format `{"pmid": XXX, "text": "..."}`
* `cd` to `scripts` and run `python run_pipeline.py $INPUT_FILE_NAME $OUT_FILE_NAME`
