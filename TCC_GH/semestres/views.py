from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from grade_horario.models import Semestres
from .sem_form import Cad_Sem_Form


# Create your views here.
@login_required
def list_sem(request):
    dados = Semestres.objects.all()

    # terceiro parametro abaixo: {'NOME_VARIAVEL_HTML': objeto}
    return render(request, 'list_sem.html', {'dados': dados})


@login_required
def ins_sem(request):
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Sem_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_sem')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'sem_form.html', {'form': form})


@login_required
def upd_sem(request, id):
    dados = get_object_or_404(Semestres, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Sem_Form(request.POST or None, instance=dados)
    if form.is_valid():
        form.save()
        return redirect('list_sem')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'sem_form.html', {'form': form})


@login_required
def del_sem(request, id):
    dados = get_object_or_404(Semestres, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    # form = Cad_Sem_Form(request.POST or None, instance=dados)
    if request.method == 'POST':
        dados.delete()
        return redirect('list_sem')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'conf_del_sem.html', {'dados': dados})
