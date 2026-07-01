import spacy


class NLPService:
    """
    Handles all NLP operations using spaCy.
    """

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process(self, text):
        """
        Convert raw text into a spaCy document.
        """
        return self.nlp(text)

    def get_sentences(self, text):
        """
        Extract sentences from text.
        """
        doc = self.process(text)

        return [sentence.text.strip() for sentence in doc.sents]

    def get_named_entities(self, text):
        """
        Extract named entities.
        """
        doc = self.process(text)

        entities = []

        for ent in doc.ents:
            entities.append({
                "text": ent.text,
                "label": ent.label_
            })

        return entities

    def tokenize(self, text):
        """
        Tokenize text.
        """
        doc = self.process(text)

        return [token.text for token in doc]

    def extract_nouns(self, text):
        """
        Extract noun phrases.
        """
        doc = self.process(text)

        return [chunk.text for chunk in doc.noun_chunks]