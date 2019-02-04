# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import Professores

class Cad_Prof_Form(ModelForm):
    class Meta:
        model = Professores
        fields = ['professor']
