from django.contrib import admin
from django.urls import path
from CRUD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>', views.RUDStudentAPI.as_view()),






    # path('studentapi/', views.StudentList.as_view()),
    # # path('studentapi/', views.StudentCreate.as_view()),
    # # path('studentapi/<int:pk>', views.StudentRetrive.as_view()),
    # # path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>', views.StudentDelete.as_view()),





    # path('studentapi/', views.StudentAPI.as_view()),
    # path('studentapi/<int:pk>', views.StudentAPI.as_view()),


    # path('studentapi/', views.student_api),
    # path('studentapi/<int:pk>', views.student_api),

    # path('studentapi/', views.StudentAPI.as_view()),
    # path('student/', views.hello_world),
]
