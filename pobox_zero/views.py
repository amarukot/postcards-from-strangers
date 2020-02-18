from django.shortcuts import render, redirect
from .models import Postcard, Sender
from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse


def postcard_list(request):
    postcards = Postcard.objects.all()
    return render(request, 'pobox_zero/postcard_list.html', {'postcards': postcards})

def postcard_detail(request, pk):
    postcard = Postcard.objects.get(id=pk)
    return render(request, 'pobox_zero/postcard_detail.html', {'postcard': postcard})

def postcard_create(request):
    if request.method == 'POST':
        form = PostcardForm(request.POST)
        if form.is_valid():
            postcard = form.save()
            return redirect('postcard_detail', id=postcard.id)
    else:
        form = PostcardForm()
    return render(request, 'pobox_zero/postcard_detail.html', {'postcard': postcard})

