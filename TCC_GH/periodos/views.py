from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from grade_horario.models import Periodos
from .per_form import Cad_Per_Form


# Create your views here.
@login_required
def list_per(request):
    dados = Periodos.objects.all()

    # terceiro parametro abaixo: {'NOME_VARIAVEL_HTML': objeto}
    return render(request, 'list_per.html', {'dados': dados})


@login_required
def ins_per(request):
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Per_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_per')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'per_form.html', {'form': form})


@login_required
def upd_per(request, id):
    dados = get_object_or_404(Periodos, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Per_Form(request.POST or None, instance=dados)
    if form.is_valid():
        form.save()
        return redirect('list_per')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'per_form.html', {'form': form})


@login_required
def del_per(request, id):
    dados = get_object_or_404(Periodos, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Per_Form(request.POST or None, instance=dados)
    if request.method == 'POST':
        dados.delete()
        return redirect('list_per')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'conf_del_per.html', {'dados': dados})
