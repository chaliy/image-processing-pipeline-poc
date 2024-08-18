# %%

# - AWS Env variables
# - s3://image-processing-pipeline-poc/drawings/Sloping Site - Proposal.pdf

# %%

from langchain_community.document_loaders import AmazonTextractPDFLoader

loader = AmazonTextractPDFLoader(
    "s3://image-processing-pipeline-poc/drawings/Sloping Site - Proposal.pdf"
)
pages = loader.load()


# %%

print(pages[1].page_content)


# %%

print(pages[2])

# %%

