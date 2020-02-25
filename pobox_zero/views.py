from django.shortcuts import render, redirect
from .models import Postcard, Sender
from .forms import PostcardForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def postcard_list(request):
    postcards = Postcard.objects.all()
    return render(request, 'pobox_zero/postcard_list.html', {'postcards': postcards})

@login_required
def favorites(request):
    faves = request.user.favorited_by.all()
    return render(request, 'pobox_zero/favorites.html', {'faves': faves})

def postcard_detail(request, pk):
    postcard = Postcard.objects.get(id=pk)
    is_fave = False
    if postcard.favorited_by.filter(id=request.user.id).exists():
        is_fave = True
    return render(request, 'pobox_zero/postcard_detail.html', {'postcard': postcard, 'is_fave': is_fave})

@login_required
def postcard_create(request):
    if request.method == 'POST':
        form = PostcardForm(request.POST, request.FILES)
        form.instance.author = request.user
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

@login_required
def postcard_favorite(request, pk):
    user = request.user
    postcard = Postcard.objects.get(id=pk)
    is_fave = False
    # fav = Favorite.objects.create(user, postcard)

    if postcard.favorited_by.filter(id=request.user.id).exists():
        postcard.favorited_by.remove(user)
        is_fave = False
    else:
        postcard.favorited_by.add(user)
        is_fave = True
    return render(request, 'pobox_zero/postcard_detail.html', {'postcard': postcard, 'is_fave': is_fave })