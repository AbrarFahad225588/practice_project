from django.shortcuts import render
from .forms import practiceModel
# Create your views here.
def model_form(request):
    if request.method=='POST':
        form=practiceModel(request.POST)
        if form.is_valid():
            return render(request,'form.html',{'form':form})
    else:
        form=practiceModel()
    return render(request,'form.html',{'form':form})