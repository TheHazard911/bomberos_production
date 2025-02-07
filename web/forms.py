from django import forms
from.models import *
from django.db.models import Q
from django.db.models import Case, When

def Asignar_ops_Personal(): 
    jerarquias = [ "General", "Coronel", "Teniente Coronel", "Mayor", "Capitán", "Primer Teniente", "Teniente", "Sargento Mayor", "Sargento Primero", "Sargento segundo", "Cabo Primero", "Cabo Segundo", "Distinguido", "Bombero" ] 
    personal = Personal.objects.filter(status="Activo").filter(rol="Bombero").order_by("id").exclude(id=4)
    personal_ordenado = personal.order_by( Case(*[When(jerarquia=nombre, then=pos) for pos, nombre in enumerate(jerarquias)]) )
    op = [("", "Seleccione Una Opcion")] 
    for persona in personal_ordenado: op.append((str(persona.id), f"{persona.jerarquia} {persona.nombres} {persona.apellidos}")) 
    return op 

def Asignar_ops_Solicitante(): 
    jerarquias = ["General", "Coronel", "Teniente Coronel", "Mayor", "Capitán", "Primer Teniente", "Teniente", "Sargento Mayor", "Sargento Primero", "Sargento segundo", "Cabo Primero", "Cabo Segundo", "Distinguido", "Bombero" ] 
    personal = Personal.objects.filter(status="Activo").filter(rol="Bombero").order_by("id").exclude(id=4)
    personal_ordenado = personal.order_by( Case(*[When(jerarquia=nombre, then=pos) for pos, nombre in enumerate(jerarquias)]) ) 
    op = [("", "Seleccione Una Opcion"), ("0", "Externo")] 
    for persona in personal_ordenado: op.append((str(persona.id), f"{persona.jerarquia} {persona.nombres} {persona.apellidos}")) 
    return op

def Asignar_op_Doctores():
    personal = Doctores.objects.all()
    op = [("", "Seleccione Una Opcion")]
    for persona in personal:
        op.append((f"{persona.doctor}", f"{persona.doctor}"))
    return op

def Asignar_op_Enfermeros():
    personal = Enfermeros.objects.all()
    op = [("", "Seleccione Una Opcion"), ("Otro", "Otro")]
    for persona in personal:
        op.append((f"{persona.enfermeros}", f"{persona.enfermeros}"))
    return op

def Asignar_op_Psicologa():
    personal = Psicologa.objects.all()
    op = [("", "Seleccione Una Opcion")]
    for persona in personal:
        op.append((f"{persona.psicologa}", f"{persona.psicologa}"))
    return op

def Asignar_op_Municipios():
    municipios = Municipios.objects.all()
    op = [("", "Seleccione Una Opcion")]
    for municipio in municipios:
        op.append((str(municipio.id), municipio))
    return op

def Asignar_op_Tipos_Procedimientos():
    op = [("", "Seleccione Una Opcion")]
    return op

def Asignar_opc_tipos_suministros():
     procedimientos = Tipo_Institucion.objects.all()
     op = [("", "Seleccione Una Opcion")]
     for procedimiento in procedimientos:
         op.append((str(procedimiento.id), procedimiento))
     return op
   
def Asignar_opc_tipos_apoyos():
     procedimientos = Tipo_apoyo.objects.all()
     op = [("", "Seleccione Una Opcion")]
     for procedimiento in procedimientos:
         op.append((str(procedimiento.id), procedimiento))
     return op
 
def Asignar_opc_motivo_prevencion():
     procedimientos = Motivo_Prevencion.objects.all()
     op = [("", "Seleccione Una Opcion")]
     for procedimiento in procedimientos:
         op.append((str(procedimiento.id), procedimiento))
     return op

def Asignar_opc_motivo_despliegue():
     procedimientos = Motivo_Despliegue.objects.all()
     op = [("", "Seleccione Una Opcion")]
     for procedimiento in procedimientos:
         op.append((str(procedimiento.id), procedimiento))
     return op
 
def Asignar_opc_motivo_fals_alarm():
   procedimientos = Motivo_Alarma.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.motivo))
   return op

def Asignar_opc_tipo_servicios():
   procedimientos = Tipo_servicios.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.serv_especiales))
   return op

def Asignar_opc_tipo_rescate():
   procedimientos = Tipo_Rescate.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo_rescate))
   return op

def Asignar_opc_tipo_incendio():
   procedimientos = Tipo_Incendio.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo_incendio))
   return op

def Asignar_opc_tipo_accidente():
   procedimientos = Tipo_Accidente.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo_accidente))
   return op

def Asignar_opc_motivos_riesgo():
   procedimientos = Motivo_Riesgo.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo_riesgo))
   return op

def Asignar_opc_motivos_riesgo_mitigacion():
   procedimientos = Mitigacion_riesgo.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo_servicio))
   return op

def Asignar_opc_avanzada():
   procedimientos = Motivo_Avanzada.objects.all()
   op = [("", "Seleccione Una Opcion")]

   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo_servicio))
   return op

def Asignar_opc_traslados():
   procedimientos = Tipos_Traslado.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo_traslado))
   return op

def Asignar_opc_cilindros():
   procedimientos = Tipo_Cilindro.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.nombre_cilindro))
   return op

def Asignar_op_Artificios():
   procedimientos = Tipos_Artificios.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo))
   return op

def Asignar_op_Investigacion():
   procedimientos = Tipos_Investigacion.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo_investigacion))
   return op

def Asignar_op_Comsion():
   procedimientos = Tipos_Comision.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id), procedimiento.tipo_comision))
   return op

def Asignar_Comercios():
   procedimientos = Comercio.objects.all()
   op = [("", "Seleccione Una Opcion")]
   for procedimiento in procedimientos:
       op.append((str(procedimiento.id_comercio), f"{procedimiento.id_comercio}: {procedimiento.nombre_comercio}"))
   return op


class FormularioBusquedaCedula(forms.Form):
    nacionalidad = forms.ChoiceField(choices=[("V", "V"),("E", "E") ], label="Nacionalidad")
    numero_cedula = forms.CharField(max_length=20, label="Número de Cédula")

class FormularioRegistroPersonal(forms.Form):
    opc = [
        ("", "Seleccione Una Opcion"),
        ("General", "General"),
        ("Coronel", "Coronel"),
        ("Teniente Coronel", "Teniente Coronel"),
        ("Mayor", "Mayor"),
        ("Capitán", "Capitán"),
        ("Primer Teniente", "Primer Teniente"),
        ("Teniente", "Teniente"),
        ("Sargento Mayor", "Sargento Mayor"),
        ("Sargento Primero", "Sargento Primero"),
        ("Sargento segundo", "Sargento segundo"),
        ("Cabo Primero", "Cabo Primero"),
        ("Cabo Segundo", "Cabo Segundo"),
        ("Distinguido", "Distinguido"),
        ("Bombero", "Bombero"),
    ]

    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")])
    cedula = forms.IntegerField()
    jerarquia = forms.ChoiceField(choices=opc, widget=forms.Select(attrs={"class": "disable-first-option"}))
    cargo = forms.CharField()
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    fecha_ingreso = forms.DateField(
        label="Fecha de Ingreso",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}))
    rol = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Administrativo", "Administrativo"), ("Bombero", "Bombero"), ("Civil", "Civil")], widget=forms.Select(attrs={"class": "disable-first-option"}))
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Activo", "Activo"), ("Jubilado", "Jubilado"), ("Incapacitado", "Incapacitado"), ("Fallecido", "Fallecido"), ("Cese", "Cese"), ("Comision de Servicios", "Comision de Servicios")], widget=forms.Select(attrs={"class": "disable-first-option"}))
    talla_camisa = forms.CharField()
    talla_pantalon = forms.CharField()
    talla_zapato = forms.CharField()
    grupo_sanguineo = forms.CharField()



# Form1
class SelectorDivision(forms.Form):
    op = [
        ("", "Seleccione una Opción"),
        ("1", "Rescate"),
        ("2", "Operaciones"),
        ("3", "Prevención"),
        ("4", "GRUMAE"),
        ("5", "Prehospitalaria"),
        ("6", "Enfermería"),
        ("7", "Servicios Médicos"),
        ("8", "Psicología"),
        ("9", "Capacitación"),
    ]
    opciones = forms.ChoiceField(
        label="Seleccionar División",
        choices=op,
        required=True, widget=forms.Select(attrs={"class": "disable-first-option"})
    )

# Form2 
class SeleccionarInfo(forms.Form):
    solicitante = forms.ChoiceField(choices=Asignar_ops_Solicitante(), required=False,
        widget=forms.Select(attrs={'class': 'disable-first-option'}))
    solicitante_externo = forms.CharField(required=False)
    unidad = forms.ChoiceField(choices=[("", "Seleccione Una Opcion")], required=False,
        widget=forms.Select(attrs={'class': 'disable-first-option'}))
    efectivos_enviados = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    jefe_comision = forms.ChoiceField(choices=Asignar_ops_Personal(), required=False,
        widget=forms.Select(attrs={'class': 'disable-first-option'}))

# Form3
class Datos_Ubicacion(forms.Form):
    opc = [("", "Seleccione una Opcion"),
        ("1", "La Concordia"),
        ("2", "Pedro Maria Morantes"),
        ("3", "San Juan Bautista"),
        ("4", "San Sebastian"),
        ("6", "Francisco Romero Lobo"),
    ]
    
    municipio = forms.ChoiceField(choices=Asignar_op_Municipios(), required=True,
        widget=forms.Select(attrs={'class': 'disable-first-option'}))
    parroquia = forms.ChoiceField(choices=opc, required=False,
        widget=forms.Select(attrs={'class': 'disable-first-option'}))
    direccion = forms.CharField()
    fecha =  forms.DateField(
        label="Fecha",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'))  # Especificar explícitamente el tipo de input

# Agregando Apartado Comisiones Presentes
class Datos_Comision(forms.Form):
    agregar = forms.BooleanField(required=False, label="Agregar Comision Presente")

class Comision_Uno(forms.Form):
    comision = forms.ChoiceField(choices=Asignar_op_Comsion, required=False, widget=forms.Select(attrs={"class": "disable-first-option"}))
    nombre_oficial = forms.CharField(required=False)
    apellido_oficial = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula_oficial = forms.CharField(max_length=60, required=False)
    nro_unidad = forms.CharField(max_length=60, required=False)
    nro_cuadrante = forms.CharField(max_length=60, required=False)
    agregar = forms.BooleanField(required=False, label="Agregar Segunda Comision Presente")

class Comision_Dos(forms.Form):
    comision = forms.ChoiceField(choices=Asignar_op_Comsion, required=False, widget=forms.Select(attrs={"class": "disable-first-option"}))
    nombre_oficial = forms.CharField(max_length=100, required=False)
    apellido_oficial = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula_oficial = forms.CharField(max_length=60, required=False)
    nro_unidad = forms.CharField(max_length=60, required=False)
    nro_cuadrante = forms.CharField(max_length=60, required=False)

    agregar = forms.BooleanField(required=False, label="Agregar Tercera Comision Presente")

class Comision_Tres(forms.Form):
    comision = forms.ChoiceField(choices=Asignar_op_Comsion, required=False, widget=forms.Select(attrs={"class": "disable-first-option"}))
    nombre_oficial = forms.CharField(max_length=100, required=False)
    apellido_oficial = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula_oficial = forms.CharField(max_length=60, required=False)
    nro_unidad = forms.CharField(max_length=60, required=False)
    nro_cuadrante = forms.CharField(max_length=60, required=False)

# Form4
class Selecc_Tipo_Procedimiento(forms.Form):
    tipo_procedimiento = forms.ChoiceField(choices=Asignar_op_Tipos_Procedimientos(), required=False, widget=forms.Select(attrs={"class": "disable-first-option"}))

# Formulario Principal de Enfermeria
class Formulario_Enfermeria(forms.Form):
    opc = [("", "Seleccione Una Opcion"),("Cuartel Central", "Cuartel Central"), ("Estacion 1", "Estacion 1"), ("Estacion 2", "Estacion 2"), ("Estacion 3", "Estacion 3")]

    dependencia = forms.ChoiceField(choices=opc, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    encargado_area = forms.ChoiceField(choices=Asignar_op_Enfermeros, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    especifique = forms.CharField(required=False)

class Formulario_Servicios_medicos(forms.Form):
    opc = [("", "Seleccione Una Opcion"),("Consultas Medicas", "Consultas Medicas"), ("Servicios Medicos", "Servicios Medicos")]

    tipo_servicio = forms.ChoiceField(choices=opc, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    jefe_area = forms.ChoiceField(choices=Asignar_op_Doctores(), widget=forms.Select(attrs={"class": "disable-first-option"}), required=False, label="Jefe de Area")
     
class Formulario_psicologia(forms.Form):
    jefe_area = forms.ChoiceField(choices=Asignar_op_Psicologa(), widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    
class Formulario_capacitacion(forms.Form):
    opc = [("", "Seleccione Una Opcion"),("Capacitacion", "Capacitacion"), ("Frente Preventivo", "Frente Preventivo"), ("Brigada Juvenil", "Brigada Juvenil")]

    dependencia = forms.ChoiceField(choices=opc ,required=False, label="Dependencia")
    instructor = forms.ChoiceField(choices=Asignar_ops_Personal(), required=False, label="Instructor")
    solicitante = forms.ChoiceField(choices=Asignar_ops_Personal(), required=False,
    widget=forms.Select(attrs={'class':'disable-first-option'}))
    solicitante_externo = forms.CharField(required=False)

# Formulario Abastecimiento de Agua -- :D
class formulario_abastecimiento_agua(forms.Form):
     tipo_servicio = forms.ChoiceField(choices=Asignar_opc_tipos_suministros(), widget=forms.Select(attrs={'class': 'disable-first-option'}), required=False)
     nombres = forms.CharField(max_length=100, required=False)
     apellidos = forms.CharField(max_length=100, required=False)
     nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
     cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
     ltrs_agua = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '5'}), required=False)
     personas_atendidas = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '4'}), required=False)
     descripcion = forms.CharField(required=False)
     material_utilizado = forms.CharField(required=False)
     status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# Formulario Apoyo a otras Unidades
class Formulario_apoyo_unidades(forms.Form):
    tipo_apoyo = forms.ChoiceField(choices=Asignar_opc_tipos_apoyos(), widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    unidad_apoyada = forms.CharField(max_length=100, required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# Formulario Guardia de Prevencion
class Formulario_guardia_prevencion(forms.Form):
     motivo_prevencion = forms.ChoiceField(choices=Asignar_opc_motivo_prevencion(), widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
     descripcion = forms.CharField(required=False)
     material_utilizado = forms.CharField(required=False)
     status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# Formulario Atendido no Efectuado 
class Formulario_atendido_no_efectuado(forms.Form):
     descripcion = forms.CharField(required=False)
     material_utilizado = forms.CharField(required=False)
     status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# Formulario Despliegue de Seguridad 
class Formulario_despliegue_seguridad(forms.Form):
     motv_despliegue = forms.ChoiceField(choices=Asignar_opc_motivo_despliegue(),label="Motivo Despliegue", widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
     descripcion = forms.CharField(required=False)
     material_utilizado = forms.CharField(required=False)
     status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# Formulario Falsa Alarma 
class Formulario_falsa_alarma(forms.Form):
   motv_alarma = forms.ChoiceField(choices=Asignar_opc_motivo_fals_alarm(),label="Motivo Alarma", widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
   descripcion = forms.CharField(required=False)
   material_utilizado = forms.CharField(required=False)
   status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
   
# Formulario Servicios Especiales
class Formulario_Servicios_Especiales(forms.Form):
   tipo_servicio = forms.ChoiceField(choices=Asignar_opc_tipo_servicios(),label="Motivo Servicio", widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
   descripcion = forms.CharField(required=False)
   material_utilizado = forms.CharField(required=False)
   status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# Formulatio Fallecidos
class Formulario_Fallecidos(forms.Form):
    motivo_fallecimiento = forms.CharField(max_length=100, required=False)
    nom_fallecido = forms.CharField(max_length=100, required=False)
    apellido_fallecido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula_fallecido = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# Formulario Rescate
class Formulario_Rescate(forms.Form):
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    tipo_rescate = forms.ChoiceField(choices=Asignar_opc_tipo_rescate, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    
class Formulario_Rescate_Persona(forms.Form):
    nombre_persona = forms.CharField(max_length=100, required=False)
    apellido_persona = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula_persona = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad_persona = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo_persona = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    
class Formulario_Rescate_Animal(forms.Form):
    especie = forms.CharField(max_length=100, required=False)
    descripcion = forms.CharField(required=False)

# Formulario de Incendio
class Formulario_Incendio(forms.Form):
    tipo_incendio = forms.ChoiceField(choices=Asignar_opc_tipo_incendio, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    check_agregar_persona = forms.BooleanField(required=False,label="Agregar Persona")
    check_retencion = forms.BooleanField(required=False,label="Agregar Retencion Preventiva")

class Formulario_Retencion_Preventiva_Incendio(forms.Form):
    tipo_cilindro = forms.ChoiceField(choices=Asignar_opc_cilindros, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    capacidad = forms.CharField(max_length=50, required=False)
    serial = forms.CharField(max_length=50, required=False)
    nro_constancia_retencion = forms.CharField(max_length=50, required=False)
    nombre = forms.CharField(max_length=100, required=False)
    apellidos = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)


class Formulario_Persona_Presente(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(label="Telefono:",widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)

class Formulario_Detalles_Vehiculos_Incendio(forms.Form):
    modelo = forms.CharField(required=False)
    marca = forms.CharField(required=False)
    color = forms.CharField(max_length=80, required=False)
    año = forms.CharField(max_length=4, required=False)
    placas = forms.CharField(max_length=40, required=False)

# Formulario de Atenciones Paramedicas
class Formulario_Atenciones_Paramedicas(forms.Form):
    tipo_atencion = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Emergencias Medicas", "Emergencias Medicas"), ("Accidentes de Transito", "Accidentes de Transito")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    
class Formulario_Emergencias_Medicas(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    idx = forms.CharField(required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    trasladado = forms.BooleanField(required=False)

class Formulario_Traslados(forms.Form):
    hospital_trasladado = forms.CharField(required=False)
    medico_receptor = forms.CharField(required=False)
    mpps_cmt = forms.CharField(required=False)
    
# Formulario de Accidentes de Transito
class Formulario_Accidentes_Transito(forms.Form):
    tipo_accidente = forms.ChoiceField(choices=Asignar_opc_tipo_accidente, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    cantidad_lesionado = forms.IntegerField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    agg_vehiculo = forms.BooleanField(required=False,label="Agregar Vehiculo")
    agg_lesionado = forms.BooleanField(required=False,label="Agregar Lesionado")
    
class Formulario_Detalles_Vehiculos(forms.Form):
    modelo = forms.CharField(required=False)
    marca = forms.CharField(required=False)
    color = forms.CharField(max_length=30, required=False)
    año = forms.CharField(max_length=30, required=False)
    placas = forms.CharField(max_length=30, required=False)
    agg_vehiculo = forms.BooleanField(required=False, label="Agregar Segundo Vehiculo")

class Formulario_Detalles_Vehiculos2(forms.Form):
    modelo = forms.CharField(required=False)
    marca = forms.CharField(required=False)
    color = forms.CharField(max_length=30, required=False)
    año = forms.CharField(max_length=30, required=False)
    placas = forms.CharField(max_length=30, required=False)
    agg_vehiculo = forms.BooleanField(required=False, label="Agregar Tercer Vehiculo")
    
class Formulario_Detalles_Vehiculos3(forms.Form):
    modelo = forms.CharField(required=False)
    marca = forms.CharField(required=False)
    color = forms.CharField(max_length=30, required=False)
    año = forms.CharField(max_length=30, required=False)
    placas = forms.CharField(max_length=30, required=False)

class Formulario_Detalles_Lesionados(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    idx = forms.CharField(required=False)
    descripcion = forms.CharField(required=False)
    trasladado = forms.BooleanField(required=False)
    otro_lesionado = forms.BooleanField(required=False, label="Agregar Segundo Lesionado")
    
class Formulario_Detalles_Lesionados2(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    idx = forms.CharField(required=False)
    descripcion = forms.CharField(required=False)
    trasladado = forms.BooleanField(required=False)
    otro_lesionado = forms.BooleanField(required=False,label="Agregar Tercer Lesionado")
    
class Formulario_Detalles_Lesionados3(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    idx = forms.CharField(required=False)
    descripcion = forms.CharField(required=False)
    trasladado = forms.BooleanField(required=False)

class Formulario_Traslado_Accidente(forms.Form):
    hospital_trasladado = forms.CharField(required=False)
    medico_receptor = forms.CharField(required=False)
    mpps_cmt = forms.CharField(required=False)
    
class Formulario_Traslado_Accidente2(forms.Form):
    hospital_trasladado = forms.CharField(required=False)
    medico_receptor = forms.CharField(required=False)
    mpps_cmt = forms.CharField(required=False)
    
class Formulario_Traslado_Accidente3(forms.Form):
    hospital_trasladado = forms.CharField(required=False)
    medico_receptor = forms.CharField(required=False)
    mpps_cmt = forms.CharField(required=False)
    
class Forulario_Evaluacion_Riesgo(forms.Form):
    opc = [("", "Seleccione Una Opcion"), ("Vivienda Unifamiliar", "Vivienda Unifamiliar"), ("Vivienda Multifamiliar", "Vivienda Multifamiliar"), ("Vivienda Improvisada", "Vivienda Improvisada")]

    tipo_riesgo = forms.ChoiceField(choices=Asignar_opc_motivos_riesgo, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    tipo_etructura = forms.ChoiceField(choices=opc, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    
class Formulario_Mitigacion_Riesgos(forms.Form):
    tipo_riesgo = forms.ChoiceField(choices=Asignar_opc_motivos_riesgo_mitigacion, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    agregar_vehiculo = forms.BooleanField(required=False)

class Detalles_Vehiculo_Derrame_Form(forms.Form):
    modelo = forms.CharField(required=False)
    marca = forms.CharField(required=False)
    color = forms.CharField(max_length=40, required=False)
    año = forms.CharField(max_length=40, required=False)
    placas = forms.CharField(max_length=40, required=False)
    agregar_segundo_vehiculo = forms.BooleanField(required=False)

class Detalles_Vehiculo_Derrame_Form2(forms.Form):
    modelo = forms.CharField(required=False)
    marca = forms.CharField(required=False)
    color = forms.CharField(max_length=40, required=False)
    año = forms.CharField(max_length=40, required=False)
    placas = forms.CharField(max_length=40, required=False)
    agregar_tercer_vehiculo = forms.BooleanField(required=False)

class Detalles_Vehiculo_Derrame_Form3(forms.Form):
    modelo = forms.CharField(required=False)
    marca = forms.CharField(required=False)
    color = forms.CharField(max_length=40, required=False)
    año = forms.CharField(max_length=40, required=False)
    placas = forms.CharField(max_length=40, required=False)


class Formulario_Puesto_Avanzada(forms.Form):
    tipo_avanzada = forms.ChoiceField(choices=Asignar_opc_avanzada, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Traslados_Prehospitalaria(forms.Form):
    tipo_traslado = forms.ChoiceField(choices=Asignar_opc_traslados, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    idx = forms.CharField(required=False)
    hospital_trasladado = forms.CharField(required=False)
    medico_receptor = forms.CharField(required=False)
    mpps_cmt = forms.CharField(required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Asesoramiento(forms.Form):
  nombre_comercio = forms.CharField(max_length=100, required=False)
  rif_comercio = forms.CharField(max_length=100, required=False)
  nombres = forms.CharField(max_length=100, required=False)
  apellidos = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
  telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  descripcion = forms.CharField(required=False)
  material_utilizado = forms.CharField(required=False)
  status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formularia_Persona_Presente_Eval(forms.Form):
  nombre = forms.CharField(max_length=100, required=False)
  apellidos = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  telefono = forms.CharField(max_length=20, required=False)

class Formulario_Reinspeccion_Prevencion(forms.Form):
  nombre_comercio = forms.CharField(max_length=80, required=False)
  rif_comercio = forms.CharField(max_length=60, required=False)
  nombre = forms.CharField(max_length=100, required=False)
  apellidos = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
  telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  descripcion = forms.CharField(required=False)
  material_utilizado = forms.CharField(required=False)
  status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Retencion_Preventiva(forms.Form):
    tipo_cilindro = forms.ChoiceField(choices=Asignar_opc_cilindros, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    capacidad = forms.CharField(max_length=50, required=False)
    serial = forms.CharField(max_length=50, required=False)
    nro_constancia_retencion = forms.CharField(max_length=50, required=False)
    nombre = forms.CharField(max_length=100, required=False)
    apellidos = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Artificios_Pirotecnicos(forms.Form):
    nombre_comercio = forms.CharField(label="Nombre Distribuidor", max_length=100, required=False)
    rif_comercio = forms.CharField(label="RIF Distribuidor", max_length=60, required=False)
    tipo_procedimiento = forms.ChoiceField(choices=Asignar_op_Artificios, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Lesionado(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    idx = forms.CharField(required=False)
    descripcion = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Incendio_Art(forms.Form):
    tipo_incendio = forms.ChoiceField(choices=Asignar_opc_tipo_incendio, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    check_agregar_persona = forms.BooleanField(required=False,label="Agregar Persona")
    
class Formulario_Persona_Presente_Art(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)

class Formulario_Detalles_Vehiculos_Incendio_Art(forms.Form):
    modelo = forms.CharField(required=False)
    marca = forms.CharField(required=False)
    color = forms.CharField(max_length=40, required=False)
    año = forms.CharField(max_length=40, required=False)
    placas = forms.CharField(max_length=40, required=False)

class Formulario_Fallecidos_Art(forms.Form):
    motivo_fallecimiento = forms.CharField(max_length=100, required=False)
    nom_fallecido = forms.CharField(max_length=100, required=False)
    apellido_fallecido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula_fallecido = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Inspeccion_Establecimiento_Art(forms.Form):
    nombre_comercio = forms.CharField(max_length=100, required=False)
    rif_comercio = forms.CharField(max_length=60, required=False)
    nombre_encargado = forms.CharField(max_length=100, required=False)
    apellido_encargado = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula_encargado = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Valoracion_Medica(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Detalles_Enfermeria(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Procedimientos_Psicologia(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
    cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '3'}), required=False)
    sexo = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Masculino", "Masculino"), ("Femenino", "Femenino")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Capacitacion_Proc(forms.Form):
    opc = [("", "Seleccione Una Opcion"), ("Charla", "Charla"), ("Taller", "Taller"), ("Curso", "Curso")]
    opc2 = [("", "Seleccione Una Opcion"), ("Publica", "Publica"), ("Privada", "Privada")]

    tipo_capacitacion = forms.ChoiceField(choices=opc, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    tipo_clasificacion = forms.ChoiceField(choices=opc2, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    personas_beneficiadas = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '5'}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Brigada(forms.Form):
    opc = [("", "Seleccione Una Opcion"), ("Charla", "Charla"), ("Taller", "Taller"), ("Curso", "Curso"), ("Otros", "Otros")]
    opc2 = [("", "Seleccione Una Opcion"), ("Publica", "Publica"), ("Privada", "Privada")]

    tipo_capacitacion = forms.ChoiceField(choices=opc, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    tipo_clasificacion = forms.ChoiceField(choices=opc2, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
    otros = forms.CharField(required=False)
    personas_beneficiadas = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '5'}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)


class Formulario_Frente_Preventivo(forms.Form):
    nombre_actividad = forms.CharField(max_length=100, required=False)
    estrategia = forms.CharField(max_length=100, required=False)
    personas_beneficiadas = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '5'}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Jornada_Medica(forms.Form):
    nombre_jornada = forms.CharField(required=False)
    cant_personas_aten = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '5'}), required=False)
    descripcion = forms.CharField(required=False)
    material_utilizado = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# =================================================================================================================

class Formulario_Inspecciones(forms.Form):
    opc = [("", "Selecciones Una Opcion"), ("Prevención", "Prevención"), ("Árbol", "Árbol"), ("Asesorias Tecnicas", "Asesorias Tecnicas"), ("Habitabilidad", "Habitabilidad"), ("Otros", "Otros")]

    tipo_inspeccion = forms.ChoiceField(choices=opc, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Inspeccion_Prevencion_Asesorias_Tecnicas(forms.Form):
  nombre_comercio = forms.CharField(max_length=100, required=False)
  propietario = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  cedula_propietario = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  descripcion = forms.CharField(required=False)
  persona_sitio_nombre = forms.CharField(max_length=100, required=False)
  persona_sitio_apellido = forms.CharField(max_length=100, required=False)
  nacionalidad2 = forms.ChoiceField(label="Nacionalidad Persona En El Sitio",choices=[("V", "V"), ("E", "E")], required=False)
  persona_sitio_cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  persona_sitio_telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  material_utilizado = forms.CharField(required=False)
  status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Inspeccion_Habitabilidad(forms.Form):
  descripcion = forms.CharField(required=False)
  persona_sitio_nombre = forms.CharField(max_length=100, required=False)
  persona_sitio_apellido = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  persona_sitio_cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  persona_sitio_telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  material_utilizado = forms.CharField(required=False)
  status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Inspeccion_Otros(forms.Form):
  especifique = forms.CharField(required=False)
  descripcion = forms.CharField(required=False)
  persona_sitio_nombre = forms.CharField(max_length=100, required=False)
  persona_sitio_apellido = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  persona_sitio_cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  persona_sitio_telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  material_utilizado = forms.CharField(required=False)
  status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
  
class Formulario_Inspeccion_Arbol(forms.Form):
  especie = forms.CharField(max_length=100, required=False)
  altura_aprox = forms.CharField(max_length=100, required=False)
  ubicacion_arbol = forms.CharField(required=False)
  persona_sitio_nombre = forms.CharField(max_length=100, required=False)
  persona_sitio_apellido = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  persona_sitio_cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  persona_sitio_telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  descripcion = forms.CharField(required=False)
  material_utilizado = forms.CharField(required=False)
  status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# ==================================================================================================================

class Formulario_Investigacion(forms.Form):
  opc = [("", "Selecciones Una Opcion"), ("Comercio", "Comercio"), ("Estructura", "Estructura"), ("Vehiculo", "Vehiculo"), ("Vivienda", "Vivienda")]

  tipo_investigacion = forms.ChoiceField(choices=Asignar_op_Investigacion(), widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
  tipo_siniestro = forms.ChoiceField(choices=opc, widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)
  
class Formulario_Investigacion_Vehiculo(forms.Form):
  marca = forms.CharField(required=False)
  modelo = forms.CharField(required=False)
  color = forms.CharField(max_length=20, required=False)
  placas = forms.CharField(max_length=20, required=False)
  año = forms.CharField(max_length=4, required=False)
  nombre_propietario = forms.CharField(max_length=100, required=False)
  apellido_propietario = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  cedula_propietario = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  descripcion = forms.CharField(required=False)
  material_utilizado = forms.CharField(required=False)
  status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Investigacion_Comercio(forms.Form):
  nombre_comercio = forms.CharField(max_length=100, required=False)
  rif_comercio = forms.CharField(max_length=50, required=False)
  nombre_propietario = forms.CharField(max_length=100, required=False)
  apellido_propietario = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  cedula_propietario = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  descripcion = forms.CharField(required=False)
  material_utilizado = forms.CharField(required=False)
  status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

class Formulario_Investigacion_Estructura_Vivienda(forms.Form):
  tipo_estructura = forms.CharField(max_length=80, required=False)
  nombre = forms.CharField(max_length=100, required=False)
  apellido = forms.CharField(max_length=100, required=False)
  nacionalidad = forms.ChoiceField(choices=[("V", "V"), ("E", "E")], required=False)
  cedula = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '15'}), required=False)
  descripcion = forms.CharField(required=False)
  material_utilizado = forms.CharField(required=False)
  status = forms.ChoiceField(choices=[("", "Seleccione Una Opcion"), ("Culminado", "Culminado"), ("En Proceso", "En Proceso")], widget=forms.Select(attrs={"class": "disable-first-option"}), required=False)

# =====================================================================================

class Comercios(forms.Form):
    nombre_comercio = forms.CharField(required=False)
    rif_empresarial = forms.CharField(required=False)

class Formulario_Solicitud(forms.Form):
    opc = [("", "Seleccione una Opcion"),
        ("1", "La Concordia"),
        ("2", "Pedro Maria Morantes"),
        ("3", "San Juan Bautista"),
        ("4", "San Sebastian"),
        ("6", "Francisco Romero Lobo"),
    ]

    comercio = forms.ChoiceField(choices=Asignar_Comercios,required=False,widget=forms.Select(attrs={'class': 'disable-first-option'}))

    fecha_solicitud = forms.DateField(
        label="Fecha Solicitud",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    hora_solicitud = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        required=False)  #

    tipo_servicio = forms.ChoiceField(choices=(("", "Selecione Una Opcion"), ("Inspeccion", "Inspeccion"), ("Reinspeccion", "Reinspeccion")), required=False, widget=forms.Select(attrs={'class': 'disable-first-option'}))

    solicitante_nombre_apellido = forms.CharField(label="Nombres Y Apellidos del Solicitante",required=False)

    solicitante_cedula = forms.CharField(label="Cedula Solicitante",required=False)

    tipo_representante = forms.ChoiceField(choices=(("", "Selecione Una Opcion"), ("Presidente", "Presidente"), ("Propietario", "Propietario"), ("Representante Legal", "Representante Legal"), ("Encargado", "Encargado")), required=False, widget=forms.Select(attrs={'class': 'disable-first-option'}))

    rif_representante_legal = forms.CharField(required=False)

    direccion = forms.CharField(required=False)

    estado = forms.CharField(required=False)

    municipio = forms.ChoiceField(choices=Asignar_op_Municipios, required=False,
        widget=forms.Select(attrs={'class': 'disable-first-option'}))

    parroquia = forms.ChoiceField(choices=opc, required=False,
        widget=forms.Select(attrs={'class': 'disable-first-option'}))
    
    numero_telefono = forms.CharField(required=False)
    correo_electronico = forms.EmailField(required=False)
    pago_tasa = forms.CharField(required=False)
    referencia = forms.CharField(required=False)

class Formularia_Requisitos(forms.Form):
    cedula_identidad = forms.BooleanField(required=False,label="Cedula de Identidad")
    cedula_vecimiento = forms.DateField(
        label="Fecha Vencimiento",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    rif_representante = forms.BooleanField(required=False,label="RIF Representante")
    rif_representante_vencimiento = forms.DateField(
        label="Fecha Vencimiento",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    rif_comercio = forms.BooleanField(required=False,label="RIF Comercio")
    rif_comercio_vencimiento = forms.DateField(
        label="Fecha Vencimiento",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    cedula_catastral = forms.BooleanField(required=False,label="Cedula Catastral")
    cedula_catastral_vencimiento = forms.DateField(
        label="Fecha Vencimiento",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )


    documento_propiedad = forms.BooleanField(required=False,label="Documento de Propiedad/Carta de Arrendamiento")
    permiso_anterior = forms.BooleanField(required=False,label="Permiso Anterior (En Caso de Renovacion)")
    carta_autorizacion = forms.BooleanField(required=False,label="Carta Autorizacion")
    registro_comercio = forms.BooleanField(required=False,label="Registro Comercio")