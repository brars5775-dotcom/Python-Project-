from utils.pdf_utils import PDFUtils
from services.clause_extractor import ClauseExtractor
from services.risk_analyzer import RiskAnalyzer

pdf_path = "sample_contract.pdf"

text = PDFUtils.extract_text(pdf_path)

clause_extractor = ClauseExtractor()
risk_analyzer = RiskAnalyzer()

clauses = clause_extractor.extract(text)
risks = risk_analyzer.analyze(text)

print("Clauses:")
print(clauses)

print("\nRisks:")
print(risks)