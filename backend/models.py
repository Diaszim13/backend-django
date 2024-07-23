from django.db import models

class user (models.Model):
    nome = models.charField(max_length=300)

    def __str__(self):
        return self.name
    