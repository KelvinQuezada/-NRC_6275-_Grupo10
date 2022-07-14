
class idRegistro():
    """
    La clase principal es idRegistro
            
    Atributos
    -------------------------------------
    nombreID: str
        Nombres de la persona para el login 
    apellidoID: int
        Apellido de la persona para el login
    telefonoID: int
        Telefono de la persona para el login
        -------------------------------------
    Metodos:
        -------------------------------------
        def __init__(self,nombreID,apellidoID,telefID):
            Construye todos los atributos
        menuLogin()
            Menu principal de login
    """
    def __init__(self,nombreID,apellidoID,telefID):
        self.nombreID=nombreID
        self.apellidoID=apellidoID
        self.telefID=telefID
        

class DatosInscripcion():
    """
    La clase principal es idRegistro
            
    Atributos
    -------------------------------------
    cedula: int
        Cedula para el registro de la afiliasion de registro de salud
    nombre: str
        Nombres para el registro de la afiliasion de registro de salud
    apellido: str
        Apellido para el registro de la afiliasion de registro de salud
    genero: str
        Genero para el registro de la  afiliasion de registro de salud 
    fechaNacimiento: str
        Fecha de nacimiento para el registro de la afiliasion de registro de salud
    pais: str
        Pais para el registro de la afiliasion de registro de salud
    provincia: str
        Provincia para el registro de la  afiliasion de registro de salud
    trabajo: str
        Trabajo para el registro de la  afiliasion de registro de salud
    direccion: str
        Direccion para el registro de la  afiliasion de registro de salud
    discapacidad: str
        Discapacidad para el registro de la  afiliasion de registro de salud
    salario: int
        Salario para el registro de la  afiliasion de registro de salud
        -------------------------------------
    Metodos:
        -------------------------------------
        def __init__(self,cedula,nombre,apellido,genero,fechaNacimiento, pais,provincia,trabajo,direccion,discapacidad,salario ):
            Construye todos los atributos
    """
    def __init__(self,cedula,nombre,apellido,genero,fechaNacimiento, pais,provincia,trabajo,direccion,discapacidad,salario ):

        self.atributo1=cedula
        self.atributo2 = nombre
        self.atributo3 =apellido
        self.atributo4=genero
        self.atributo5=fechaNacimiento
        self.atributo6=pais
        self.atributo7=provincia
        self.atributo8=trabajo
        self.atributo9=direccion
        self.atributo10=discapacidad
        self.atributo11=salario


def RegistroAfiliaccion():
    print("================================================")
    print("                  Registro de Cuenta            ")
    print("================================================")
    registoVentanilla=DatosInscripcion(int(input("Ingrese su cedula: ")),
    str(input("Ingrese Nombre: ")),str(input("Ingrese Apellido: ")),
    str(input("Ingrese su genero: ")),str(input("Ingrese su fecha de nacimiento: ")),
    str(input("Ingrese su Pais: ")),str(input("Ingrese su Provincia: ")),
    str(input("Ingrese su Trabajo: ")),str(input("Ingrese su Direccion: ")),
    str(input("Sufre de una discapacidad: ")),int(input("Ingrese el valor de su ganacia: ")))
    print("================================================")
    print("           SUS DATOS PERSONALES SON: ")
    print("================================================")
    print("Cedula: ",registoVentanilla.atributo1)
    print("Nombre: ",registoVentanilla.atributo2)
    print("Apellido: ",registoVentanilla.atributo3)
    print("Genero: ",registoVentanilla.atributo4 )
    print("Fecha de nacimiento: ",registoVentanilla.atributo5 )
    print("Pais:",registoVentanilla.atributo6 )
    print("Provincia:",registoVentanilla.atributo7 )
    print("Trabjao:",registoVentanilla.atributo8 )
    print("Direccion:",registoVentanilla.atributo9 )
    print("Discapacidad:",registoVentanilla.atributo10 )
    print("Salario:",registoVentanilla.atributo11 )
    print("================================================")



def menuLogin():

    while(True!=3):
        print("====================== BIENVENIDO AFILIACION ======================")
        print("1.- Registrarse al Login")
        print("2.- Iniciar sesion con el Login")
        print("3.- SALIR")
        print("===============================================================")
        while True:
            try:        
                opcC=int(input("Seleccione una respuesta: "))
            except:
                print("Error")
            else:
                break
        if opcC==1:
            '''Registrar una cuenta en el sistema.'''
            print("===============================================================")
            print("           REGISRARSE DE LOGIN  PARA LA AFILIACION ")
            print("===============================================================")
            '''Creacion de usuario'''
            while True:
                try:
                    nombreID=input("Ingrese su nombre: ")
                    apellidoID=input("Ingrese su apellido: ")
                    telefID=input("Ingrese su numero de telefono (10 digitos): ")
                    while len(telefID)<10 or len(telefID)>10:
                        print("Error")
                        telefID=input("Ingrese su numero de telefono (10 digitos): ")
                    correoApp=input("Ingrese su correo electronico de preferencia: ")
                    if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                        print("Correo correcto")
                    else:
                        print("Error")
                        correoApp=input("Ingrese su correo electronico de preferencia: ")
                        if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                            print("Correo correcto")
                        else:
                            print("Error")
                            correoApp=input("Ingrese su correo electronico de preferencia: ")
                            if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                                print("Correo correcto")
                            else:
                                print("Error")
                                correoApp=input("Ingrese su correo electronico de preferencia: ")
                                if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                                    print("Correo correcto")
                                else:
                                    print("Error")
                                    correoApp=input("Ingrese su correo electronico de preferencia: ")
                                    if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                                        print("Correo correcto")
                                    else:
                                        print("Error")
                                        correoApp=input("Ingrese su correo electronico de preferencia: ")
                except:
                    print("Ingrese los datos correctamente")
                else:
                    break
            '''poner en minusculas con lower()
            Minusculas al nombre,apellido y utilzar 3 primeras variables y las 3 ultimos valores del telefono'''
            nombreIDCortado=nombreID[0:3].lower()
            apellidoIDCortado=apellidoID[0:3].lower()
            telefIDCortado=telefID[7:10]
            print("El nombre de usuario creado con sus datos es el siguiente")
            '''asignacion de los datos a la variable user'''
            user=nombreIDCortado+telefIDCortado+ apellidoIDCortado
            print("→ ", user)
            """El password  es la crear una contrasenia  """
            print("La contrasenia creada es la siguiente")
            password=apellidoIDCortado + nombreIDCortado + telefIDCortado
            print("→ ",password )
        elif opcC==2:
            '''Inicio de sesion y el registro de afiliasion de Salud'''
            print("=======================================================")
            print("                 INICIO DE SESION                      ")
            print("=======================================================")
            user2=input(print("Ingrese el usuario: "))
            print("=======================================================")
            if user2==user:
                print("El usuario es correcto: ")
                print("=======================================================")
                password2=input(print("Ingrese su  contrasenia: "))
                print("=======================================================")
                if password2==password:
                    print("La contrasenia es correcta ")
                    """LLamamos la funcion de RegistroAfiliaccion() para registar el usuario a la afiliasion"""
                    RegistroAfiliaccion()
                else:
                    print("La constrasenia es incorrecta")
            else:
                print("El usuario o contrasenia es incorrecto")

        elif opcC== 3:
            print("Acaba de salir del Menu de la Afiliacion de Salud")
        else:
            print("Error, vuelva a ingresar de nuevo")
menuLogin()