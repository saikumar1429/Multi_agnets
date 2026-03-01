from transformers import pipeline
from .base_agent import BaseAgent

class SentimentAgent(BaseAgent):
    def __init__(self):
        super().__init__("SentimentAnalyzer")
        self.analyzer = pipeline("sentiment-analysis")

    def process(self, text, context=None):
        return self.analyzer(text)