from django.shortcuts import render,redirect,get_object_or_404
from .forms import festival_F
from .models import festival_M
from django.utils.timezone import datetime

# Create your views here.

def festival_home(request):
    try:
       area = request.GET['locate']
       festivals = festival_M.objects.filter( locate = area)
    except:
        festivals = festival_M.objects.all()
    return render (request, 'festival_home.html', {'festivals': festivals})

def writing(request):
    if request.method == 'POST':
        inputForm = festival_F(request.POST,request.FILES)
        print("여기들어옴?", inputForm)
        if inputForm.is_valid():
            tempsave = inputForm.save(commit = False)
            tempsave.pub_date = datetime.now()
            tempsave.save()
            return redirect('festival_home')
        return redirect('festival_home')

    else:
        newForm = festival_F()
        return render(request,'writing.html', {'newForm' : newForm})

def detail(request, festival_id):
    detailForm = get_object_or_404(festival_M, pk = festival_id) #db에서 해당 객체 담기.
    return render (request, 'detail.html', {'detailForm' : detailForm})

def delete(request, festival_id):
    deleteForm = get_object_or_404(festival_M, pk = festival_id)
    deleteForm.delete()
    return redirect('festival_home')

def edit(request,festival_id):
    editForm = get_object_or_404(festival_M, pk = festival_id)
    return render(request, 'edit.html', {'editForm': editForm})

def update(request,festival_id):
    updateForm = get_object_or_404(festival_M, pk = festival_id)
    updateForm.title = request.POST['edit_title']
    updateForm.locate = request.POST['edit_locate']
    updateForm.period = request.POST['edit_period']
    updateForm.body = request.POST['edit_body']
    updateForm.pub_date = timezone.datetime.now()
    updateForm.save()
    return redirect ('/festival/detail/' + str(festival_id))
