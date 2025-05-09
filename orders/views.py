from django.shortcuts import render, redirect
from .forms import CheckoutForm

# Create your views here.
def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process form.cleaned_data here
            return redirect('home')  # or 'thank_you'
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})