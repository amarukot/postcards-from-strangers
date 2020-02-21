from django.shortcuts import render, redirect
from .models import Postcard, Sender
from .forms import PostcardForm
from django.contrib.auth.decorators import login_required


def postcard_list(request):
    postcards = Postcard.objects.all()
    return render(request, 'pobox_zero/postcard_list.html', {'postcards': postcards})

def postcard_detail(request, pk):
    postcard = Postcard.objects.get(id=pk)
    return render(request, 'pobox_zero/postcard_detail.html', {'postcard': postcard})

@login_required
def postcard_create(request):
    if request.method == 'POST':
        form = PostcardForm(request.POST, request.FILES)
        if form.is_valid():
            postcard = form.save()
            return redirect('postcard_detail', pk=postcard.id)
    else:
        form = PostcardForm()
    return render(request, 'pobox_zero/postcard_form.html', {'form': form})

@login_required
def postcard_edit(request, pk):
    postcard = Postcard.objects.get(id=pk)
    if request.method == 'POST':
        form = PostcardForm(request.POST, request.FILES, instance=postcard)
        if form.is_valid():
            postcard = form.save()
            return redirect('postcard_detail', pk=postcard.id)
    else:
        form = PostcardForm(instance=postcard)
    return render(request, 'pobox_zero/postcard_form.html', {'form': form})

@login_required
def postcard_delete(request, pk):
    Postcard.objects.get(id=pk).delete()
    return redirect('/')