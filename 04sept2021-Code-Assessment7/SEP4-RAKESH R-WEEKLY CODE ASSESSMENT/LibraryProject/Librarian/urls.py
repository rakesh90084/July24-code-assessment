from django.urls import path,include
from . import views
urlpatterns = [
 
    path('addpage/',views.librarianPage,name='librarianPage'),
    path('viewall/',views.librarian_list,name='librarian_list'),
    path('viewlibrarian/<fetchid>',views.librarian_details,name='librarian_details'),
    path('register/',views.register,name='register'),
    path('view/',views.viewall,name='viewall'),
    path('search/',views.searchapi,name='searchapi'),
    path('update_search_api/',views.update_search_api,name='update_search_api'),
    path('delete_search_api/',views.delete_search_api,name='delete_search_api'),
    path('update_api/',views.update_data_read,name='update_data_read'),
    path('delete_api/',views.delete_data_read,name='delete_data_read'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),
    path('searchview/',views.search_librarian,name='search_librarian'),
    path('home/',views.home,name='home'),
    path('login/',views.login_check,name='login_check'),
    path('loginview/',views.loginview,name='loginview'),
#     path('contact/',views.contact,name='contact'),
]