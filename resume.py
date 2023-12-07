from pathlib import Path
from llama_index import download_loader,VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

PDFReader = download_loader("PDFReader")

loader = PDFReader()
documents = loader.load_data(file=Path('data/resume.pdf'))
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("Tell me about this candidate based off of their resume.")
print(response)