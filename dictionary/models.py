import uuid
from django.db import models


class Word(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    word = models.CharField(max_length=100)

    def __str__(self):
        return str(self.word)


class WordMeaning(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    word = models.ForeignKey("dictionary.Word", on_delete=models.CASCADE)
    meaning = models.TextField(max_length=255)
    priority = models.IntegerField(null=True)

    def __str__(self):
        return str(self.word)

    
    
    
