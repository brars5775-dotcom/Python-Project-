import spacy

class NLPProcessor:
    """
    Singleton spaCy model loader.
    """

    _nlp = None

    @classmethod
    def get_model(cls):
        if cls._nlp is None:
            cls._nlp = spacy.load("en_core_web_sm")
        return cls._nlp