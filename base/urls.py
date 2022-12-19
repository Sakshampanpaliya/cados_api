from django.urls import path
from . import views

from rest_framework_simplejwt.views import(
    TokenObtainPairView
)
urlpatterns=[
    path('',views.endpoints),
    path('advocates/',views.advocate_list,name='advocates'),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('advocates/<str:username>/',views.advocate_detail),
    path('advocates/<str:username>/',views.AdvocteDetail.as_view()),
    path('companies/',views.company_list),
    # path('add_advocate/',views.add_advocate),
    #<username> is a dynamic value 
]