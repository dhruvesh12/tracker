from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import track_data
# Create your views here.

def home(request):
	
	s= request.GET.get('search')
	if s:
		p = track_data.objects.filter(name__icontains=s)


		#Post.objects.create(name=h, content=c, img=i)

		return render(request,'home.html',{'p':p})
	return render(request,'home.html')


def add(request):
	if request.method == 'POST':
		h = request.POST['firstname']
		c = request.POST['track']
		#i = request.FILES['pho']

		track_data.objects.create(name=h, tracking_no=c)
	return render(request, 'add.html',{})


def track_detail(request,pk):
	post = get_object_or_404(track_data, pk=pk)
	

	return render(request,'track_detail.html',{'post':post})