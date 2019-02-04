# -*- coding: utf-8 -*-

from django.forms import ModelForm
from grade_horario.models import Cursos


class Cad_Cursos_Form(ModelForm):
    class Meta:
        model = Cursos
        fields = ['nome']
