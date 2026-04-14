from django.shortcuts import render

# Create your views here.
posts = [
        {"id":1, "title":"First Post", "content":"This is the content of the first post."},
        {"id":2, "title":"Second Post", "content":"This is the content of the second post."},
        {"id":3, "title":"Third Post", "content":"This is the content of the third post."},
    ]
def home(request):
    return render(request, "home.html", {"posts": posts})

def post_details(request, post_id):
    post = next(p for p in posts if p["id"] == post_id)
    return render(request, "post_detail.html", {"post":post})