
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from comment.form import CommentForm
from comment.models import Comment


def create(request):
    if request.method == 'GET':
        form = CommentForm()
    elif request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.created = timezone.now()
            comment.save()
            return render(request, 'create_success.html')
            #return redirect("/create_success.html")
    return render(request, 'create.html', context={
        'form': form})


def all(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', context={
        'comments': comments})


def retrieve(request, id=None):
    comment = Comment.objects.get(pk=id)
    return render(request, 'item.html', context={
        'comment': comment,
    })


def delete(request, id=None):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    return redirect('/comments')


def edit(request, id=None):
    comment = get_object_or_404(Comment, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.save()
            return redirect('/comments')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit.html', {'form': form})