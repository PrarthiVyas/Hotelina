from django.contrib.auth.models import User
from django.db import DefaultConnectionProxy, models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db.models.fields import CharField, IntegerField
from django.urls.base import reverse_lazy


class sign(models.Model):
    username=models.CharField(max_length=122)
    email=models.EmailField(null=True,blank=True,max_length=122)
    pass1=models.CharField(null=True,blank=True,max_length=122)


    def __str__(self):
        return self.username
    
class City(models.Model):
    name=models.CharField(max_length=22)


    

    image=models.ImageField(upload_to="")

class Bvn(models.Model):
    name=models.CharField(max_length=50)
    area=models.CharField(max_length=120)
    # phone=models.CharField(max_length=120,default="")
    
    # email=models.EmailField(max_length = 254,default="")
    cat1=models.CharField(max_length=22)
    cat2=models.CharField(max_length=22)
    cat3=models.CharField(max_length=22,default="")
    cat4=models.CharField(max_length=22,default="")
    cat5=models.CharField(max_length=22,default="")
    entry1=models.CharField(max_length=22,default="")
    entry2=models.CharField(max_length=22,default="")
    image=models.ImageField(upload_to="")

    def __str__(self) :
        return self.name


class baroda(models.Model):
    name=models.CharField(max_length=50,default="")
    area=models.CharField(max_length=120,default="")
    cat1=models.CharField(max_length=22,default="")
    cat2=models.CharField(max_length=22,default="")
    cat3=models.CharField(max_length=22,default="")
    cat4=models.CharField(max_length=22,default="")
    cat5=models.CharField(max_length=22,default="")
    entry1=models.CharField(max_length=22,default="")
    entry2=models.CharField(max_length=22,default="")
    image=models.ImageField(upload_to="")

1
class Rooms(models.Model):
    ROOM_CATEGORIES={
        ('AC','AC'),
        ('NON-AC','NON-AC'),
        ('DELUX','DELUX')
    }
    
    number=models.IntegerField(default=0)
    category=models.CharField(max_length=10,choices=ROOM_CATEGORIES,default="AC")
    beds=models.IntegerField(default=0)
    capacity=models.IntegerField(default=0)
    amount=models.IntegerField(default=0)
    image=models.ImageField(upload_to="")
    
    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'

                

class Booking(models.Model):
    hotel=models.ForeignKey(Bvn,on_delete=models.CASCADE,null= True, blank =True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    day=models.IntegerField(default=0,null= True)
    def __str__(self):
        return f'{self.user} From: {self.check_in} To: {self.check_out}'
    
    def get_room_category(self):
        room_categories=dict(self.room.ROOM_CATEGORIES)
        room_category=room_categories.get(self.room.category)
        return room_category

    def get_cancel_url(self):
        return reverse_lazy('home:CancelBookingView',args=[self.pk,])
    # return f'{}has booked'


class Restaura(models.Model):
    username=models.CharField(max_length=22)
    hotel=models.ForeignKey(Bvn,on_delete=models.CASCADE)
    phone1=models.IntegerField(unique=False)
    
    
    no_of_members=models.IntegerField(unique=False)
    time=models.CharField(max_length=22)
    url=CharField(max_length=22,default="")