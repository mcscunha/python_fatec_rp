from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from grade_horario.models import Dias
from .dia_form import Cad_Dias_Form


# Create your views here.
@login_required
def list_dias(request):
    dias = Dias.objects.all()

    # terceiro parametro abaixo: {'NOME_VARIAVEL_HTML': objeto}
    return render(request, 'list_dias.html', {'dias': dias})


@login_required
def ins_dia(request):
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Dias_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_dias')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'dia_form.html', {'form': form})


@login_required
def upd_dia(request, id):
    dados = get_object_or_404(Dias, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Dias_Form(request.POST or None, instance=dados)
    if form.is_valid():
        form.save()
        return redirect('list_dias')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'dia_form.html', {'form': form})


@login_required
def del_dia(request, id):
    dados = get_object_or_404(Dias, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Dias_Form(request.POST or None, instance=dados)
    if request.method == 'POST':
        dados.delete()
        return redirect('list_dias')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'conf_del_dia.html', {'dados': dados})
