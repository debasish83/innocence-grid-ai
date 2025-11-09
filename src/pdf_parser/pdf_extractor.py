from typing import List
import PyPDF2
import os

class PDFExtractor:
    def extract_text(self, path: str) -> str:
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            parts = []
            for page in reader.pages:
                try:
                    parts.append(page.extract_text() or "")
                except Exception:
                    parts.append("")
            return "\n".join(parts)

    def chunk(self, text: str, max_chars: int) -> List[str]:
        chunks = []
        current = []
        size = 0
        for line in text.splitlines():
            line_len = len(line) + 1
            if size + line_len > max_chars and current:
                chunks.append("\n".join(current))
                current = [line]
                size = line_len
            else:
                current.append(line)
                size += line_len
        if current:
            chunks.append("\n".join(current))
        return chunks
