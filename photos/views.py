from django.shortcuts import render, redirect
from .models import UploadPhoto

# Create your views here.

def home(request):
	if request.method == 'POST':
		new = UploadPhoto()
		new.image = request.FILES['photo']
		new.save()
		return redirect('/')
	else:
		pic = UploadPhoto.objects.all()
		return render(request, 'home.html', {'pic': pic})


def home_delete(request, id):
	if request.method == 'POST':
		pic = UploadPhoto.objects.get(id=id)
		pic.delete()
		return redirect('/')