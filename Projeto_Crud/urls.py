from django.urls import path
from app_crud import views

urlpatterns = [
    path('', views.home, name="home"),
    path('lista/',views.pacientes,name="criar_pacientes" ),
    path('pacientes/', views.listar, name='listar_pacientes'),
    path('editar/<int:id>/', views.edit, name="alterar_pacientes"),
    path('editado/<int:id>/', views.savedit, name="alterados"),
    path('apagar/<int:id>/', views.delete, name="apagar"),
]
