from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from myapi.core import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('branches/', views.branchesView.as_view(), name='branches'),
    path('branchesurl', views.branchesUrlView.as_view(), name='branchesurl'),
    path('branchesprurl', views.branchesPrView.as_view(), name='branchesprurl'),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
