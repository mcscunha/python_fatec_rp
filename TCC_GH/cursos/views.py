from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from grade_horario.models import Cursos
from .cur_form import Cad_Cursos_Form


# Create your views here.
@login_required
def list_cursos(request):
    curs = Cursos.objects.all()

    # terceiro parametro abaixo: {'NOME_VARIAVEL_HTML': objeto}
    return render(request, 'cur_list_cursos.html', {'curs': curs})


@login_required
def cur_cad_cur(request):
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Cursos_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cur_list_cursos')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'cur_form.html', {'form': form})


@login_required
def gh_upd_prof(request, id):
    dados = get_object_or_404(Cursos, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Cursos_Form(request.POST or None, instance=dados)
    if form.is_valid():
        form.save()
        return redirect('cur_list_cursos')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'cur_form.html', {'form': form})


@login_required
def gh_del_prof(request, id):
    dados = get_object_or_404(Cursos, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Cursos_Form(request.POST or None, instance=dados)
    if request.method == 'POST':
        dados.delete()
        return redirect('cur_list_cursos')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'list_links', {'dados': dados})
