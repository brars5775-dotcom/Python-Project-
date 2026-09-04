from django.db import models


class Document(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extraction_timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["status"]),
        ]


class ExtractedClause(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="clauses"
    )
    clause_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["document"]),
        ]


class RiskFlag(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="risk_flags"
    )
    clause = models.ForeignKey(
        ExtractedClause,
        on_delete=models.CASCADE,
        related_name="risk_flags"
    )
    risk_type = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["document", "clause", "risk_type"],
                name="unique_risk_flag"
            )
        ]