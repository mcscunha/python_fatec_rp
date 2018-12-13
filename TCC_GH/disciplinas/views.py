from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from grade_horario.models import Disciplinas
from .disc_form import Cad_Disc_Form


# Create your views here.
@login_required
def list_disc(request):
    dados = Disciplinas.objects.all()

    # terceiro parametro abaixo: {'NOME_VARIAVEL_HTML': objeto}
    return render(request, 'list_disc.html', {'dados': dados})


@login_required
def ins_disc(request):
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Disc_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_disc')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'disc_form.html', {'form': form})


@login_required
def upd_disc(request, id):
    dados = get_object_or_404(Disciplinas, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Disc_Form(request.POST or None, instance=dados)
    if form.is_valid():
        form.save()
        return redirect('list_disc')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'disc_form.html', {'form': form})


@login_required
def del_disc(request, id):
    dados = get_object_or_404(Disciplinas, pk=id)

    # Redirecionar para ModelForms do Django para montar o form
    # form = Cad_Sem_Form(request.POST or None, instance=dados)
    if request.method == 'POST':
        dados.delete()
        return redirect('list_disc')

    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'conf_del_disc.html', {'dados': dados})
