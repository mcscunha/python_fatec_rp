# -*- coding: utf-8 -*-

from django.forms import ModelForm
from grade_horario.models import Disciplinas


class Cad_Disc_Form(ModelForm):
    class Meta:
        model = Disciplinas
        fields = [
            'id_professor',
            'id_curso',
            'id_periodo',
            'id_semestre',
            'disciplina',
            'carga_horaria'
        ]
