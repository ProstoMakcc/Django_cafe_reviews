from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm

def reviews_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews
    }

    return render(request, 'reviews_system/reviews_list.html', context)

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('reviews_list')
    else:
        form = ReviewForm()

    return render(request, 'reviews_system/add_review.html', {'form': form})
