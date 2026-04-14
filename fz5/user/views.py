from django.shortcuts import render

# Create your views here.
def info(request):
    context = {
        "user": {"Id": 20231370582, "name": "Enyinnaya", "age": 18, "course": "Python"}
    }
    return render(request, 'user/index.html', context)

def tag(request):
    context = {
        "vars": [1,2,3,4,5,6,7,8,9,10],
        "is_logged_in": False
    }
    return render(request, 'user/tags.html', context)

def filters(request):
    context = {
        "text": "hello world",
        "items": ["apple", "banana", "cherry"],
        "price": 1234.56789,
        "date": "2024-11-15",
        "html_content": "<strong>Bold Text</strong>"
    }
    return render(request, 'user/filter.html', context)