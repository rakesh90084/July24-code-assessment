from django.urls  import path,include
from . import views
urlpatterns= [ 

   path('register/',views.register_faculty,name='register_faculty'),
   path('login/',views.login_faculty,name='login_faculty'),
   path('viewall/',views.faculty_list,name='faculty_list'),
   path('view/<fetchid>',views.faculty_details,name='faculty_details'),
   path('fcode/<fcode>',views.faculty_fetch,name='faculty_fetch'),
   path('add/',views.facultyaddpage,name='facultyaddpage'),
   
]