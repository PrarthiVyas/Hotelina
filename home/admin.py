from django.contrib import admin

from .models import sign
from .models import City
from .models import Bvn
from .models import baroda
from .models import Rooms
from .models import Booking
from .models import Restaura
# Register your models here.

admin.site.register(sign)
admin.site.register(City)
admin.site.register(Bvn)
admin.site.register(baroda)
admin.site.register(Rooms)
admin.site.register(Booking)
admin.site.register(Restaura)
