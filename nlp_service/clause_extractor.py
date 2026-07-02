class ClauseExtractor:

    CLAUSE_KEYWORDS = {
        "Confidentiality": [
            "confidential",
            "non-disclosure",
            "trade secret"
        ],
        "Termination": [
            "termination",
            "terminate",
            "terminated"
        ],
        "Payment Terms": [
            "payment",
            "invoice",
            "fees"
        ],
        "Indemnification": [
            "indemnify",
            "hold harmless",
            "liability"
        ],
        "Governing Law": [
            "governing law",
            "jurisdiction"
        ]
    }

    def __init__(self):
        self.nlp_service = NLPService()

    def extract(self, text):

        clauses = {}

        sentences = self.nlp_service.get_sentences(text)

        for category, keywords in self.CLAUSE_KEYWORDS.items():

            clauses[category] = []

            for sentence in sentences:

                if any(keyword.lower() in sentence.lower()
                       for keyword in keywords):
                    clauses[category].append(sentence)

        return clauses