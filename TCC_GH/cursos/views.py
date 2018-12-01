from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from grade_horario.models import Cursos
from .cur_form import Cad_Cursos_Form


# Create your views here.
@login_required
def list_cursos(request):
    curs = Cursos.objects.all()

    # terceiro parametro abaixo: {'NOME_VARIAVEL_HTML': objeto}
    return render(request, 'cur_list_cursos.html', {'curs': curs})


@login_required
def ins_cur(request):
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Cursos_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_cursos')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'cur_form.html', {'form': form})


@login_required
def upd_curso(request, id):
    dados = get_object_or_404(Cursos, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Cursos_Form(request.POST or None, instance=dados)
    if form.is_valid():
        form.save()
        return redirect('list_cursos')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'cur_form.html', {'form': form})


@login_required
def del_curso(request, id):
    dados = get_object_or_404(Cursos, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Cursos_Form(request.POST or None, instance=dados)
    if request.method == 'POST':
        dados.delete()
        return redirect('list_cursos')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'conf_del_curso.html', {'dados': dados})
