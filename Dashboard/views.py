from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create a function for View Dashboard Pages
@login_required
def view_dashboard(request):

    if request.user.user_type == "normal":
        render(request, "normal.html")

    elif request.user.user_type == "seller":
        render(request, "seller.html")

    elif request.user.user_type == "admin":
        render(request, "admin.html")


@login_required
def upgrade_to_seller(request):

    if request.method == "POST":
        store_name = request.POST.get("store_name")
        store_description = request.POST.get("store_description")

        if store_name and store_description:
            user = request.user
            user.type_user = "seller"
            user.store_name = store_name
            user.store_description = store_description
            user.save()
            return redirect("dashboard")

        else:
            context = {"error": "All fields is required."}

    return render(request, "normal_to_seller.html", context)
