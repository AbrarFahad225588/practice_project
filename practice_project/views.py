from django.shortcuts import render
from .forms import PracticeForm
def show_form(request):
    if request.method=='POST':
        form=PracticeForm(request.POST)
        if form.is_valid():
            return render(request,'form.html',{'form':form})
    else:
         form=PracticeForm()
    return render(request,'form.html',{'form':form})




   