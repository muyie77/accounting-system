from django.urls import path

from . import views

app_name = 'accounting_system'

urlpatterns = [
    path('', views.index, name='index'),
    path('chart_of_accounts/', views.chart_of_accounts, name='chart_of_accounts')
]
