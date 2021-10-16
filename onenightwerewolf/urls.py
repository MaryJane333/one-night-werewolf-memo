from django.contrib import admin
from django.urls import path
from .views import Delete, list_func, login_func, logoutfunc, NameCreate, NameUpdate, NumberCreate, NumberUpdate, sign_up_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', NameCreate.as_view(), name='create_name'),
    path('create/number', NumberCreate.as_view(), name='create_number'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
    path('update/number/<int:pk>', NumberUpdate.as_view(), name='update_number'),
    path('list/', list_func, name='list'),
    path('login/', login_func, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('sign_up/', sign_up_func, name='sign_up'),
    path('update/name/<int:pk>', NameUpdate.as_view(), name='update_name'),
]