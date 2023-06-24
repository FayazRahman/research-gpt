import loopgpt
import openai
import os

# openai.api_type = "azure"
# openai.api_base = "https://loopgpt-azure-openai.openai.azure.com/"
# openai.api_version = "2023-03-15-preview"
# openai.api_key = os.getenv("AZURE_OPENAI_KEY")

from loopgpt.models import AzureOpenAIModel, OpenAIModel
from loopgpt.embeddings import AzureOpenAIEmbeddingProvider, OpenAIEmbeddingProvider

# model = AzureOpenAIModel("loop-gpt-35-turbo")
# emb = AzureOpenAIEmbeddingProvider("loop-text-embedding-ada-002")
model = OpenAIModel()
emb = OpenAIEmbeddingProvider()

loopgpt.set_aifunc_args(model=model, embedding_provider=emb)
