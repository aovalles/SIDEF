from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Regional(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60, blank=True)
    telefono = models.CharField(max_length=11, blank=True)
    encargado = models.ManyToManyField('UserProfile')

    class Meta: 
        ordering = ["nombre"] 
        verbose_name_plural = "Regionales" 
 
    def __unicode__(self):
        return '%s' %(self.nombre) 



class Distrito(models.Model):
    nombre = models.CharField(max_length=30)
    regional = models.ForeignKey('Regional')
    #encargado = models.ManyToManyField('UserProfile')
    direccion = models.CharField(max_length=60, blank=True)
    telefono = models.CharField(max_length=11, blank=True)

    class Meta:
        #unique_together = ("codigo", "regional")
        ordering = ["nombre"] 
        verbose_name_plural = "Distritos" 
 
    def __unicode__(self):
        return '%s - %s' %(self.nombre, self.regional) 


        

class Centro(models.Model):
    nombre = models.CharField(max_length=50)
    distrito = models.ForeignKey('Distrito')
    direccion = models.CharField(max_length=60, blank=True)
    telefono = models.CharField(max_length=11, blank=True)
    encargado = models.ManyToManyField('UserProfile')

    class Meta: 
        ordering = ["nombre"] 
        verbose_name_plural = "Centros" 
 
    def __unicode__(self):
        return '%s - %s' %(self.nombre, self.distrito) 


class Individuo(models.Model):
    Genero_Opciones = (('M', 'Masculino'),('F', 'Femenino'),)
    Activo_Opciones = (('S', 'Si'),('N', 'No'),)
    
    genero = models.CharField(max_length=1, choices=Genero_Opciones, blank=False) 
    nombre = models.CharField(max_length=30, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False, verbose_name = "Fecha de Nac.")
    centro = models.ForeignKey('Centro')
    
    # Eliminado S=si N=no
    activo = models.CharField(max_length=1, choices=Activo_Opciones, blank=False)

    class Meta: 
        ordering = ["nombre"]
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes" 
 
    def __unicode__(self):
        return (self.nombre)

    
    # metodo que calcule la edad a partir de la fecha actual
        
    # def calcula_edad(self):
    #     import datetime

    #     #mydate = datetime.datetime.strptime(fecha_nac, "%d-%m-%y")
    #     return int((datetime.datetime.now() - self.fecha_nac).days / 30)

    # edad = property(calcula_edad)



class Visita(models.Model):
    
    Activo_Opciones = (('S', 'Si'),('N', 'No'),)

    codigo = models.ForeignKey('Parametros', null=False, verbose_name="Codigo de la visita")

    individuo = models.ForeignKey('Individuo')
    
    edad = models.PositiveSmallIntegerField(blank=False, null=False, verbose_name="Edad") 
    
    pesoVisita = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False,
        verbose_name="Peso")

    alturaVisita = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False,
        verbose_name="Altura")

    imcVisita = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False,
        verbose_name="IMC")

    pesoReferencia = models.SmallIntegerField(verbose_name="Peso - Puntaje Z ")
    alturaReferencia = models.SmallIntegerField(verbose_name="Altura - Puntaje Z")
    imcReferencia = models.SmallIntegerField(verbose_name="IMC - Puntaje Z")

    creada = models.DateTimeField(auto_now_add=True)
    modificada = models.DateTimeField(auto_now=True)

    activo = models.CharField(max_length=1, choices=Activo_Opciones, blank=False, default="S")
    


    class Meta: 
        ordering = ["creada"] 
        verbose_name_plural = "Visitas" 
 
    
    # La clase visita tiene un metodo de instancia para calcular los puntajes Z

    # def zscore(self, refList, x):

    #     # print "Buscando " + str(x)
    #     # ans = None
    #     x = float(x)

    #     #Antes valido los datos
    #     if len(refList) != 7:
    #         print "Lista de referencia de puntajes Z no es correcta"
    #         return
            
    #     #Primero averiguo si es el valor medio
    #     if x == refList[3]:
    #         ans = 0
            
    #     #Luego averiguo si se sale por la derecha
    #     if x > refList[6]:
    #         print str(x) + " es mayor que el valor superior de la lista"
                
    #     #Luego averiguo si se sale por la izquierda
    #     if x < refList[0]:
    #         print str(x) + " es menor que el valor inferior de la lista"
            
    #     if x > refList[3]:
    #         if x < refList[4]:
    #             ans = 1
    #         elif x < refList[5]:
    #             ans = 2
    #         elif x <= refList[6]:
    #             ans = 3
    #     elif x < refList[3]:
    #         if x > refList[2]:
    #             ans = -1
    #         elif x > refList[1]:
    #             ans = -2
    #         elif x >= refList[0]:
    #             ans = -3

    #     return ans


    # #### Fin del metodo para calcular el puntaje Z




class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)
    #nombre = models.CharField(max_length=30)
    #email = models.EmailField(blank=True, verbose_name="E-mail")

    telefono = models.CharField(max_length=12, blank=True)
    extension = models.CharField(max_length=12, blank=True)
    celular = models.CharField(max_length=12, blank=True)
    es_digitador = models.BooleanField(default=False)


    def __unicode__(self):
        return (self.user_auth.username)

    
    class Meta: 
        
        verbose_name_plural = "Perfiles de usuarios" 



class Altura(models.Model):
    Genero_Opciones = (('M', 'Masculino'),('F', 'Femenino'),)
    
    genero = models.CharField(max_length=1, choices=Genero_Opciones) 
    edad = models.IntegerField(blank=False, null=False)
    dem3 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='-3de')
    dem2 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='-2de')
    dem1 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='-1de')
    mediana = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False)
    de1 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='+1de')
    de2 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='+2de')
    de3 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='+3de')


    class Meta: 
        ordering = ["edad"] 
        verbose_name_plural = "Altura para la edad" 
 
    def __unicode__(self):
        return '%s - %s' % (self.genero, self.edad)


class Peso(models.Model):
    Genero_Opciones = (('M', 'Masculino'),('F', 'Femenino'),)
    
    genero = models.CharField(max_length=1, choices=Genero_Opciones)
    edad = models.IntegerField(blank=False, null=False)
    dem3 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='-3de')
    dem2 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='-2de')
    dem1 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='-1de')
    mediana = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False)
    de1 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='+1de')
    de2 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='+2de')
    de3 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='+3de')

    class Meta: 
        ordering = ["edad"] 
        verbose_name_plural = "Peso para la edad" 
 
    def __unicode__(self):
        return '%s - %s' % (self.genero, self.edad)


class IMC(models.Model):
    Genero_Opciones = (('M', 'Masculino'),('F', 'Femenino'),)
    
    genero = models.CharField(max_length=1, choices=Genero_Opciones) 
    edad = models.IntegerField(blank=False, null=False)
    dem3 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='-3de')
    dem2 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='-2de')
    dem1 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='-1de')
    mediana = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False)
    de1 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='+1de')
    de2 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='+2de')
    de3 = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False, verbose_name='+3de')

    class Meta: 
        ordering = ["edad"] 
        verbose_name_plural = "Indice de masa corporal para la edad"
        
 
    def __unicode__(self):
        return '%s - %s' % (self.genero, self.edad)



class Parametros(models.Model):
    
    visita_opciones = (('C', 'Completa'),('I', 'Incompleta'),)

    fecha_ref = models.DateField()  #Fecha a tomar en cuenta como inicio de registro de medidas
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=1000)
    estatus = models.CharField(max_length=1, choices=visita_opciones)
    rangoEdad = models.CharField(max_length=6)

    class Meta: 
        verbose_name_plural = "Parametros"
    
    def __unicode__(self):
        return '%s' % (self.codigo)