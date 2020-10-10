from django.urls import path
from . import views


urlpatterns = [
    path('<str:username>/list/', views.HistoryListView.as_view(), name='list'),
    path('detailhis/<int:pk>', views.HistoryDetailView.as_view(), name='detail_his'),
    path('createhis/', views.HistoryCreateView.as_view(), name='create_his'),
    path('createtag/', views.TagCreateView.as_view(), name='create_tag'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logoutfunc, name='logout'),
    path('update/<int:pk>', views.HistroyUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.HistoryDeleteView.as_view(), name='delete'),
    path('search_user', views.SearchUserView.as_view(), name='search_user')
]
