from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from grade_horario.models import Disponibilidades
from .disp_form import Cad_Disp_Form


# Create your views here.
@login_required
def list_disp(request):
    dados = Disponibilidades.objects.all()

    # terceiro parametro abaixo: {'NOME_VARIAVEL_HTML': objeto}
    return render(request, 'list_disp.html', {'dados': dados})


@login_required
def ins_disp(request):
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Disp_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_disp')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'disp_form.html', {'form': form})


@login_required
def upd_disp(request, id):
    dados = get_object_or_404(Disponibilidades, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Disp_Form(request.POST or None, instance=dados)
    if form.is_valid():
        form.save()
        return redirect('list_disp')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'disp_form.html', {'form': form})


@login_required
def del_disp(request, id):
    dados = get_object_or_404(Disponibilidades, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    # form = Cad_Sem_Form(request.POST or None, instance=dados)
    if request.method == 'POST':
        dados.delete()
        return redirect('list_disp')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'conf_del_disp.html', {'dados': dados})
