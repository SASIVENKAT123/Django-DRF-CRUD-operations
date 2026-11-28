from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)


# urlpatterns=[
#     path('api/students/' ,views.student_list),
#     path('api/students/<int:student_id>/',views.student_detail),
#     path('api/students/create/', views.student_create),
# ]


# drf
urlpatterns=[
    path('api/drf/students/',views.StudentListAPIView.as_view()),
    path('api/drf/students/<int:student_id>/',views.StudentDetailsAPIView.as_view()),
    path('api/drf/generic/students/<int:student_id>/',views.StudentDetailGenericAPIView.as_view()),
    path('api/drf/mixin/students/<int:student_id>/',views.StudentRetrieveMixinAPIView.as_view()),
    path('api/drf/mixin/students/RUD/<int:student_id>/',views.StudentRetrieveUpdateDeleteMixinAPIView.as_view()),
    path('api/drf/mixin/students/',views.StudentListCreateMixinAPIView.as_view()),
    path('api/drf/concrete/students/',views.StudentListCreateAPIView.as_view()),
    path('api/drf/concrete/students/<int:student_id>/',views.StudentRetrieveUpdateDestroyAPIView.as_view()),
]
router =DefaultRouter()
router.register(

    'students',
    views.StudentViewSet,
    basename = 'student'
)

urlpatterns+= router.urls


urlpatterns+=[
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]


