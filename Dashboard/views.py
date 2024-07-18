from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create a function for View Dashboard Pages
@login_required
def view_dashboard(request):

    if request.user.user_type == "normal":
        render(request, "normal.html")

    elif request.user.user_type == "seller":
        render(request, "seller.html")

    elif request.user.user_type == "admin":
        render(request, "admin.html")
