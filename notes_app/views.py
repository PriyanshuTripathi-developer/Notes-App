from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm , NoteForm
from .models import Note


def register_view(request):
    if request.method == "POST":
        form =  RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            messages.success(request , "Registration Successful !")
            request.session["username"] = user.username
            return redirect("notes_list")
        else:
            messages.error(request , "Registration failed.")
            return render(request, "register.html", {"form": form})
    else:
        form = RegistrationForm()
        return render(request , 'register.html' , {'form':form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            messages.success(request , 'Login Successful !')
            request.session["username"] = user.username
            return redirect('notes_list')
        else:
            messages.error(request , "Invalid User name")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request , "Logout successfully !")
    return redirect('login')


@login_required(login_url='login')
def notes_list(request):
    notes = Note.objects.filter(user=request.user, archived=False, trashed=False)
    search_query = request.GET.get("search")
    if search_query:
        notes = notes.filter(title__icontains=search_query)
    notes = notes.order_by("-pinned", "-updated_at")
    context = {"notes": notes, "search_query": search_query}
    return render(request, "notes_list.html", context)

@login_required
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user     
            note.save()
            messages.success(request, "Note created successfully!")
            return redirect("notes_list")
    else:
        form = NoteForm()
    return render(request, "note_form.html", {"form": form, "title": "Create Note"})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully!")
            return redirect("notes_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "note_form.html", {"form": form, "title": "Edit Note"})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.trashed = True
    note.save()
    messages.warning(request, "Note moved to trash.")
    return redirect("notes_list")

@login_required
def trash_list(request):
    notes = Note.objects.filter(user=request.user, trashed=True)
    return render(request, "trash_list.html", {"notes": notes})

@login_required
def restore_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.trashed = False
    note.save()
    messages.success(request, "Note restored successfully!")
    return redirect("trash_list")

@login_required
def delete_permanently(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()

    messages.error(request, "Note deleted permanently.")
    return redirect("trash_list")

@login_required
def toggle_pin(request, note_id):

    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.pinned = not note.pinned
    note.save()
    return redirect("notes_list")

@login_required
def archive_note(request, note_id):
   
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.archived = True
    note.save()
    messages.info(request, "Note archived.")
    return redirect("notes_list")

@login_required
def archive_list(request):
    notes = Note.objects.filter(user=request.user, archived=True, trashed=False)
    return render(request, "archive_list.html", {"notes": notes})

@login_required
def restore_archived(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.archived = False
    note.save()
    messages.success(request, "Note restored to main notes.")
    return redirect("archive_list")