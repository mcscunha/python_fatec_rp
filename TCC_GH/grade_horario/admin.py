from django.contrib import admin
from .models import Professores
from .models import Cursos
from .models import Periodos
from .models import Semetres
from .models import Dias
from .models import Disciplinas
from .models import Disponibilidades




# Register your models here.
admin.site.register(Professores)
admin.site.register(Cursos)