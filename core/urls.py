"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from home.views import *
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import *
urlpatterns = [
    path('' , home),
    path('register-page/' , register),
    path('login/' , login_attempt),
    path('create-question/<quiz_id>/' , create_question),

    path('verify/<token>/' , verify_user_account),
    
    path('get-questions/' , get_questions),
    path('create-quiz/' , create_quiz),

    path('excel-import/' , excel_import),
    path('jet/', include('jet.urls', 'jet')), 
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()