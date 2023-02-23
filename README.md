# PDF To Text

This project converts a multi-page PDF to png images, then offers two ways to read the text off of those pages. The extracted text is saved in a separate markdown file.

## Method 1: Tesseract

[Tesseract](https://tesseract-ocr.github.io/) is a free, open source library for reading text off of images. Using Tesseract requires installing the tool on your computer separately.

## Method 2: Azure Form Recognizer

Azure Form Recognizer is Microsoft's OCR offering, part of its Cognitive Services package. In my experience, Form Recognizer has higher accuracy than Tesseract. You will need to create an Azure account and a Form Recognizer resource to use this service ([Instructions](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-formrecognizer-readme?view=azure-python#create-a-cognitive-services-or-form-recognizer-resource)).

Form Recognizer is not free, but its pricing is very reasonable ([pricing chart](https://azure.microsoft.com/en-in/pricing/details/form-recognizer/)). Azure gives you 500 pages per month for free, then $1.50 per 1,000 pages after that.

## Installation

1. Install [Tesseract](https://tesseract-ocr.github.io/) from that tool's website.
2. Install a few python packages:

```
pip install pymupdf
pip install pytesseract
pip install azure-ai-formrecognizer
```

3. (If using Form Recognizer), set two environment variables: `AZURE_FORMRECOGNIZER_ENDPOINT` and `AZURE_FORMRECOGNIZER_KEY`.

## Instructions

1. Copy a pdf file to the project directory.
2. Change the `pdffile` variable on convert.py:4 to match the name of the file (I'm too lazy to get this to use command-line arguments)
3. Run `python convert.py`; this will split the PDF into images and put them in the `img` directory.
4. The next steps depend on which OCR tool you would like to use:
   - Tesseract: run `python tesseract.py`; the output will be saved to a file named `output-tesseract.md` in the "out" directory
   - Azure Form Recognizer: (Make sure you set the `AZURE_FORMRECOGNIZER_ENDPOINT` and `AZURE_FORMRECOGNIZER_KEY` environment variables). Run `python form_recognizer.py`; the output will be saved to a file named `output-formrecognizer.md` in the "out" directory.