from django.urls import path
from student_app import views

urlpatterns = [
    path('', views.StudentList.as_view()),
    path('<int:pk>', views.StudentDetail.as_view()),
    path('year/<int:year>', views.StudentListByYear.as_view()),

    path('marks', views.MarkList.as_view()),
    path('marks/<int:pk>', views.MarkDetail.as_view()),
]