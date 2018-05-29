from django.conf.urls import url
from firstapp import views
from django.urls import path,re_path
app_name = 'firstapp'
urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^$',views.index,name='view_index'),
    url(r'^user_login$',views.user_login,name='user_login')

    # url(r'formpage/',views.form_name_view,name='form_name'),
]
