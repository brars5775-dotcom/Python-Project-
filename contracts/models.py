from django.db import models


class Document(models.Model):
    file = models.FileField(upload_to='contracts/')
    filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename


class ExtractedClause(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='clauses'
    )

    clause_type = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.clause_type


class RiskFlag(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='risks'
    )

    risk_type = models.CharField(max_length=100)
    risk_score = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.risk_type