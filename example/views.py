from django.shortcuts import render,HttpResponse
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.
#def home(request):
    #return HttpResponse("this is my page")
    #return render(request, 'home.html',{'name':'Ibrar'})
    #return render(request, 'service.html')
    #return render(request, 'login.html')
#def register(request):
    #form = UserCreationForm()
    #return render(request, 'register.html',{'form': form})
#def setcookie(request):  
    #response = HttpResponse("Cookie Set")  
    #response.set_cookie('java-tutorial', 'javatpoint.com')  
    #return response  

#def getcookie(request):  
    #tutorial  = request.COOKIES['java-tutorial']  
    #return HttpResponse("java tutorials @: "+  tutorial)
def setsession(request):  
    request.session['sname'] = 'irfan'  
    request.session['semail'] = 'irfan.sssit@gmail.com'  
    return HttpResponse("session is set")  

#def getsession(request):  
    #studentname = request.session['sname']  
    #studentemail = request.session['semail']  
    #return HttpResponse(studentname+" "+studentemail)