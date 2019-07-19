from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
from .forms import NewPortfolio

# Create your views here.

def portfolio(request):
    portfolio = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolio':portfolio})

def new(request):
    if request.method == "POST":
        form = NewPortfolio(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('portfolio') 
    else:
        form = NewPortfolio()
        return render(request, 'portfolio/new.html', {'form':form})

def update(request, pk):
    portfolio = get_object_or_404(Portfolio, pk = pk)
    form = NewPortfolio(request.POST, request.FILES, instance=portfolio)
    if form.is_valid():
        form.save()
        return redirect('portfolio')   
    return render(request, 'portfolio/new.html', {'form':form})
    
def delete(request, pk):
    portfolio = get_object_or_404(Portfolio, pk = pk)
    portfolio.delete()
    return redirect('portfolio')
