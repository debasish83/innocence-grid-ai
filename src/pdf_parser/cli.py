import argparse
from .config import GEMINI_API_KEY, DEFAULT_MODEL, MAX_CHARS_PER_CHUNK
from .gemini_client import GeminiClient
from .pdf_extractor import PDFExtractor
from .pdf_analyzer import PDFAnalyzer
import sys

def build():
    if not GEMINI_API_KEY:
        print("Missing GEMINI_API_KEY in environment (.env).", file=sys.stderr)
        sys.exit(1)
    client = GeminiClient(GEMINI_API_KEY, DEFAULT_MODEL)
    extractor = PDFExtractor()
    return PDFAnalyzer(client, extractor, MAX_CHARS_PER_CHUNK)

def main():
    parser = argparse.ArgumentParser(prog="pdf-parser")
    sub = parser.add_subparsers(dest="cmd")

    s = sub.add_parser("summarize")
    s.add_argument("pdf")

    k = sub.add_parser("keypoints")
    k.add_argument("pdf")

    i = sub.add_parser("innocence-score")
    i.add_argument("pdf")
    
    q = sub.add_parser("ask")
    q.add_argument("pdf")
    q.add_argument("question")

    c = sub.add_parser("compare")
    c.add_argument("pdfs", nargs="+", help="Two or more PDFs")

    args = parser.parse_args()
    analyzer = build()

    if args.cmd == "summarize":
        print(analyzer.summarize_pdf(args.pdf))
    elif args.cmd == "innocence-score":
        print(analyzer.innocence_score(args.pdf))
    elif args.cmd == "keypoints":
        print(analyzer.key_points(args.pdf))
    elif args.cmd == "ask":
        print(analyzer.qa(args.pdf, args.question))
    elif args.cmd == "compare":
        if len(args.pdfs) < 2:
            print("Need at least two PDFs.", file=sys.stderr)
            sys.exit(1)
        print(analyzer.multi_pdf_compare(args.pdfs))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
