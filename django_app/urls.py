from django.urls import path
from .views import *

urlpatterns=[
    path('first/',first),
    path('secondurl/',second),
    path('renderurl/',third),
    path('cristiano/',work),
    path('pdf/',work),
    path('reg/',reg_page),
    path('login/',login),
    path('home/',home),
    path('fileupload/',fileupload),
    path('employee_reg/',employee_reg),
    path('search/',search_emply),
    path('prod/',product_details),
    path('prodsearch/',product_search),
    path('files/',file),
    path('check/',check),
    path('display/',display),
    path('display_emp/',display_emp),
    path('file/',filedisplay),
    path('uploads/',dis_uploads),
    path('edit/<int:id>',update_data),
    path('editemp/<int:id>',update_employ),
    path('fileedit/<int:id>',file_update),
    path('files_edit/<int:id>',files_update),
    path('delete_reg/<int:id>',reg_delete),
    path('delete_emply/<int:id>',emply_delete),
    path('delete_file/<int:id>',file_delete),
    path('auth-user-reg/',register_auth_user),
    path('user-reg1/',reg1_user),
    path('log/',reg1_login),
    path('movie/',movie_passing.as_view()),
    path('uploadsapi/',upload_passing.as_view()),


]


