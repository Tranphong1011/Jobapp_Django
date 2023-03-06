from django.shortcuts import redirect, render
from django.urls import reverse

from uploadapp.forms import uploadappForm, uploadfileForm

# Create your views here.
def uploadapp(request):
    form = uploadappForm()
    if request.POST:
        form = uploadappForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/add_image.html', {'form': form, 'saved_object': saved_object})
            # return redirect(reverse('thank_you'))
    # context = {'form': form, 'saved_object': saved_object}
    # context = {"form": form, "save_object": save_object}
    
    # return render(request, 'uploadapp/add_image.html', context)
    return render(request, 'uploadapp/add_image.html', {'form': form})
    

# def thank_you(request):
#     context = {}
#     return render(request, 'uploadapp/thank.html', context)

def uploadfile(request):
    form = uploadfileForm()
    if request.POST:
        form = uploadfileForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/add_file.html', {'form': form, 'saved_object': saved_object})
            # return redirect(reverse('thank_you'))
    # context = {'form': form, 'saved_object': saved_object}
    # context = {"form": form, "save_object": save_object}
    
    # return render(request, 'uploadapp/add_image.html', context)
    return render(request, 'uploadapp/add_file.html', {'form': form})
 