from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User


# The Section select and View Main page of LoginSystem
def view_login_signin_page(request):

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "login":
            return login_process(request)

        elif form_type == "signup":
            return signup_process(request)

        else:
            messages.error(request, "Invalid form type.")
            return render(request, "index.html")

    else:
        messages.error(request, "Method of Request is not POST.")

    return render(request, "index.html")


# The login process
def login_process(request):

    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return redirect("home")

    else:
        return JsonResponse({"error": "Invalid username or password."}, status=400)


# The signup process
def signup_process(request):

    username = request.POST.get("username")
    password = request.POST.get("password")
    password_confirm = request.POST.get("password_confirm")

    if password == password_confirm:

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already taken."}, status=400)

        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            return redirect("home")

    else:
        return JsonResponse({"error": "Passwords do not match."}, status=400)

    return redirect("index")
