# Adapted from https://learn.microsoft.com/en-us/python/api/overview/azure/ai-formrecognizer-readme?view=azure-python
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from os import walk

endpoint = os.environ['AZURE_FORMRECOGNIZER_ENDPOINT']
credential = AzureKeyCredential(os.environ['AZURE_FORMRECOGNIZER_KEY'])

print(f"endpoint: {endpoint}")
print(f"credential: {credential}")

document_analysis_client = DocumentAnalysisClient(endpoint, credential)


if os.path.exists("out") == False:
    os.mkdir("out")

with open(r"./out/output-formrecognizer.md", "w") as output_file:
    page = 1
    for (dirpath, dirnames, filenames) in walk('./img'):
        for file in filenames:
            if file.endswith('.png'):
                with open(f"img/{file}", "rb") as fd:
                    print(f"Parsing {file}...")
                    document = fd.read()
                    poller = document_analysis_client.begin_analyze_document("prebuilt-layout", document)
                    result = poller.result()
                    if len(result.paragraphs) > 0:
                        output_file.write(f"___\n(page {page})\n\n")
                        for paragraph in result.paragraphs:
                            output_file.write(paragraph.content + "\n\n")
                page += 1
    output_file.close()                    


