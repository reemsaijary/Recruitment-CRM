from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("dashboard")

            if hasattr(user, "profile"):
                if user.profile.role == "admin":
                    return redirect("dashboard")
                elif user.profile.role == "company":
                    return redirect("company_dashboard")
                elif user.profile.role == "candidate":
                    return redirect("candidate_dashboard")

            messages.error(request, "User role is not assigned.")
            return redirect("login")

        messages.error(request, "Invalid username or password.")

    return render(request, "core/auth/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")