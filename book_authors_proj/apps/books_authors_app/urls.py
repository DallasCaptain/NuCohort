from django.conf.urls import url
from django.urls import path
from . import views
                    
urlpatterns = [
    url(r'^$', views.books),
    url(r'^addbook$', views.newbook),
    path('book/<int:id>', views.book),
    path('book/addauthor', views.addauthor),
    path('authors',views.authors),
    path('addauthor', views.newauthor),
    path('author/<int:id>', views.author),
    path('author/addbook', views.addbook)
]