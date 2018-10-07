from django.shortcuts import render, redirect, get_object_or_404
from .models import Professores
from .prof_form import Cad_Prof_Form

# Create your views here.
def gh_list_prof(request):
    profs = Professores.objects.all()
    
    # terceiro parametro abaixo: {'NOME_VARIAVEL_HTML': objeto}
    return render(request, 'gh_list_prof.html', {'profs': profs})

def gh_cad_prof(request):
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Prof_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gh_list_prof')
    
    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'prof_form.html', {'form': form})

def gh_upd_prof(request, id):
    dados = get_object_or_404(Professores, pk=id)
    
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Prof_Form(request.POST or None, instance=dados)
    if form.is_valid():
        form.save()
        return redirect('gh_list_prof')
    
    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'prof_form.html', {'form': form})

def gh_del_prof(request, id):
    dados = get_object_or_404(Professores, pk=id)
    
    # Redirecionar para ModelForms do Django para montar o form
    form = Cad_Prof_Form(request.POST or None, instance=dados)
    if request.method == 'POST':
        dados.delete()
        return redirect('gh_list_prof')
    
    # Redirecionar para pagina HTML se retornar invalida
    return render(request, 'prof_conf_form.html', {'dados': dados})