

from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
data = {
    "title" : "Home Page",
    "content" : "This is the home page",
    "values": [100, 300, True],
}
def index(request):
    return render(request, "main/index.html", data)


def about(request):
    return render(request, "main/about.html", {"text":"About Us Page"})



