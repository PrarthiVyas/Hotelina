from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import  RoomDetailView, CancelBookingView


app_name="home"
urlpatterns = [
    path('', views.index, name="home"),
    path('aboutus/',views.aboutus,name="aboutus"),
    
    
    path('login/',views.log_in),
    path('register/',views.register),
    path('bvn/',views.bvn),
    path('baroda/',views.baroda),
    path('surat/',views.surat),
    path('abad/',views.abad),
    path('bvnroom/',views.bvnroom),
    path('bvnres/',views.bvnres),
    path('room_list/<id>',views.RoomList, name="room_list"),
    path('booking_list/',views.BookingList,name="BookingList"),
    path('restaura/<id>',views.restaura , name = "restaura"),
    path('tableservice/', views.tableservice),
    path('takeout/', views.takeout),
    path('outdoor/',views.outdoor),
    path('booking/cancel/<pk>', CancelBookingView.as_view() ,name="CancelBookingView"),
    
    path('room/<hotel_id>/<id>',RoomDetailView.as_view(),name='RoomDetailView'),
    path('AC/<hotel_id>',views.AC,name='AC'),
    path('NONAC/<hotel_id>',views.NONAC,name='NONAC'),
    path('DELUX/<hotel_id>',views.DELUX,name='DELUX')

    
]+ static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
                             