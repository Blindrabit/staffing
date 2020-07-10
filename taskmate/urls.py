from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views
from user_app import views as user_views
from calendar_app import views as calendar_views
from shiftDB import views as shiftDB_views
from django.conf import settings
from django.conf.urls.static import static
#from shiftDB.tasks import shift_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('user_app.urls')),
    path('', todolist_views.index, name= 'index'),
    path('todolist/', include('todolist_app.urls')),
    path('about/', todolist_views.about, name='about'),
    path('contact/', todolist_views.contact, name='contact'),
    path('profile/', user_views.profile, name='profile'),
    path('', include('calendar_app.urls')),
    path('shifts/', shiftDB_views.shifts_view, name='shifts'),
    path('shifts_add/', shiftDB_views.shifts_add_view, name='shifts_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

