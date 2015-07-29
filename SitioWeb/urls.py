from django.conf.urls import patterns, include, url
from django.contrib import admin
from Sidefi import views


admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'SitioWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^SitioWeb/', include(SitioWeb.urls)),
    
    # url (r'^signin/', 'Sidefi.views.signin', name="signin"), 
    
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
    
]

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)

