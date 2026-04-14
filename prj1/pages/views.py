from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {'title': 'Home'})
def about(request):
    return render(request, "pages/about.html", {'title': 'About'})
def services(request):
    services_list = [
        {'name': 'Web Development', 'popular': True},
        {'name': 'Mobile App', 'popular': False},
        {'name': 'Data Analysis', 'popular': True},
        {'name': 'SEO Optimization', 'popular': False},
    ]
    context = {'services': services_list, 'title': 'Our Services'}
    return render(request, 'pages/services.html', context)
def teams(request):
    team_members = [
        {'name': 'Alice Johnson', 'role': 'Project Manager', 'Experience': 3, 'Lead': False},
        {'name': 'Bob Smith', 'role': 'Web Developer', 'Experience': 3, 'Lead': False},
        {'name': 'Catherine Lee', 'role': 'UI/UX Designer', 'Experience': 4, 'Lead': False},
        {'name': 'Enyinnaya', 'role': 'Python Dev', 'Experience': 3, 'Lead': True},
    ]
    context = {'team_members': team_members, 'title': 'Our Team'}
    return render(request, 'pages/team.html', context)