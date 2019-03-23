from django.contrib import admin

from .models import (Passager, Bus, Route, Travel, Passage, Trade)

# Register your models here.

admin.site.register(Passager)
admin.site.register(Passage)
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Travel)
admin.site.register(Trade)

