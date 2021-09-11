from django.urls import path,include
from . import views
urlpatterns = [
 
    path('signuppage/',views.employeePage,name='employeePage'),
    path('viewall/',views.employee_list,name='employee_list'),
    path('viewemployee/<fetchid>',views.employee_details,name='employee_details'),
    path('signup/',views.signup,name='signup'),
    path('view/',views.viewall,name='viewall'),
    path('update_search_api/',views.update_search_api,name='update_search_api'),
    path('update_api/',views.update_data_read,name='update_data_read'),
    path('update/',views.update,name='update'),
    path('login/',views.login_check,name='login_check'),
    path('logout/',views.logout,name='logout'),
    path('loginview/',views.loginview,name='loginview'),

]