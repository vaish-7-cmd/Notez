from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.http import require_POST
# Create your views here.
def note_list(request):
       query = request.GET.get('q')
       if query:
        notes = Note.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-is_pinned', '-created_at')  # Order by pinned status and then by creation date
       else:
        notes = Note.objects.all()
       return render(request, 'notes/note_list.html', {'notes': notes})

def toggle_pin(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.is_pinned = not note.is_pinned
    note.save()
    return redirect('note_list')

def create_note(request):
    if request.method == 'POST':
        print("FILES:", request.FILES)  # Debugging line to check if files are being sent
        form = NoteForm(request.POST , request.FILES)
        # Check if the form is valid and if the note already exists
        # This prevents duplicate notes with the same title and content
        
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            
        # Redirect to the note list after saving
            # Check if a note with the same title and content already exists   
            if Note.objects.filter(title=title, content=content).exists():
                messages.warning(request, "This note already exists!")
            else:
                 form.save()
            messages.success(request, "Note saved successfully!")
            return redirect('note_list')  # Always redirect after POST
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})

def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
        return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/update_note.html', {'form': form})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/delete_note.html', {'note': note})



def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        voice_file = request.FILES.get('voice_note')

        note = Note(title=title, content=content)
        if voice_file:
            note.voice_note = voice_file
        note.save()
        messages.success(request, "Note added successfully!")
        return redirect('note_list')

    return render(request, 'note_list.html')  # use your actual file name

