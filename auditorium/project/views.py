from .models import booking
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def history(request):
    bookings = booking.objects.all()
    return render(request, 'history.html', {'bookings': bookings})


from django.contrib import messages

def booking_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        booking.objects.create(
            name=name,
            date=date,
            time=time
        )

        messages.success(request, "Booking Successful!")  # ✅ first
        return redirect('history')  # ✅ then redirect

    return render(request, 'booking.html')