# %%

from langchain_community.document_loaders import PyPDFLoader

file_path = (
    "./data/drawings/Sloping Site - Proposal.pdf"
)
loader = PyPDFLoader(file_path)
pages = loader.load()


# %%

print(pages[1].page_content)


# %%

print(pages[2])

# %%

