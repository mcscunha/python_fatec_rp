from django.db import models


# Create your models here.
class Professores(models.Model):
    # id_professor = models.AutoField(primary_key=True)
    professor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.professor
    
    
class Cursos(models.Model):
    # id_curso = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Dias(models.Model):
    # id_dias = models.AutoField(primary_key=True)
    dia_semana = models.CharField(max_length=50)

    def __str__(self):
        return self.dia_semana


class Periodos(models.Model):
    # id_periodo = models.AutoField(primary_key=True)
    periodo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.periodo
    
    
class Semestres(models.Model):
    # id_semestre = models.AutoField(primary_key=True)
    semestre = models.IntegerField()

    def __str__(self):
        return str(self.semestre)


class Disciplinas(models.Model):
    # id_disciplina = models.AutoField(primary_key=True)
    id_professor = models.ForeignKey(Professores, on_delete=models.DO_NOTHING)
    id_curso = models.ForeignKey(Cursos, on_delete=models.DO_NOTHING)
    id_periodo = models.ForeignKey(Periodos, on_delete=models.DO_NOTHING)
    id_semestre = models.ForeignKey(Semestres, on_delete=models.DO_NOTHING)
    disciplina = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    
    def __str__(self):
        return 'Curso: {} - Disciplina: {}'.format(Cursos, self.disciplina)


class Disponibilidades(models.Model):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    # id_disponibilidade = models.AutoField(primary_key=True)
    id_professor = models.ForeignKey(Professores, on_delete=models.DO_NOTHING)
    id_periodo = models.ForeignKey(Periodos, on_delete=models.DO_NOTHING)
    horario = models.IntegerField()
    sequencia = models.IntegerField()
    segunda = models.BooleanField(choices=TRUE_FALSE_CHOICES, verbose_name='Segunda-Feira')
    terca = models.BooleanField(choices=TRUE_FALSE_CHOICES, verbose_name='Terça-Feira')
    quarta = models.BooleanField(choices=TRUE_FALSE_CHOICES, verbose_name='Quarta-Feira')
    quinta = models.BooleanField(choices=TRUE_FALSE_CHOICES, verbose_name='Quinta-Feira')
    sexta = models.BooleanField(choices=TRUE_FALSE_CHOICES, verbose_name='Sexta-Feira')
    sabado = models.BooleanField(choices=TRUE_FALSE_CHOICES, verbose_name='Sábado')

    def __str__(self):
        # o ID_PROFESSOR e ID_PERIODO colocados aqui, exibem o NOME_DO_PROFESSOR e o DESCRICAO_DO_PERIODO
        # Assim como é exibido na tela na hora de cadastrar as disponibilidades
        return 'Professor: {} - Periodo: {}'.format(self.id_professor, self.id_periodo)
