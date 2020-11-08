from django.urls import path
from . import views
from .views import postlistview,postdetailview,postcreateview,postupdateview,postdeleteview,userpostlistview


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',postlistview.as_view(), name='home'),
    path('user/<str:username>',userpostlistview.as_view(), name='user-posts'),
    path('post/<int:pk>/',postdetailview.as_view(), name='post-detail'),
    path('post/new/',postcreateview.as_view(), name='post-create'),
    path('about/',views.about,name='about'),
    path('post/<int:pk>/update',postupdateview.as_view(), name='post-update'),
    path('post/<int:pk>/delete',postdeleteview.as_view(), name='post-delete'),
]