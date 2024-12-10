
from django.contrib import admin
from django.urls import path
from  raja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('insert/',views.insert,name="insert"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete)
]
