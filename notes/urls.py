from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views


urlpatterns = [
    path('accounts/login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.library , name="library"),
    path('book/<slug>/', views.bookDetail, name="book"),
    path('add/<slug>/', views.addNote, name='add'),
    path('mynotes/', views.myNotes, name='mynotes')
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
