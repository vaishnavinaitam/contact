from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
# Create your views here.

def add_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'app1/contact_form.html'
    context = {'form': form}
    return render(request, template_name, context)

def show_view(request):
    objs = Contact.objects.all()
    template_name = 'app1/contact_list.html'
    context = {'data': objs}
    return render(request, template_name, context)

def update_view(request, pk):
    obj = Contact.objects.get(id=pk)
    form = ContactForm(instance=obj)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'app1/contact_form.html'
    context = {'form': form}
    return render(request, template_name, context)

def delete_view(request, pk):
    obj = Contact.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'app1/Delete_conformation.html'
    context = {'data': obj}
    return render(request, template_name, context)
