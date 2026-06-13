from rest_framework import serializers
from .models import Document, ExtractedClause, RiskFlag


class ExtractedClauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedClause
        fields = "__all__"


class RiskFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFlag
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    clauses = ExtractedClauseSerializer(many=True, read_only=True)
    risks = RiskFlagSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = "__all__"