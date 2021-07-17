
from django.contrib.auth.forms import UsernameField
from django.http import request
from django.shortcuts import redirect, render,HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Restaura
from .models import sign
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from .models import City
from .models import Bvn
from .models import Rooms,Booking
from .models import Restaura
from django.views.generic import ListView, FormView,View,DeleteView
from .forms import AvailableForm
from .available import check_availability
from home import available
from django.urls import reverse_lazy,reverse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

def index(request):
    city1=City.objects.filter(name="Bhavnagar")
    city2=City.objects.filter(name="Baroda")
    city3=City.objects.filter(name="Surat")
    city4=City.objects.filter(name="Ahemdabad")
    city5=City.objects.filter(name="Rajkot")
    city6=City.objects.filter(name="Gandhinagar")
    city7=City.objects.filter(name="Junagadh")
    city8=City.objects.filter(name="Amreli")
    city9=City.objects.filter(name="Jamnagar")
    return render(request,'index.html',{'city':city1,'city2':city2,'city3':city3,'city4':city4,'city5':city5,'city6':city6,'city7':city7,'city8':city8,'city9':city9})


# Create your views here.
def aboutus(request):
    return render(request,'aboutus.html')

def services(request):
    return render(request,'services.html')




def log_in(request):
    if request.method=="POST":
        username=request.POST.get("email")
        pass1=request.POST.get("pass1")
        user=authenticate(username=username,password=pass1)
      
        print(username)
        print(pass1)
        if user:
            login(request , user)
            print("login success")
            return redirect("/")
        else:
            messages.error(request, 'Please Enter Valid Crendentials!')
            return render(request,"login.html")
    else:
        return render(request,'login.html')
def register(request):
   
    if request.method=="POST":
    
        username=request.POST.get('username')      
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')       
        if len(username)>15:
            messages.error(request, "*Your user name must be under 10 characters")
            return render(request,'register.html')

        if not username.isalnum():
            messages.error(request, "*User name should only contain letters and numbers")
            return render(request,'register.html')
        SpecialSym =['$', '@', '#', '%']
    
    
        if len(pass1) < 6:
            messages.error(request,'''*Passwword's length should be at least 6''')
            
            return render(request,'register.html')
        
        if len(pass1) > 20:
            messages.error(request,'''*Password's length should be not be greater than 20''')
            
            return render(request,'register.html')
        
            
            
        if not any(char.isdigit() for char in pass1):
            messages.error(request,'*Password should have at least one numeric / digit')
            
            return render(request,'register.html')
        
        if not any(char.isupper() for char in pass1):
            messages.error('*Password should have at least one uppercase letter')
        
            return render(request,'register.html')
        
        
        if not any(char.islower() for char in pass1):
            messages.error(request,'*Password should have at least one lowercase letter')
        
            return render(request,'register.html')
        

        user_obj=User.objects.create(username=username,email=email)
        user_obj.set_password(pass1)   
        user_obj.save()
        return render(request,"login.html")
  
    return render(request,'register.html')

def bvn(request):
  
    bvn1=Bvn.objects.all()

    return render(request,'bvn.html',{'bvn':bvn1 , "user" : request.user})
   
def bvnroom(request):
    room=Bvn.objects.filter(entry1="Room")
    return render(request,'bvnroom.html',{'bvn':room})
def bvnres(request):
    room=Bvn.objects.filter(entry2="Restaura")
    return render(request,'bvnres.html',{'bvn':room})


def baroda(request):
    return render(request,'baroda.html')
def surat(request):
    return render(request,'surat.html')
def abad(request):
    return render(request,'abad.html')

def RoomList(request, id):
    print(f"this is roomlist {id}")
    r1=Rooms.objects.filter(category="AC")
    r2=Rooms.objects.filter(category="NON-AC")
    r3=Rooms.objects.filter(category="DELUX")
    return render(request,'room_list_view.html',{'id' : id ,'r1':r1,'r2':r2,'r3':r3})

   
def BookingList(request):
    
    booking = Booking.objects.last()
    context={'booking':booking}
    return render(request,'booking_list.html',context)

class RoomDetailView(View):
    def get(self,request,*args,**kwargs):
        id=self.kwargs.get('id',None)
        hotel_id=self.kwargs.get('hotel_id',None)
        
        room_list=Rooms.objects.filter(id=id)
        
        if len(room_list):
            room=room_list[0]
            room_category=dict(room.ROOM_CATEGORIES).get(room.id,None)
            context={'room_category':room_category,"hotel_id" : hotel_id}
            return render(request,'room_detail_view.html',context)
        else:
            return HttpResponse("Category does not exist")
             

    def post(self,request,*args,**kwargs):
        id=self.kwargs.get('id',None)
        hotel_id=self.kwargs.get('hotel_id',None)
        room_list=Rooms.objects.filter(id=id)
        form=AvailableForm(request.POST)
        day=request.POST.get('day')
        if form.is_valid():
            data=form.cleaned_data
        available_rooms=[]
        user =User.objects.get(id=request.user.id)
        for room in room_list:
            data=form.cleaned_data
            if check_availability(room,data['check_in'],data['check_out']):
                available_rooms.append(room)
        if len(available_rooms)>0:

            room=available_rooms[0]
            # Bvn_obj = Bvn.objects.get(pk=int(request.POST['hotel_id']) )
            
            booking=Booking.objects.create(hotel = Bvn.objects.get(id=int(id)),user=user,day=day,room=room,check_in=data['check_in'],check_out=data['check_out'])
            booking.save()
            return BookingList(request)
        else:
            return HttpResponse('This category of rooms are booked!Try another one')

def restaura(request , id):
        if request.method == 'POST':
           
            if request.POST.get('username') and request.POST.get('phone1') and request.POST.get('no_of_members') and request.POST.get('time'):
                Bvn_obj = Bvn.objects.get(pk=int(request.POST['hotel_id']) )
                username=request.POST.get('username')      
                phone1=request.POST.get('phone1')
                

                # if len(phone1)<10 :
                #     messages.error(request, "*Your Phone Number must be of 10 Digits")
                #     # return render(request,'restaura.html' ,  {"hotel_id" : request.POST['hotel_id']})
                # if not username.isalnum():
                #     messages.error(request, "*User name should only contain letters and numbers")
                    # return render(request,'restaura.html' ,  {"hotel_id" : request.POST['hotel_id']})
                
                    
                post=Restaura.objects.create(username = request.POST.get('username'),hotel= Bvn_obj, phone1 = request.POST.get('phone1'), no_of_members=request.POST.get('no_of_members') , time=request.POST.get('time') ,url=request.POST.get('url'))
              
                print(request.POST['hotel_id'])
                
                post.save()
                post.username= request.POST.get('username')
                post.phone1= request.POST.get('phone1')
                post.no_of_members= request.POST.get('no_of_members')
                post.time= request.POST.get('time')
                 
                
                post.save()
                messages.success(request, "Your data has saved successfully!!")
                
            return render(request, 'restaura.html' , {"hotel_id" : request.POST['hotel_id']})  

        else:
            print(id)
            return render(request,'restaura.html' , {"hotel_id" : id})

def tableservice(request):
    room=Bvn.objects.filter(cat2="Table service")
    return render(request,'tableservice.html',{'bvn':room})

def takeout(request):
    room=Bvn.objects.filter(cat3="Takeout")
    return render(request,'takeout.html',{'bvn':room})

def outdoor(request):
    room=Bvn.objects.filter(cat4="Outdoor seating")
    return render(request,'outdoor.html',{'bvn':room})

class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('home:BookingList')


def AC(request,hotel_id):
    bvn=Rooms.objects.filter(category="AC")
    return render(request,'AC.html',{'bvn':bvn,"hotel_id" : hotel_id})


def NONAC(request,hotel_id):
    bvn=Rooms.objects.filter(category="NON-AC")
    return render(request,'NONAC.html',{'bvn':bvn ,"hotel_id" : hotel_id})



def DELUX(request,hotel_id):
    bvn=Rooms.objects.filter(category="DELUX")
    return render(request,'DELUX.html',{'bvn':bvn,"hotel_id" : hotel_id})