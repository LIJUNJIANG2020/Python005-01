from django.shortcuts import render, get_object_or_404
from .models import Movie, Comment

# Create your views here.
def list(request, **kwargs):
    movies = Movie.objects.all()
    if request.method == 'GET':
        try:
            kw = request.GET.dict()['kw']
            movies = movies.filter(name__contains=kw)
        except:
            kw = ''
    return render(request, 'list.html', locals())


def commnet(request, **kwargs):
    pk = kwargs.get("pk")
    movie = get_object_or_404(Movie, pk=pk)
    comments = Comment.objects.filter(movie_id=movie.id)
    try:
        kw = request.GET.dict()['kw']
        comments = comments.filter(comm__contains=kw)
    except:
        kw = ''

    return render(request, 'comment.html', locals())
    