from django.db import models

# Create your models here.
class Professores(models.Model):
    id_professor = models.AutoField(primary_key=True)
    professor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.professor
    
    
class Cursos(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Dias(models.Model):
    id_dias = models.AutoField(primary_key=True)
    dia_semana = models.CharField(max_length=50)

    def __str__(self):
        return self.dia_semana


class Periodos(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    periodo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.periodo
    
    
class Semetres(models.Model):
    id_semestre = models.AutoField(primary_key=True)
    semetre = models.IntegerField()        

    def __str__(self):
        return self.semestre


class Disciplinas(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    id_professor = models.ForeignKey(Professores, on_delete=models.DO_NOTHING)
    id_curso = models.ForeignKey(Cursos, on_delete=models.DO_NOTHING)
    id_periodo = models.ForeignKey(Periodos, on_delete=models.DO_NOTHING)
    id_semestre = models.ForeignKey(Semetres, on_delete=models.DO_NOTHING)
    disciplina = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    
    def __str__(self):
        return self.id_curso + ' - ' + self.disciplina
    
class Disponibilidades(models.Model):
    id_disponibilidade = models.AutoField(primary_key=True)
    id_professor = models.ForeignKey(Professores, on_delete=models.DO_NOTHING)
    id_periodo = models.ForeignKey(Periodos, on_delete=models.DO_NOTHING)
    id_dias = models.ForeignKey(Dias, on_delete=models.DO_NOTHING)
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.DO_NOTHING)
    id_curso = models.ForeignKey(Cursos, on_delete=models.DO_NOTHING)
    id_semestre = models.ForeignKey(Semetres, on_delete=models.DO_NOTHING)
    horario = models.IntegerField()
    carga_horaria = models.IntegerField()
    
    def __str__(self):
        return self.horario
