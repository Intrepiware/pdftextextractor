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
    for file in os.listdir('./img'):
        if os.path.isfile(f"./img/{file}") and file.endswith('.png'):
            with open(f"img/{file}", "rb") as fd:
                print(f"Parsing {file}...")
                document = fd.read()
                poller = document_analysis_client.begin_analyze_document("prebuilt-document", document)
                result = poller.result()
                for kv_pair in result.key_value_pairs:
                    if kv_pair.key and kv_pair.value:
                        print("* Key '{}': Value: '{}'".format(kv_pair.key.content, kv_pair.value.content))
                    else:
                        print("* Key '{}': Value:".format(kv_pair.key.content))
            page += 1
            break
    output_file.close()                    


