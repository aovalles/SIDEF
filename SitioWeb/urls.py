from django.conf.urls import patterns, include, url
from django.contrib.auth.views import password_reset
from django.contrib import admin
from Sidefi import views


admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'SitioWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset',
     {'post_reset_redirect' : '/accounts/password/reset/done/'}),
    (r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
     {'post_reset_redirect' : '/accounts/password/done/'}),
    (r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),


    url(r'^admin/', include(admin.site.urls)),
    #url(r'^SitioWeb/', include(SitioWeb.urls)),
    
    url (r'^signin/', 'Sidefi.views.signin', name="signin"), 
    
    url (r'^logout/', 'Sidefi.views.logout', name="logout"), 

    url (r'^$', 'Sidefi.views.signin'), 

    url (r'^principal/$', 'Sidefi.views.principal'), 


    #url (r'^testform/', 'Sidefi.views.vistaVisita'), 
    
    url (r'^dashboard/$', 'Sidefi.views.vistaDashboard'), 
    

    url (r'^estudiantes/$', 'Sidefi.views.vistaEstudiantes'), 

    url (r'^mediciones/$', 'Sidefi.views.vistaMediciones'), 
	
	url (r'^ingreso_estudiante/(\d+)/$', 'Sidefi.views.IngresoEstudiante'), 

    url (r'^ingreso_visita/(\d+)/$', 'Sidefi.views.IngresoVisita'), 

    # Exportar a archivos CSV
    url (r'^export_e/$', 'Sidefi.views.exportar_estudiantes'), 
    url (r'^export_m/$', 'Sidefi.views.exportar_visitas'), 

    url(r'^charts/$', 'Sidefi.views.charts', name='charts'),
    url(r'^ayuda/$', 'Sidefi.views.ayuda', name='ayuda'),


    
]

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)

