import google.generativeai as genai
from typing import List

class GeminiClient:

    def __init__(self, api_key: str, model: str):
        genai.configure(api_key=api_key)
        self.innocence_prompt = """You are an expert legal analyst specialized in detecting innocence claims in court transcripts.
Your task is to analyze inmate statements and identify any signals suggesting innocence claims.

## Signal Types to Detect:

1. **Explicit Signals**: Direct statements of innocence
   - Examples: "I did not commit this crime", "I'm innocent", "I didn't do it"

2. **Implicit Signals**: Maintained innocence despite negative outcomes
   - Examples: Refusing plea deals, consistently maintaining innocence over time, accepting harsher sentences rather than admit guilt

3. **Contextual Signals**: Evidence of problematic case circumstances
   - Examples: Mentions of coerced confessions, recantations, witness recantations, evidence gaps, alibi evidence, prosecutorial misconduct

4. **Bias Language**: Institutional language suggesting bias against maintaining innocence
   - Examples: "lack of insight", "failure to take responsibility", "minimization", "denial"

## Output Format:

Return a JSON array of innocence claims. Each claim must have:
- "signal_type": One of: "explicit", "implicit", "contextual", "bias_language"
- "explanation": A brief explanation of why this is classified as this signal type
"""
        self.generation_config = genai.GenerationConfig(
            temperature=1.0
        )
        self.model = genai.GenerativeModel(model, generation_config=self.generation_config)
    
    def generate(self, parts: List[str]) -> str:
        resp = self.model.generate_content(parts)
        return resp.text

    def summarize(self, text: str, words: int = 200) -> str:
        prompt = f"Summarize the following document in about {words} words:\n{text}"
        return self.generate([prompt])

    def extract_key_points(self, text: str) -> str:
        prompt = f"Extract key bullet points from:\n{text}"
        return self.generate([prompt])
    
    def extract_innocence_score(self, text: str) -> str:
        prompt = f"inmate statements:\n{text}\n\n{self.innocence_prompt}\n"
        return self.generate([prompt])
    
    def answer(self, text: str, question: str) -> str:
        prompt = f"Context:\n{text}\n\nQuestion: {question}\nAnswer:"
        return self.generate([prompt])
    
