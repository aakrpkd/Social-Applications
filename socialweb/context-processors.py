from api.models import Post

def activity(request):
    if request.user.is_authenticated:
        cnt=Post.objects.filter(user=request.user).count()
        pup=Post.objects.filter(upvote=request.user).count()
        return {"pcount":cnt,"punt":pup}
    else:
        return {"pcount":0}
