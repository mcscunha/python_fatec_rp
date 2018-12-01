# -*- coding: utf-8 -*-

from django.forms import ModelForm
from grade_horario.models import Periodos


class Cad_Per_Form(ModelForm):
    class Meta:
        model = Periodos
        fields = ['id_periodo', 'periodo']
