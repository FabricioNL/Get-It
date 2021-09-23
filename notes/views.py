from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tagInput = (str(request.POST.get('tag'))).upper()
        
        if Tag.objects.filter(tag = tagInput).exists():
            t = Tag.objects.get(tag = tagInput)
            newNote = Note(title=title, content=content, tag=t)
            newNote.save()
            

        else:
            newTag = Tag(tag=tagInput)
            newTag.save()

            # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
            newNote = Note(title=title, content=content, tag=newTag)
            newNote.save()

        #criando um conjunto de TAGS
        
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
        #se houver apenas uma note com a tag e for deletada, a tag é deletada também

        TAG = card.tag
        if len(Note.objects.filter(tag = TAG)) == 1:
            TAG.delete()
            #Tag.objects.all().delete() #usado apenas em caso de debugar
            card.delete()
        else:
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
    TAG = (request.POST.get('tag_card')).upper()
    # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
    
    updateNote = Note.objects.get(id=int(ID))
    updateNote.title = title
    updateNote.content = content  
    if Tag.objects.filter(tag = TAG).exists():
            t = Tag.objects.get(tag = TAG) 
    else:
        t = Tag(tag = TAG)
        t.save()
    updateNote.tag = t
    updateNote.save()
    return redirect('index')


def tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/noteTags.html', {'tags': all_tags})

def tagVisualization(request, name):
    t = Tag.objects.get(tag = name)
    Notes = Note.objects.all().filter(tag=t)
    return render(request, 'notes/note.html', {'notes': Notes})