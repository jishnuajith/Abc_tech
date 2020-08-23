from django.urls import path
from Emp_management import views

urlpatterns = [
    path('', views.home),
    path('signin/', views.signinPage),
    path('admin/dashboard', views.signin, name='adminsignin'),
    path('admin/insert', views.emp, name='emp'),
    path('admin/show', views.show, ),
    path('admin/edit/<int:id>', views.edit),
    path('admin/update/<int:id>', views.update),
    path('admin/delete/<int:id>', views.destroy),
    path('admin/signout',views.signout)

]

# path('signin/show', views.show, ),
#     path('signin/edit/<int:id>', views.edit),
#     path('signin/update/<int:id>', views.update),
#     path('signin/delete/<int:id>', views.destroy),
#     path('signin/dashboard', views.signin, name='adminsignin'),
#     path('signin/', views.signinPage, ),
#     path('signin/insert', views.emp, name='emp'),
# path('signin/adminpanel/', views.emp,),

# path('signin/', views.empChecking, name='empsignin')
