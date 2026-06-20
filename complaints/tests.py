from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm
from .models import Complaint

@login_required
def file_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("complaints:my_complaints")
    else:
        form = ComplaintForm()

    return render(request, "complaints/file_complaint.html", {"form": form})


@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "complaints/my_complaints.html", {"complaints": complaints})