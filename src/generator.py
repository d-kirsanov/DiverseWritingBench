import os
from litellm import completion # Supports OpenRouter, Local, etc.

class StyleGenerator:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_samples(self, domain_data, k=5):
        """Generates k independent attempts for a single domain."""
        prompt = self._build_prompt(domain_data)
        samples = []
        
        for _ in range(k):
            response = completion(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.9 # High temperature is crucial for Max-K!
            )
            samples.append(response.choices[0].message.content)
            
        return samples

    def _build_prompt(self, domain):
        return f"Style Master: {domain['author']}\n"
               
