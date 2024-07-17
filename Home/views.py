from django.shortcuts import render

# Create your views here.


def view_home_page(request):
    if request.method == "POST":
        pass

    return render(request=request)
