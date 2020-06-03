from django.shortcuts import render,get_object_or_404,redirect
from .models import Review
from django.utils import timezone
from .form import Reviewform

# Create your views here.
def review(request):
    reviews = Review.objects.all()
    return render(request,'review.html',{'reviews':reviews})

def review_detail(request,review_id):
    review = get_object_or_404(Review,pk=review_id)
    return render(request,'review_detail.html',{'review':review})

def review_new(request):
    if request.method=='POST':
        form = Reviewform(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date=timezone.now()
            content.save()
            return redirect('review')
    else:
        form = Reviewform()
        return render(request,'review_new.html',{'form':form})

def review_create(request):
    new_review = Review()
    new_review.title = request.POST['title']
    new_review.pub_date = timezone.datetime.now()
    new_review.body = request.POST['body']
    new_review.fest_date = request.POST['fest_date']
    new_review.save()
    return redirect('review_detail',new_review.id)

def review_edit(request,review_id):
    edit_review = get_object_or_404(Review,pk=review_id)
    return render(request,'review_edit.html',{'review':edit_review})

def review_update(request,review_id):
    update_review = get_object_or_404(Review,pk=review_id)
    update_review.title = request.POST['title']
    update_review.pub_date = timezone.datetime.now()
    update_review.body = request.POST['body']
    update_review.fest_date = request.POST['fest_date']
    update_review.save()
    return redirect('review_detail',update_review.id)


def review_delete(request,review_id):
    delete_review = get_object_or_404(Review,pk=review_id)
    delete_review.delete()
    return redirect('review')