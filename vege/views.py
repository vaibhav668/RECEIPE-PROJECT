from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipe

def receipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name", "").strip()
        receipe_description = data.get("receipe_description", "").strip()

        if receipe_name and receipe_description:
            Receipe.objects.create(
                receipe_name=receipe_name,
                receipe_description=receipe_description,
                receipe_image=receipe_image,
            )
        return redirect("/")   # root shows recipes

    queryset = Receipe.objects.all()
    if request.GET.get("search"):
        queryset = queryset.filter(
            receipe_name__icontains=request.GET.get("search").strip()
        )
    return render(request, "receipes.html", {"receipes": queryset})


def update_receipe(request, id):
    receipe_obj = get_object_or_404(Receipe, id=id)
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name", "").strip()
        receipe_description = data.get("receipe_description", "").strip()

        if receipe_name:
            receipe_obj.receipe_name = receipe_name
        if receipe_description:
            receipe_obj.receipe_description = receipe_description
        if receipe_image:
            receipe_obj.receipe_image = receipe_image

        receipe_obj.save()
        return redirect("/")   # back to root

    return render(request, "update_receipes.html", {"receipe": receipe_obj})


def delete_receipe(request, id):
    receipe_obj = get_object_or_404(Receipe, id=id)
    receipe_obj.delete()
    return redirect("/")       # back to root
