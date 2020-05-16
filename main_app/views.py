from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm


def index(request):
    if request.method == 'POST':
        form = WidgetForm(request.POST)

        if form.is_valid():
            
            form.save()
            widgets = Widget.objects.all
            
            return render(request, 'widgets/index.html', {'widgets': widgets})

    else:
        widgets = Widget.objects.all
        return render(request, 'widgets/index.html', {'widgets': widgets})

def view(request, widget_id):
    context = {
        'widget': Widget.objects.get(id=widget_id),
    }
    return render(request, 'widgets/view.html', context)

def delete(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    
    return redirect('/')



