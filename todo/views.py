from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    item_list = Todo.objects.order_by('-date')
    if request.method == 'POST':
         form = TodoForm(request.POST)
         if form.is_valid():
             form.save()
             # messages.success(request, 'Item added successfully')

             return redirect('home')
    form = TodoForm()
    context = {
        'list': item_list,
        'forms': form,
        "title": "TODO LIST"
    }
    return render(request, 'index.html', context)

def remove(request, items_id):
    item = Todo.objects.get(id=items_id)
    item.delete()
    messages.info(request, 'Item removed successfully')
    return redirect('home')
