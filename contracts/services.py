from .models import ExtractedClause, RiskFlag


def parse_contract(document, text):
    clauses = []

    text = text.lower()

    # Detect termination-related clauses
    if "terminat" in text:
        clauses.append(
            ExtractedClause.objects.create(
                document=document,
                clause_type="Termination",
                content="Termination clause detected"
            )
        )

    # Detect confidentiality clauses
    if "confidential" in text:
        clauses.append(
            ExtractedClause.objects.create(
                document=document,
                clause_type="Confidentiality",
                content="Confidentiality clause detected"
            )
        )

    # Detect liability risks
    if "unlimited liability" in text:
        RiskFlag.objects.create(
            document=document,
            risk_type="Liability",
            risk_score=0.9,
            description="Unlimited liability detected"
        )

    return clauses