from django.urls  import path,include
from . import views
urlpatterns=[
   path('',views.register,name='register'),
   path('viewall/',views.student_list,name='student_list'),
   path('view/<fetchid>',views.student_details,name='student_details'),
   path('admno/<admno>',views.admission,name='admission'),
   path('add/',views.studentaddpage,name='studentaddpage'),
   
]