# -*- coding: utf-8 -*-

from django.forms import ModelForm
from grade_horario.models import Dias


class Cad_Dias_Form(ModelForm):
    class Meta:
        model = Dias
        fields = ['dia_semana']
