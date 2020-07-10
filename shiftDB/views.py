from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .tasks import shift_book
from .form import ShiftForm
from .models import Shifts



def shifts_view(request):
    shift_book()
    all_shifts = Shifts.objects.all()
    paginator = Paginator(all_shifts, 7)
    page = request.GET.get('pg')
    all_shifts = paginator.get_page(page)
    return render(request, 'shifts.html',{'all_shifts': all_shifts})
    


def shifts_add_view(request):
    if request.method=='POST':
        shift_form = ShiftForm(request.POST)
        if shift_form.is_valid():
            shift_form.save()
            messages.success(request, ('new shift added!'))
            return redirect('shifts')
    else:
        shift_form = ShiftForm()    
    return render(request, 'shifts_add.html', {'shift_form': shift_form})
