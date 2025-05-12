from django.shortcuts import render, redirect
from noteapp.models import Note

# Create your views here.
def index(request):
    notes = Note.objects.all()
    if request.method == 'POST' :
        text = request.POST['note']
        note = Note.objects.create(text=text)
        note.save()
        return redirect('index')

    return render (request, 'index.html',{'notes': notes})

def delete_note(request,id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('index')

def edit_note(request,id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.text = request.POST ['note']
        note.save()
        return redirect('index')
    return render(request,'edit.html',{'note':note})