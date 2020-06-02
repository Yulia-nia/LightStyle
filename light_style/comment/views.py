from django.shortcuts import render, redirect
from comment.form import CommentForm
# Create your views here.


def create_comment(request):
    if request.method == 'GET':
        form = CommentForm()
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            #poll = form.save()
            #poll.image = Pillow(request.FILES['image'])
            return redirect("/")
    return render(request, 'create_comment.html', context={'form': form})