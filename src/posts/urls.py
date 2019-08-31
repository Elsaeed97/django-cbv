from django.urls import path
from posts.views import HomePage, PostsDetail, PostCreate, PostUpdate,PostDelete
urlpatterns = [ 
    path('', HomePage.as_view(), name='home' ),
    path('<int:pk>/', PostsDetail.as_view(), name='detail'),
    path('create/', PostCreate.as_view(), name='create' ),
    path('update/<int:pk>', PostUpdate.as_view(), name='update'),
    path('confirm_delete/<int:pk>', PostDelete.as_view(), name='delete')
]
