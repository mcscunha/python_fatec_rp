# -*- coding: utf-8 -*-

from django.forms import ModelForm
from grade_horario.models import Disponibilidades


class Cad_Disp_Form(ModelForm):
    class Meta:
        model = Disponibilidades
        fields = [
            'id_professor',
            'id_periodo',
            'horario',
            'sequencia',
            'segunda',
            'terca',
            'quarta',
            'quinta',
            'sexta',
            'sabado',
        ]
