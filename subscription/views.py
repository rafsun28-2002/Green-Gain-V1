from django.shortcuts import render

# Create your views here.
def create_plan(request):
    return render(request, "CreatePlan.html")