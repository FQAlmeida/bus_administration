from django.db import models
from .route import (Route)
from .bus import (Bus)

class Travel(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    route = models.ForeignKey(Route, verbose_name="Route", on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, verbose_name="Bus", on_delete=models.CASCADE)