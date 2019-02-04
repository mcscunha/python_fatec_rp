# Generated by Django 2.1.2 on 2019-02-04 00:07

from django.db import migrations


def carregar_sql_disciplina():
    sql_disciplina = open('grade_horario/sql/disciplinas.sql', 'r').read()
    return sql_disciplina


def limpar_tabela_disciplina():
    return 'DELETE FROM grade_horario_disciplinas'


class Migration(migrations.Migration):

    dependencies = [
        ('grade_horario', '0006_CargaInicial_Curso'),
    ]

    operations = [
        migrations.RunSQL(carregar_sql_disciplina(), limpar_tabela_disciplina())
    ]
