from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template import Context, Template
from django.template.context_processors import csrf
from Sidefi.forms import IngresarEstudiante, IngresarVisita
from django.forms.models import modelformset_factory
from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.core.exceptions import ValidationError
from Sidefi.models import Centro, Individuo, Visita, Parametros, Altura, Peso, IMC
import datetime
import csv



def signin (request):

    contexto = Context({"mensaje": ""})
    contexto.update(csrf(request))
    
    # # Si el usuario ya esta autenticado, muestra su pagina principal
    # if request.user.is_authenticated():
    #     return redirect("http://sidefi.herokuapp.com/")

    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        #Crear un objeto user si el usuario es autenticado correctamente
        user = auth.authenticate(username=username, password=password)


        if user is not None and user.is_active:

            #Hacer el login
            auth.login(request, user)
        
            # Guardar la escuela asignada al usuario
            micentro = Centro.objects.filter(encargado=request.user.id)
            
            request.session["MiCentroId"] = micentro[0].id
            return redirect("http://sidefi.herokuapp.com/")
            ## Que hacer si no tiene centro asignado
            
        
        else:
            # captcha = CaptchaForm()
            # contexto['captcha'] = captcha
            return render_to_response("signin.html", contexto)
    else:

        # captcha = CaptchaForm()
        # contexto['captcha'] = captcha
        return render_to_response("signin.html", contexto)



def logout (request):
    auth.logout(request)
    return HttpResponseRedirect("/")




def principal(request):
    return render(request, "principal.html")




#===============================================================================================


def signin2 (request):

    contexto = Context({"mensaje": ""})
    contexto.update(csrf(request))
    
    # Si el usuario ya esta autenticado, muestra su pagina principal
    if request.user.is_authenticated():
        return redirect("http://sidefi.herokuapp.com/")

    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        #Crear un objeto user si el usuario es autenticado correctamente
    
        user = auth.authenticate(username=username, password=password)

    
        #Comprobar la autenticacion y que el usuario esta activo para proceder
        #a conceder el acceso

        if user is not None and user.is_active:

            #Hacer el login
            auth.login(request, user)
        
            # Guardar la escuela asignada al usuario
            micentro = Centro.objects.filter(encargado=request.user.id)
            
            request.session["MiCentroId"] = micentro[0].id
            return redirect("http://sidefi.herokuapp.com/")
            ## Que hacer si no tiene centro asignado
            
        
        else:

            return render_to_response("signin.html", contexto)
        
    return render(request, "signin.html")



def logout (request):
    auth.logout(request)
    return HttpResponseRedirect("/")




def principal(request):
    return render(request, "principal.html")




#===============================================================================================
# Vista Dashboard
#===============================================================================================

def vistaDashboard(request):

    # Comprobar que el usuario esta autenticado

    if not request.user.is_authenticated():
        return redirect("http://sidefi.herokuapp.com/signin")


    micentro = Centro.objects.get(id=request.session["MiCentroId"])

   
    #Variable de contexto   
    contexto = Context(
                {"usuario":request.user.username,
                "nombre":request.user.first_name+" " +request.user.last_name,
                "centro": str(micentro.nombre) + " en " + str(micentro.distrito)})

    try:        
        parametro = Parametros.objects.get(estatus="I")
        contexto['procesoid'] = parametro.id
        contexto['procesonombre'] = parametro.codigo
        contexto['edadminima'] = parametro.rangoEdad[:2]
        contexto['edadmaxima'] = parametro.rangoEdad[3:]
        fecha_ref = parametro.fecha_ref
    except Exception as e:
        print str(e)

        
    
    poblacionActiva = Individuo.objects.values_list('activo',
     flat=True).filter(activo="S", centro=request.session["MiCentroId"])

    poblacionActiva = len(poblacionActiva)

    # misestudiantes = Individuo.objects.filter(centro=request.session["MiCentroId"])

    estudiantes = Individuo.objects.filter(
         centro=request.session["MiCentroId"], activo="S").select_related()

    
    poblacioncondatos = 0
    
    for e in estudiantes:
        v = e.visita_set.filter(individuo = e.id, creada__gte = fecha_ref)

        if len(v) == 1:  #Tiene una visita registrada
            poblacioncondatos += 1
    
        
    contexto["poblaciontotal"] = poblacionActiva
    
    contexto["poblacioncondatos"] = poblacioncondatos
    
    contexto["poblacionsindatos"] = poblacionActiva - poblacioncondatos

    try:
        progreso = round((float(poblacioncondatos)/poblacionActiva)*100)
    except:
        progreso = 0

    
    progreso = str(int(progreso)) + "%"
    contexto["progreso"] = progreso

    contexto["fecha_ref"] = fecha_ref

    contexto["codigovisita"] = Parametros.objects.get(estatus="I")



    return render_to_response("dashboard.html", contexto)





#===============================================================================================
# Vista ingreso de Estudiantes
#===============================================================================================

def IngresoEstudiante(request, identificador):

    try:

        if not request.user.is_authenticated():
            return redirect("http://sidefi.herokuapp.com/signin")
        
        micentro = Centro.objects.get(id=request.session["MiCentroId"])

        contexto = Context({
                "usuario":request.user.username,
                "nombre":request.user.first_name+" " +request.user.last_name,
                "centro": str(micentro.nombre) + " - " + str(micentro.distrito),
                "centro_id" : micentro.id})

        contexto.update(csrf(request))
    
        formDict = dict()  # Diccionario para almacenar los datos del formulario
        estudiante = None  # Variable para almacenar objeto estudiante

    except Exception as e:        
    
        contexto["mensaje"] = "Error 1 - " + str(e)
        return render(request, "ingreso_estudiante.html", contexto)
    
   
    try:

        estudiante = Individuo.objects.get(id=int(identificador))
        
    
    except:

        estudiante = Individuo()
        


    if request.method == "POST":

        try:
            estudiante.nombre = request.POST['nombre_estudiante']
            estudiante.genero = request.POST['genero']

            # Convertir string a objeto tipo fecha 
            f = datetime.datetime.strptime(request.POST['fecha_nac'], "%d/%m/%Y").date()

            estudiante.fecha_nac = f

            estudiante.activo = request.POST['activo']
            estudiante.centro = micentro
        except:
            pass

        try:

            estudiante.full_clean()

        except ValidationError as e:

            contexto["mensaje"] = "Debe llenar todos los campos. Revise y vuelva a intentarlo."
            
            formDict["nombre_estudiante"] = request.POST['nombre_estudiante']
            formDict["activo"] = request.POST['activo']          
            formDict["fecha_nac"] = request.POST['fecha_nac']
            formDict["genero"] = request.POST['genero']

            contexto["datos"] = formDict


            return render(request, "ingreso_estudiante.html", contexto)
        
        else:
            estudiante.save()
            #contexto["mensaje"] = "Registro guardado."
            return render(request, "ingreso_estudiante.html", contexto)

    else:
        
        try:
            formDict["nombre_estudiante"] = estudiante.nombre

            try:
                fecha = estudiante.fecha_nac.strftime('%d/%m/%Y')
            except:
                fecha = ""

            formDict["fecha_nac"] = fecha
            formDict["activo"] = estudiante.activo           
            formDict["centro"] = contexto["centro"]
            formDict["genero"] = estudiante.genero

            contexto["datos"] = formDict

            return render(request, "ingreso_estudiante.html", contexto)

        except Exception as e:          
    
            contexto["mensaje"] = "Error 4 -"  + str(e)

            return render(request, "ingreso_estudiante.html", contexto)


#===============================================================================================
# Vista Tabla de estudiantes
#===============================================================================================

def vistaEstudiantes(request):

    try:

        # Comprobar que el usuario esta autenticado

        if not request.user.is_authenticated():
            return redirect("http://sidefi.herokuapp.com/signin")


        micentro = Centro.objects.get(id=request.session["MiCentroId"])

        #Variable de contexto   
        contexto = Context(
                    {"usuario":request.user.username,
                    "nombre":request.user.first_name+" " +request.user.last_name,
                    "centro": str(micentro.nombre) + " en " + str(micentro.distrito)})

        try:        
            #Parametros
            parametro = Parametros.objects.get(estatus="I")
            contexto['procesoid'] = parametro.id
            contexto['procesonombre'] = parametro.codigo
            contexto['edadminima'] = parametro.rangoEdad[:2]
            contexto['edadmaxima'] = parametro.rangoEdad[3:]
        except:
            formDict["mensaje"] = "Se produjo un error. Verificar los parametros del proceso activo."

            
        estudiantes = Individuo.objects.filter(centro=request.session["MiCentroId"])

        # Calcular la edad actual

        def dif_meses (fecha):
            try:
                hoy = datetime.datetime.now()
                e = (hoy.year - fecha.year)*12 + (hoy.month - fecha.month)
                return e
            except:
                return 0
            
        
        datos1=[]

        for e in estudiantes:

            datos1.append({'nombre': e.nombre,
                        'genero' : e.genero,
                        'fecha_nac' : e.fecha_nac,
                        'id' : e.id,
                        'activo': e.activo,
                        'edad_actual' : dif_meses(e.fecha_nac),
                            })

        contexto["poblaciontotal"] = len(datos1)

        contexto["datos"] = datos1

        return render_to_response("estudiantes.html", contexto)


    except:
        contexto["mensaje"] = "Error vistaEstudiantes. Por favor, notifique al administrador."
        return render_to_response("estudiantes.html", contexto)
    

    return render_to_response("estudiantes.html", contexto)


#===============================================================================================
# Vista Tabla Mediciones
#===============================================================================================

def vistaMediciones(request):

    # Comprobar que el usuario esta autenticado

    if not request.user.is_authenticated():
        return redirect("http://sidefi.herokuapp.com/signin")


    micentro = Centro.objects.get(id=request.session["MiCentroId"])

    #Fecha de referencia, inicio de la toma de medidas
    #Los estudiantes solo tendran un registro despues de esta fecha
    fecha_ref = Parametros.objects.get(estatus="I").fecha_ref

    #Variable de contexto   
    contexto = Context(
                {"usuario":request.user.username,
                "nombre":request.user.first_name+" " +request.user.last_name,
                "centro": str(micentro.nombre) + " en " + str(micentro.distrito)})

        
    #misestudiantes = Individuo.objects.filter(centro=request.session["MiCentroId"])

    estudiantes = Individuo.objects.filter(
        centro=request.session["MiCentroId"], activo="S").select_related()

    datos1=[]
    
    for e in estudiantes:
        v = e.visita_set.filter(individuo = e.id, creada__gte = fecha_ref)

        if len(v) == 1:  #Tiene una visita registrada
            fecha = v[0].creada
            edad_medicion = v[0].edad
        else:
            fecha = None
            edad_medicion = None
        
        datos1.append({'nombre': e.nombre,
                    'genero' : e.genero,
                    'fecha_nac' : e.fecha_nac,
                    'fecha_visita' : fecha,
                    'id' : e.id,
                    'activo': e.activo,
                    'edad_medicion':edad_medicion,

                        })


    # datos =[]
    # for v in Visita.objects.select_related():

    #     datos.append({'nombre': v.individuo.nombre,
    #                     'genero' : v.individuo.genero,
    #                     'fecha_nac' : v.individuo.fecha_nac,
    #                     'fecha_visita' : v.creada,
    #                     'id' : v.individuo.id,
    #                     'edad_medicion' : v.edad,
    #                     })
    
        
    contexto["poblaciontotal"] = len(datos1) #misestudiantes.count()
    
    # contexto["poblacioncondatos"] = len(datos)
    
    # contexto["poblacionsindatos"] = contexto["poblaciontotal"] - contexto["poblacioncondatos"]

    contexto["fecha_ref"] = fecha_ref

    contexto["codigovisita"] = Parametros.objects.get(estatus="I")

    contexto["datos"] = datos1
    

    return render_to_response("mediciones.html", contexto)

    #except:
    #   print "Estoy aqui +========================="
    return render_to_response("mediciones.html", contexto)


#===============================================================================================
# Vista ingreso de Visita o mediciones
#===============================================================================================


def IngresoVisita(request, identificador):
    
    
    if not request.user.is_authenticated():
        return redirect("http://sidefi.herokuapp.com/signin")

    formDict = dict()  # Diccionario para almacenar los datos del formulario
    

    try:

        micentro = Centro.objects.get(id=request.session["MiCentroId"])

        contexto = Context({
            "usuario":request.user.username,
            "nombre":request.user.first_name+" " +request.user.last_name,
            "centro": str(micentro.nombre) + " - " + str(micentro.distrito)})

        contexto.update(csrf(request))

    except:
        formDict["mensaje"] = "Se produjo un error. Verificar asignacion del centro."


        # Obtener los datos para llenar el formulario
        # Los valores del codigo de ingreso de medidas, y los de referencia no se cambian

    try:        
        #Parametros
        parametro = Parametros.objects.get(estatus="I")
        formDict['procesoid'] = parametro.id
        formDict['procesonombre'] = parametro.codigo
        formDict['edadminima'] = parametro.rangoEdad[:2]
        formDict['edadmaxima'] = parametro.rangoEdad[3:]
    except:
        contexto["mensaje"] = "Se produjo un error. Verificar los parametros del proceso activo."


    try:
        # Obtener datos del estudiante
        estudiante = Individuo.objects.get(id=identificador)
        formDict['nombre'] = estudiante.nombre

        # Obtener la edad
        # Metodo que calcula la cantidad de meses entre dos fechas
        
        def dif_meses (fecha):
            hoy = datetime.datetime.now()
            e = (hoy.year - fecha.year)*12 + (hoy.month - fecha.month)
            return e

        # El campo fecha_nac contiene un objeto!!!
        meses = dif_meses(estudiante.fecha_nac)
        f= estudiante.fecha_nac.strftime('%d-%b-%Y')

        formDict['fecha_nac'] = f
        formDict['edad'] = meses

        # Obtener el sexo
        sexo = estudiante.genero
        formDict['genero'] = sexo

    except:
        contexto["mensaje"] = "Se produjo un error. Verificar los datos del estudiante."
        # Obtener datos antropometricos de referencia

    try:
        altura = (Altura.objects.filter(edad = meses, genero=sexo)).values()[0]
        peso = Peso.objects.filter(edad = meses, genero=sexo).values()[0]
        imc = IMC.objects.filter(edad = meses, genero=sexo).values()[0]

        #Altura
        formDict["a1"] = str(altura["dem3"])
        formDict["a2"] = str(altura["dem2"])
        formDict["a3"] = str(altura["dem1"])
        formDict["a4"] = str(altura["mediana"])
        formDict["a5"] = str(altura["de1"])
        formDict["a6"] = str(altura["de2"])
        formDict["a7"] = str(altura["de3"])

        listAltura = [None] * 7
        listAltura[0] = altura["dem3"]
        listAltura[1] = altura["dem2"]
        listAltura[2] = altura["dem1"]
        listAltura[3] = altura["mediana"]
        listAltura[4] = altura["de1"]
        listAltura[5] = altura["de2"]
        listAltura[6] = altura["de3"]


        #Peso
        formDict["p1"] = str(peso["dem3"])
        formDict["p2"] = str(peso["dem2"])
        formDict["p3"] = str(peso["dem1"])
        formDict["p4"] = str(peso["mediana"])
        formDict["p5"] = str(peso["de1"])
        formDict["p6"] = str(peso["de2"])
        formDict["p7"] = str(peso["de3"])

        listPeso = [None] * 7
        listPeso[0] = peso["dem3"]
        listPeso[1] = peso["dem2"]
        listPeso[2] = peso["dem1"]
        listPeso[3] = peso["mediana"]
        listPeso[4] = peso["de1"]
        listPeso[5] = peso["de2"]
        listPeso[6] = peso["de3"]       


        #IMC
        formDict["i1"] = str(imc["dem3"])
        formDict["i2"] = str(imc["dem2"])
        formDict["i3"] = str(imc["dem1"])
        formDict["i4"] = str(imc["mediana"])
        formDict["i5"] = str(imc["de1"])
        formDict["i6"] = str(imc["de2"])
        formDict["i7"] = str(imc["de3"])

        listImc = [None] * 7
        listImc[0] = imc["dem3"]
        listImc[1] = imc["dem2"]
        listImc[2] = imc["dem1"]
        listImc[3] = imc["mediana"]
        listImc[4] = imc["de1"]
        listImc[5] = imc["de2"]
        listImc[6] = imc["de3"]


    except:
        contexto["mensaje"] = "Edad fuera de rango o " + \
        "no fue posible obtener los datos antropometricos para esta edad."


    if request.method == "POST":

        try:    

            visita = Visita.objects.filter(individuo = identificador, 
                codigo = formDict['procesoid']).values()

            obj = Visita.objects.get(id=visita[0]['id'])

            obj.pesoVisita = request.POST['pesoVisita']
            obj.alturaVisita = request.POST['alturaVisita']
            obj.imcVisita = request.POST['imcVisita']
            obj.pesoReferencia = zscore(listPeso, request.POST['pesoVisita'])
            obj.alturaReferencia = zscore(listAltura, request.POST['alturaVisita'])
            obj.imcReferencia = zscore(listImc, request.POST['imcVisita'])

            if validar(listPeso, request.POST['pesoVisita']):
                if validar(listAltura, request.POST['alturaVisita']):
                    obj.save()
            
            return HttpResponseRedirect("/ingreso_visita/" + str(identificador))

        except:

            try:
        
                v = Visita(codigo = parametro,
                    individuo = estudiante,
                    edad = meses,

                    pesoVisita = request.POST['pesoVisita'],
                    alturaVisita = request.POST['alturaVisita'],
                    imcVisita = request.POST['imcVisita'],
                    
                    pesoReferencia = zscore(listPeso, request.POST['pesoVisita']),
                    alturaReferencia = zscore(listAltura, request.POST['alturaVisita']),
                    imcReferencia = zscore(listImc, request.POST['imcVisita']))
                
                if validar(listPeso, request.POST['pesoVisita']):
                    if validar(listAltura, request.POST['alturaVisita']):
                        v.save()
            
                return HttpResponseRedirect("/ingreso_visita/" + str(identificador))
            
            except:
            
                return HttpResponseRedirect("/ingreso_visita/" + str(identificador))

        
    else:

        # Determinar si el estudiante ya tiene datos registrado
        try:    
            visitaexiste = Visita.objects.filter(individuo = identificador, 
                codigo = formDict['procesoid']).values()
            
            peso = str(visitaexiste[0]['pesoVisita'])
            altura = str(visitaexiste[0]['alturaVisita'])
            imc = str(visitaexiste[0]['imcVisita'])

            formDict['zpeso'] = str(visitaexiste[0]['pesoReferencia'])
            formDict['zaltura']= str(visitaexiste[0]['alturaReferencia'])
            formDict['zimc']= str(visitaexiste[0]['imcReferencia'])


            # Pasar datos para presentar en el formulario
            if len(visitaexiste)> 0:
                contexto['mensaje2'] = "Este estudiante ya tiene mediciones registradas. " \
                                    + "Puede modificar y actualizar los datos si es necesario."
                formDict['pesoregistrado'] = peso
                formDict['alturaregistrada'] = altura
                formDict['imcregistrado'] = imc

            contexto["datos"] = formDict
        
            return render(request, "ingreso_visita.html", contexto)


        except:

            formDict['mensaje'] = "Registro de visita nuevo"

            if meses > formDict['edadmaxima'] or meses < formDict['edadminima']:
                formDict['mensaje'] = "Edad fuera del rango: " +\
                  str(formDict['edadminima']) + " - " + str(formDict['edadmaxima']) + " meses."

            contexto["datos"] = formDict
        
            return render(request, "ingreso_visita.html", contexto)
    
    return render(request, "ingreso_visita.html", contexto)

    


#===============================================================================================
# Funciones de ayuda
#===============================================================================================

def zscore(refList, x):

        ans = None
        x = float(x)

        #Antes valido los datos
        if len(refList) != 7:
            print "Lista de referencia de puntajes Z no es correcta"
            return
            
        #Primero averiguo si es el valor medio
        if x == refList[3]:
            ans = 0
            
        # #Luego averiguo si se sale por la derecha
        # if x > refList[6]:
        #     print str(x) + " es mayor que el valor superior de la lista"
                
        # #Luego averiguo si se sale por la izquierda
        # if x < refList[0]:
        #     print str(x) + " es menor que el valor inferior de la lista"
            
        if x > refList[3]:
            if x < refList[4]:
                ans = 1
            elif x < refList[5]:
                ans = 2
            elif x <= refList[6]:
                ans = 3
        elif x < refList[3]:
            if x > refList[2]:
                ans = -1
            elif x > refList[1]:
                ans = -2
            elif x >= refList[0]:
                ans = -3

        return ans


#===============================================================================================
# Funcion que valida que las mediciones estan dentro del rango
#===============================================================================================


def validar(refList, x):
    ans = None
    x = float(x)

    if x >= min(refList) and x <= max(refList):
        ans = True
    else:
        ans = False

    # print min(refList)
    # print max(refList),
    # print type(max(refList))
    # print x
    return ans




#===============================================================================================
# Exportar a CSV
#===============================================================================================


class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def exportar_estudiantes(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.

    #----------------------------------------------------------------------------------#

    try:

        micentro = Centro.objects.get(id=request.session["MiCentroId"])


        contexto = Context(
                    {"usuario":request.user.username,
                    "centro": str(micentro.nombre) + "-"+ str(micentro.distrito)})

        #Parametros
        parametro = Parametros.objects.get(estatus="I")
        contexto['procesoid'] = parametro.id
        contexto['procesonombre'] = parametro.codigo
            
        estudiantes = Individuo.objects.filter(centro=request.session["MiCentroId"])


        # Calcular la edad actual
        def dif_meses (fecha):
            try:
                hoy = datetime.datetime.now()
                e = (hoy.year - fecha.year)*12 + (hoy.month - fecha.month)
                return e
            except:
                return 0
            

        #Ensambalar el archivo CSV

        header = ["id","nombre","genero","fecha_nac","edad_actual","activo"]


        datos = [header,]

        for e in estudiantes:
            edad = dif_meses(e.fecha_nac)
            datos.append([e.id, e.nombre, e.genero, e.fecha_nac, edad, e.activo])
        

    except Exception as i:
        
        print str(i)
    


    #----------------------------------------------------------------------------------#
    try:

        rows = datos
        
        pseudo_buffer = Echo()
            
        writer = csv.writer(pseudo_buffer)
            
        response = StreamingHttpResponse((writer.writerow(row) for row in rows), content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="estudiantes.csv"'
            
        return response


    except Exception as i:

        print str(i)


def exportar_visitas(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.

    #----------------------------------------------------------------------------------#

    try:

        visitas = Visita.objects.all()

        

        #Ensambalar el archivo CSV

        header = ["nombre","peso","altura","imc","zP","zA","zI","Fecha"]


        datos = [header,]

        #datos = []

        for e in visitas:
            datos.append([e.individuo, e.pesoVisita, e.alturaVisita, e.imcVisita, 
                e.pesoReferencia, e.alturaReferencia, e.imcReferencia, e.creada])
        

    except Exception as i:
        
        print str(i)
    


    #----------------------------------------------------------------------------------#
    try:

        rows = datos
        
        pseudo_buffer = Echo()
            
        writer = csv.writer(pseudo_buffer)
            
        response = StreamingHttpResponse((writer.writerow(row) for row in rows), content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="visitas.csv"'
            
        return response


    except Exception as i:

        print str(i)



#===============================================================================================
# graficos
#===============================================================================================


def charts(request):



    # Comprobar que el usuario esta autenticado

    if not request.user.is_authenticated():
        return redirect("http://sidefi.herokuapp.com/signin")


    micentro = Centro.objects.get(id=request.session["MiCentroId"])

    #Variable de contexto   
    contexto = Context(
                {"usuario":request.user.username,
                "nombre":request.user.first_name+" " +request.user.last_name,
                "centro": str(micentro.nombre) + " en " + str(micentro.distrito)})


    estudiantes = Individuo.objects.filter(centro=request.session["MiCentroId"],
        activo="S")

    # ============== Poblacion estudiantil ===============
    poblacion={}

    for e in estudiantes:
        poblacion[e.genero] = poblacion.get(e.genero,0)+1
        


    # ============== Peso para la edad ===================

    estudiantes = estudiantes.select_related()

    fecha_ref = Parametros.objects.get(estatus="I").fecha_ref

    l = [["-3DE", 0],["-2DE", 0],["-1DE", 0],["N", 0],["+1DE", 0],["+2DE", 0],["+3DE", 0]]
    

    for e in estudiantes:
        v = e.visita_set.filter(individuo = e.id, creada__gte = fecha_ref)

        if len(v) == 1:  #Tiene una visita registrada
            valor = v.values("pesoReferencia")[0]["pesoReferencia"]
            
            if valor == -3:
                l[0][1] += 1
            if valor == -2:
                l[1][1] += 1
            if valor == -1:
                l[2][1] += 1
            if valor == 0:
                l[3][1] += 1
            if valor == 1:
                l[4][1] += 1
            if valor == 2:
                l[5][1] += 1
            if valor == 3:
                l[6][1] += 1
            

       
    print l
       
    #contexto["poblacion"] = poblacion

    contexto["peso"] = l


    return render(request, 'charts.html', contexto)