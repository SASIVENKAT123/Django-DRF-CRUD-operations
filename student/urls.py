from django.urls import path
from . import views

# urlpatterns=[
#     path('api/students/' ,views.student_list),
#     path('api/students/<int:student_id>/',views.student_detail),
#     path('api/students/create/', views.student_create),
# ]

urlpatterns=[
    path('api/drf/students/',views.StudentListAPIView.as_view()),
    path('api/drf/students/<int:student_id>/',views.StudentDetailsAPIView.as_view()),
]