---
title: OCR & Document AI
description: OCR engines, document layout analysis, and PDF parsing tooling for reading text from images and documents.
tags: [machine-learning, vision, llm]
---

# OCR & Document AI

Fetch when the target reads text from images or parses document layouts. Each entry is one line and a documentation entry point; fetch model and pipeline details from the entry point, never from memory. No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| PaddleOCR | multilingual OCR and document parsing toolkit | <https://www.paddleocr.ai/> |
| Tesseract | the long-standing OCR engine (system install) | <https://tesseract-ocr.github.io/> |
| EasyOCR | ready-to-use OCR in 80+ languages | <https://github.com/JaidedAI/EasyOCR> |
| docTR | deep-learning document text recognition | <https://mindee.github.io/doctr/> |
| Surya | OCR, layout, and reading order for documents | <https://github.com/datalab-to/surya> |
| LayoutParser | document layout analysis toolkit | <https://layout-parser.github.io/> |
| Unstructured | ingest and chunk documents for LLM pipelines | <https://docs.unstructured.io/> — llms.txt: <https://docs.unstructured.io/llms.txt> |
| Docling | document conversion to structured formats | <https://docling-project.github.io/docling/> |
| PyMuPDF | fast PDF parsing and rendering | <https://pymupdf.readthedocs.io/> — llms.txt: <https://pymupdf.readthedocs.io/llms.txt> |
| pdfplumber | PDF text and table extraction | <https://github.com/jsvine/pdfplumber> |

## Gotchas

- Tesseract installs from system packages, not pip — fetch install guidance from its docs.
