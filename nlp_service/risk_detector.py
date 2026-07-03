class RiskAnalyzer:

    HIGH_RISK_TERMS = {
        "High": [
            "without notice",
            "unlimited liability",
            "sole discretion",
            "perpetual"
        ],

        "Medium": [
            "30 days",
            "arbitration",
            "exclusive jurisdiction"
        ],

        "Low": [
            "reasonable notice"
        ]
    }

    def __init__(self):
        self.nlp_service = NLPService()

    def analyze(self, text):

        sentences = self.nlp_service.get_sentences(text)

        risks = []

        for sentence in sentences:

            for severity, patterns in self.HIGH_RISK_TERMS.items():

                for pattern in patterns:

                    if pattern.lower() in sentence.lower():

                        risks.append({
                            "severity": severity,
                            "pattern": pattern,
                            "sentence": sentence
                        })

        return risks