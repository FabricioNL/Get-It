from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        newNote = Note(title=title, content=content)
        newNote.save()
        return redirect('index')
    else:

        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})

def update(request, id):
    note = Note.objects.get(id=id)
    return render(request, 'notes/noteEdit.html', {'note': note})

def delete(request):
    if request.method == 'POST':
        id_card = int(request.POST.get('id_card'))
        card = Note.objects.get(id=id_card)
        card.delete()
        return redirect('index')
    else:

        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})

def save(request):
    print(request)
    title = request.POST.get('title')
    content = request.POST.get('content')
    ID = request.POST.get('id_card')
    # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
    updateNote = Note.objects.get(id=int(ID))
    updateNote.title = title
    updateNote.content = content    
    updateNote.save()
    return redirect('index')
