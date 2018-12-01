# -*- coding: utf-8 -*-

from django.forms import ModelForm
from grade_horario.models import Semestres


class Cad_Sem_Form(ModelForm):
    class Meta:
        model = Semestres
        fields = ['id_semestre', 'semestre']
