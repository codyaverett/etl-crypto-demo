from django.db import models

class Network(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name