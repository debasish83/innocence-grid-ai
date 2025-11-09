from typing import Dict, List
from .pdf_extractor import PDFExtractor
from .gemini_client import GeminiClient

class PDFAnalyzer:
    def __init__(self, client: GeminiClient, extractor: PDFExtractor, max_chars_per_chunk: int):
        self.client = client
        self.extractor = extractor
        self.max_chars = max_chars_per_chunk

    def summarize_pdf(self, path: str) -> str:
        text = self.extractor.extract_text(path)
        chunks = self.extractor.chunk(text, self.max_chars)
        summaries = [self.client.summarize(c, 120) for c in chunks]
        joined = "\n".join(summaries)
        return self.client.summarize(joined, 200)

    def key_points(self, path: str) -> str:
        text = self.extractor.extract_text(path)
        return self.client.extract_key_points(text)
    
    def innocence_score(self, path: str) -> str:
        text = self.extractor.extract_text(path)
        return self.client.extract_innocence_score(text)
    
    def qa(self, path: str, question: str) -> str:
        text = self.extractor.extract_text(path)
        return self.client.answer(text, question)

    def multi_pdf_compare(self, paths: List[str]) -> str:
        docs = []
        for p in paths:
            t = self.extractor.extract_text(p)
            docs.append(f"File: {p}\n{t[:4000]}")
        prompt = "Compare these documents. Summarize similarities and differences:\n\n" + "\n\n---\n\n".join(docs)
        return self.client.generate([prompt])
