# Automated Contract Parsing & Risk Extraction Engine

> Django + spaCy system that extracts entities and flags risky clauses from legal PDFs

### Project Objective
This project automates the review of legal contracts. Users upload PDF contracts, the system extracts text, identifies key information such as company names, dates, and jurisdictions, and flags potentially risky clauses for review.

### Technology Stack
| COMPONENTS | TOOLS |
| --- | --- |
| Programming language | Python |
| Backend framework | Django |
| API Development | Django REST Framework |
| Database | SQLite for development, PostgreSQL for final submission |
| PDF Text Extraction | PyMuPDF |
| NLP | spaCy |
| API Testing | Postman |
| Version Control | GitHub |

### 6. System Modules 
1.Document Upload Module: Handles PDF file ingestion and validation
2.PDF Processing Module: Extracts raw text from uploaded documents
3.NLP Processing Module: Runs spaCy pipeline for entity recognition
4.Risk Analysis Engine: Identifies and flags risky clauses based on rules
5.Database Layer: Stores contracts, entities, and risk assessments 
6.API Layer: Exposes DRF endpoints for upload, processing, and retrieval
7.Admin Dashboard: UI for manual review and system monitoring

### Week-wise Plan
Week 1 –
👩‍💻 Member 1 (Backend)
Understand requirements
Create workflow diagram
Set up Django project
Install Django REST Framework
Configure project structure

👨‍💻 Member 2 (Database)
Analyze contract data requirements
Design database schema
Create ER diagram
Define tables and relationships

👨‍💻 Member 3 (NLP)
Research contract clauses
Study spaCy
Research contract risk categories
Study PyMuPDF

👩‍💻 Member 4 (GitHub & Testing)
Create GitHub repository
Add team members
Create branches
Create README.md
Set up project documentation structure


Week 2: PDF text extraction pipeline
Week 3: NLP integration and risk detection
Week 4: API serialization, testing, documentation, admin dashboard



### Expected Output
JSON response containing extracted entities, contract details, and risk flags.

### Benefits
Reduces review time, improves accuracy, automates repetitive work, and provides hands-on experience with backend development and NLP.

### Version Control
This project uses GitHub for source code management, issue tracking, and collaboration.
