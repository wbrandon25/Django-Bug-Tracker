

from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('project/<str:pk>/', views.projectPage, name = 'project'),
    path('project/<str:pk>/create-ticket', views.createTicketForProject, name = 'createTicketForProject'),

    path('login/', views.userLogin, name = 'login'),
    path('logout/', views.userLogout, name = 'logout'),
    path('register/', views.userRegister, name = 'register'),

    path('create-project/', views.createProject, name = 'create-project'),
    path('update-project/<str:pk>/', views.updateProject, name = 'update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name = 'delete-project'),


    path('ticket/<str:pk>/', views.ticket, name = 'ticket'),
    path('create-ticket/', views.createTicket, name = 'create-ticket'),
    path('update-ticket/<str:pk>/', views.UpdateTicket, name = 'update-ticket'),
    path('update-ticket-admin/<str:pk>/', views.UpdateTicketAdmin, name = 'update-ticket-admin'),
    path('delete-ticket/<str:pk>/', views.deleteTicket, name = 'delete-ticket'),
    path('ticket-overview/', views.ticketOverview, name = 'ticket-overview'),
    
    path('update-comment/<str:pk>/', views.updateComment, name = 'update-comment'),

    path('profile-list/', views.profileList, name = 'profile-list'),
    path('profile/<str:pk>/', views.userProfile, name = 'profile-page'),
    path('update-profile/<str:pk>/', views.updateProfile, name = 'update-profile'),


    path('joe/', views.joe, name = 'joemama'),
    path('pager/<str:pk>/', views.pager, name = 'pager'),

]
