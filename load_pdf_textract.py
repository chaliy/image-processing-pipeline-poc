# %%

from textractcaller import call_textract

textract_json = call_textract(
    input_document="s3://image-processing-pipeline-poc/drawings/Sloping Site - Proposal.pdf"
)


# %%

import json

json.dumps(textract_json)


# %%
