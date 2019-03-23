from django.db import models

class Route(models.Model):
    origem = models.CharField(max_length=50,)
    destiny = models.CharField(max_length=50)

    def __str__(self):
        return f"Origem: {self.origem}\nDestiny: {self.destiny}"