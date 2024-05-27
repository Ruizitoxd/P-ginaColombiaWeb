import json

ListaBrigadas = []
ListaRegiones = []
ListaEspecies = []


def Input(texto):  #Buscar manera de declarar el tipo como none
  rta = input(texto)
  while (rta.isspace() or rta == ""):
    rta = input(texto)

  return rta


class Region:

  def __init__(self):
    self.Nombre = ""
    self.CantConglomerados = 0
    self.ListaConglomerados = []

  def AñadirConglomerado(self):
    conglomerado = Conglomerado()
    conglomerado.Numero = int(Input("Ingrese el número del conglomerado: "))
    ConglomeradoEsta = False

    #Validar que el conglomerado no exista en la lista
    if (self.ListaConglomerados != []):
      for conglomeradoL in self.ListaConglomerados:
        if (conglomerado.Numero == conglomeradoL.Numero):
          ConglomeradoEsta = True
          print("El conglomerado ya está registrado en la región.")
          break

    if not ConglomeradoEsta:
      conglomerado.Superficie = int(
          Input("Ingrese la superficie que abarca el conglomerado: "))
      if (ListaBrigadas != []):
        canti = int(
            Input("Ingrese la cantidad de brigadas que desea añadir: "))
        while (canti > len(ListaBrigadas)):
          print(
              "No se pueden añadir más brigadas de las que hay en el sistema.")
          canti = int(
              Input("Ingrese la cantidad de brigadas que desea añadir: "))

        for i in range(canti):
          numBrigada = int(Input("Ingrese el número de la brigada: "))
          for brigada in ListaBrigadas:
            if (brigada.NumBrigada == numBrigada):
              if (brigada in conglomerado.Brigadas):
                print("La brigada ya está registrada en el conglomerado.")
              else:
                conglomerado.Brigadas.append(brigada)
              break
      else:
        print(
            "No hay brigadas para añadir, por favor cree las brigadas y después añada al conglomerado."
        )

      self.CantConglomerados += 1
      self.ListaConglomerados.append(conglomerado)

  def EliminarConglomerado(self):
    num = int(Input("Ingrese el número del conglomerado que desea eliminar: "))
    for conglomerado in self.ListaConglomerados:
      if (conglomerado.Numero == num):
        self.ListaConglomerados.remove(conglomerado)
        self.CantConglomerados -= 1
        print("Se ha elimando el conglomerado.")

  def EditarConglomerado(self):
    num = int(Input("Ingrese el número del conglomerado que desea editar: "))
    for conglomerado in self.ListaConglomerados:
      if (conglomerado.Numero == num):
        opcion = ""
        print("\n¡Editor de conglomerados!")
        print("¿Que desea hacer?")
        print("1) Añadir brigada")
        print("2) Eliminar brigada")
        while (opcion != "1" and opcion != "2"):
          opcion = Input("Opción: ")
          match (opcion):
            case "1":
              conglomerado.AñadirBrigada()
            case "2":
              conglomerado.EliminarBrigada()
            case _:
              print("Opción inválida.")


class Conglomerado:

  def __init__(self):
    self.Numero = 0
    self.Superficie = 0
    self.Brigadas = []

  def AñadirBrigada(self):
    num = int(Input("Ingrese el número de la brigada que desea agregar: "))
    BrigadaEsta = False
    for brigada in ListaBrigadas:
      if (num == brigada.NumBrigada):
        BrigadaEsta = True
        if brigada in self.Brigadas:
          print(
              "No se puede agregar la brigada, porque ya está en este conglomerado"
          )
        else:
          self.Brigadas.append(brigada)
          print("La brigada fue añadida al conglomerado.")
        break

    if (not BrigadaEsta):
      print("No se ha encontrado la brigada")

  def EliminarBrigada(self):
    num = int(Input("Ingrese el número de la brigada que desea eliminar: "))
    BrigadaEsta = False
    for brigada in ListaBrigadas:
      if (num == brigada.NumBrigada):
        self.Brigadas.remove(brigada)
        BrigadaEsta = True
        print("La brigada fue eliminada del conglomerado.")
        break

    if (not BrigadaEsta):
      print("No se ha encontrado la brigada")


class Especie:

  def __init__(self):
    self.Nombre = ""
    self.NombreCientifico = ""
    self.Reino = ""
    self.Phylum = ""
    self.Clase = ""
    self.Orden = ""
    self.Familia = ""
    self.Genero = ""
    self.Especie = ""
    self.Ocurrencia = 0
    self.Ubicacion = {
        "Departamentos": [],
        "Conglomerados": [],
        "Brigadas": [],
        "IdDepartamento": ""
    }


class Brigada:
  #Declaración de la brigadare
  def __init__(self):
    self.NumBrigada = 0
    self.CantPersonas = 0
    self.Personas = []

  #Añadir una persona al a brigada
  def AñadirPersona(self):
    persona = Persona()
    persona.Identificacion = Input("Ingrese la identificacion de la persona: ")
    PersonaEsta = False

    #Validar que la persona no exista en la lista
    if (self.Personas != []):
      for personaL in self.Personas:
        if (persona.Identificacion == personaL.Identificacion):
          PersonaEsta = True
          print("La persona ya existe en la brigada")
          break

    if not PersonaEsta:
      persona.Nombre = Input("Ingrese el nombre de la persona: ")
      persona.Edad = int(Input("Ingrese la edad de la persona: "))
      persona.Profesion = Input("Ingrese la profesion de la persona: ")
      persona.NumBrigada = self.NumBrigada
      self.Personas.append(persona)
      self.CantPersonas += 1

  #Eliminar una persona de la brigada
  def EliminarPersona(self):
    identi = Input("Ingrese la identificación de la persona a eliminar: ")
    if (self.Personas != []):
      for persona in self.Personas:
        if (identi == persona.Identificacion):
          self.Personas.remove(persona)
          self.CantPersonas -= 1
          print("La persona fue eliminada de la brigada.")
          break

  #Editar las personas de la brigada
  def EditarPersona(self):
    identi = Input("Ingrese la identificacion de la persona a editar: ")
    if (self.Personas != []):
      for persona in self.Personas:
        if (identi == persona.Identificacion):
          persona.Nombre = input("Ingrese el nuevo nombre de la persona: ")
          persona.Edad = int(input("Ingrese la nueva edad de la persona: "))
          persona.Profesion = input(
              "Ingrese la nueva profesion de la persona: ")
          break

  #Visualizar las personas de la brigada
  def Visualizar(self):
    if (self.Personas != []):
      for persona in self.Personas:
        print(f"  Nombre: {persona.Nombre}")
        print(f"  Identificacion: {persona.Identificacion}")
        print(f"  Edad: {persona.Edad}")
        print(f"  Profesion: {persona.Profesion}")
        print()
    else:
      print("Actualmente, no hay personas registradas.")


class Persona:

  def __init__(self):
    self.Nombre = ""
    self.Identificacion = ""
    self.Edad = 0
    self.Profesion = ""
    self.NumBrigada = 0


class Presentacion():
  #Sistema para controlar las brigadas
  def SistemaBrigadas(self):
    opcion = ""
    while (opcion != "5"):
      print("\nBienvenido al sistema de brigadas")
      print("1) Crear una brigada")
      print("2) Eliminar brigada")
      print("3) Editor de brigadas")
      print("4) Visualizar brigadas")
      print("5) Salir")
      opcion = input("Ingrese una opcion: ")
      match opcion:
        case "1":
          self.RegistrarBrigada()
        case "2":
          self.EliminarBrigada()
        case "3":
          self.EditorBrigadas()
        case "4":
          self.VisualizarBrigadas()
        case "5":
          print("Sistema de brigadas cerrado.")
        case _:
          print("La opción no está disponible en el sistema.")

  #Sistema para registrar una brigada
  def RegistrarBrigada(self):
    print("\n¡ATENCIÓN! Estás apunto de crear una nueva brigada.")
    print(
        "Porfavor asegurate de que la brigada no esté registrada previamente.")
    print("\nRegistro de Brigada")
    brigada = Brigada()
    brigada.NumBrigada = int(Input("Ingrese el numero de la brigada: "))

    #Ingresar código para revisar si la brigada ya existe
    brigadaEsta = False
    if (ListaBrigadas != []):
      for i in ListaBrigadas:
        if (i.NumBrigada == brigada.NumBrigada):
          print("Esta brigada ya está registrada en el sistema")
          brigadaEsta = True
          break

      #RegistrarBrigada
      if (not brigadaEsta):
        canti = int(
            Input("Ingrese la cantidad de personas dentro de la brigada: "))
        #RegistrarPersona
        for i in range(0, canti):
          print()
          brigada.AñadirPersona()
        ListaBrigadas.append(brigada)
    else:
      canti = int(
          Input("Ingrese la cantidad de personas dentro de la brigada: "))
      #RegistrarPersona
      for i in range(0, canti):
        print()
        brigada.AñadirPersona()
      ListaBrigadas.append(brigada)

  #Sistema para eliminar una brigada
  def EliminarBrigada(self):
    num = int(Input("Ingrese el número de la brigada que desea eliminar: "))
    BrigadaEsta = False

    #Encontrar la brigada
    for brigada in ListaBrigadas:
      if (num == brigada.NumBrigada):
        num = ListaBrigadas.index(brigada)
        BrigadaEsta = True
        break

    if (BrigadaEsta):
      ListaBrigadas.remove(ListaBrigadas[num])
      print("La brigada fue eliminada del sistema.")
    else:
      print("La brigada no está registrada en el sistema.")

  #Sistema para editar una brigada
  def EditorBrigadas(self):
    num = int(Input("Ingrese el número de la brigada que desea editar: "))
    BrigadaEsta = False

    #Encontrar la brigada
    for brigada in ListaBrigadas:
      if (num == brigada.NumBrigada):
        num = ListaBrigadas.index(brigada)
        BrigadaEsta = True
        break

    if (BrigadaEsta):
      brigada = ListaBrigadas[num]
      opcion = ""
      while (opcion != "5"):
        print("\n\n¡Bienvenido al editor de brigadas!")
        print(f"NUMERO DE  BRIGADA: {brigada.NumBrigada}")
        print(f"CANTIDAD DE PERSONAS: {brigada.CantPersonas}")
        print("¿Qué desea hacer?")
        print("1) Añadir Persona")
        print("2) Eliminar Persona")
        print("3) Editar Personas")
        print("4) Visualizar Personas")
        print("5) Salir")
        opcion = input("Opción: ")
        match (opcion):
          case "1":
            brigada.AñadirPersona()
          case "2":
            brigada.EliminarPersona()
          case "3":
            brigada.EditarPersona()
          case "4":
            brigada.Visualizar()
          case "5":
            print("Editr de brigadas cerrado.")
          case _:
            print("La opción no está disponible en el sistema.")
    else:
      print("La brigada no está registrada en el sistema.")

  #Sistema para imprimir las brigadas
  def VisualizarBrigadas(self):
    if (ListaBrigadas != []):
      for brigada in ListaBrigadas:
        print(f"\nBrigada #: {brigada.NumBrigada}")
        print(f"Cantidad de personas: {brigada.CantPersonas}")
        print("Personas:")
        #Imprimir personas
        for persona in brigada.Personas:
          print(f"  Nombre: {persona.Nombre}")
          print(f"  Identificacion: {persona.Identificacion}")
          print()
    else:
      print("Actualmente no hay brigadas registradas.")

  #Sistema para controlar las regiones
  def SistemaRegiones(self):
    opcion = ""
    while (opcion != "5"):
      print("\nBienvenido al sistema de regiones")
      print("1) Crear región")
      print("2) Editar región")
      print("3) Editar conglomerados de una región")
      print("4) Visualizar regiones")
      print("5) Salir")
      opcion = input("Ingrese una opcion: ")
      match opcion:
        case "1":
          self.RegistrarRegion()
        case "2":
          self.EditarRegion()
        case "3":
          self.EditarConglomeradoRegion()
        case "4":
          self.VisualizarRegiones()
        case "5":
          print("Sistema de regiones cerrado.")
        case _:
          print("La opción no está disponible en el sistema.")

  #Sistema para registrar una región
  def RegistrarRegion(self):
    print("\n¡ATENCIÓN! Estás apunto de crear una nueva región.")
    print(
        "Porfavor asegurate de que la región no esté registrada previamente.")
    print("\nRegistro de región")
    region = Region()
    region.Nombre = Input("Ingrese el nombre de la región: ")

    #Ingresar código para revisar si la región ya existe
    regionEsta = False
    if (ListaRegiones != []):
      for i in ListaRegiones:
        if (i.Nombre.lower() == region.Nombre.lower()):
          print("Esta región ya está registrada en el sistema")
          regionEsta = True
          break

      #RegistrarRegion
      if (not regionEsta):
        canti = int(
            Input(
                "Ingrese la cantidad de conglomerados dentro de la región: "))
        #RegistrarConglomerado
        for i in range(0, canti):
          print()
          region.AñadirConglomerado()
        ListaRegiones.append(region)
    else:
      canti = int(
          Input("Ingrese la cantidad de conglomerados dentro de la región: "))
      #RegistrarPersona
      for i in range(0, canti):
        print()
        region.AñadirConglomerado()
      ListaRegiones.append(region)

  #Sistemas para editar una región
  def EditarRegion(self):
    opcion = ""
    while (opcion != "4"):
      print("\n¡Editor de región!")
      print("¿Que desea hacer?")
      print("1) Añadir conglomerado")
      print("2) Eliminar conglomerado")
      print("3) Cambiar nombre de la región")
      print("4) Cancelar")
      opcion = Input("Opción: ")
      match (opcion):
        case "1":
          self.AgregarConglomerado()
        case "2":
          self.EliminarConglomerado()
        case "3":
          self.CambiarNombreRegion()
    else:
      print("No hay regiones registradas.")

  #Sistema para agregar o eliminar brigadas del conglomerado
  def EditarConglomeradoRegion(self):
    nombre = Input(
        "Ingrese la región a la que desea editar los conglomerados: ")
    #Buscar Región
    if (ListaRegiones != []):
      for region in ListaRegiones:
        if (region.Nombre.lower() == nombre.lower()):
          region.EditarConglomerado()
          break
    else:
      print("No hay regiones registradas")

  #Sistema para cambiar el nombre de una region
  def CambiarNombreRegion(self):
    nombre = Input("Ingrese el nombre de la región que desea cambiar: ")
    RegionEsta = False
    RegionEsta2 = False
    NombreCambiado = False

    #Buscar la región
    if (ListaRegiones != []):
      for region in ListaRegiones:
        if (region.Nombre.lower() == nombre.lower()):
          RegionEsta = True
          nombre = Input("Ingrese el nuevo nombre de la región: ")

          #Revisar si el nombre ya está
          for region2 in ListaRegiones:
            if (region2.Nombre.lower() == nombre.lower()):
              print("Esta región ya está registrada en el sistema")
              RegionEsta2 = True
              break

          if RegionEsta2:
            print("No puede colocar un nombre que ya está registrado.")
          else:
            region.Nombre = nombre
            NombreCambiado = True
          break

      if (RegionEsta and NombreCambiado):
        print("Se ha cambiado el nombre del a región")
      elif (not RegionEsta):
        print("No se ha encontrado la región")
      else:
        print("No se ha podido cambiar el nombre de la región")

  #Sistema para agregar un conglomerado
  def AgregarConglomerado(self):
    nombre = Input(
        "Ingrese la región a la que desea agregar el conglomerados: ")
    if (ListaRegiones != []):
      for region in ListaRegiones:
        if (region.Nombre.lower() == nombre.lower()):
          region.AñadirConglomerado()
          break

  #Sistema para eliminar un conglomerado
  def EliminarConglomerado(self):
    nombre = Input(
        "Ingrese la región a la que desea eliminar el conglomerados: ")
    #Buscar Región
    if (ListaRegiones != []):
      for region in ListaRegiones:
        if (region.Nombre.lower() == nombre.lower()):
          region.EliminarConglomerado()
          break

  #Sistema para visualizar las regiones
  def VisualizarRegiones(self):
    if (ListaRegiones != []):
      for region in ListaRegiones:
        print(f"\nRegion: {region.Nombre}")
        print(f"Cantidad de conglomerados: {region.CantConglomerados}")
        print("Conglomerados:")
        #Imprimir personas
        for conglomerado in region.ListaConglomerados:
          print(f"  Numero: {conglomerado.Numero}")
          print(f"  Superficie: {conglomerado.Superficie}")
          print("  Brigadas:")
          #Imprimir brigadas
          for brigada in conglomerado.Brigadas:
            print(f"    Brigada #: {brigada.NumBrigada}")
            print(f"    Cantidad de personas: {brigada.CantPersonas}")
            print()
          print()
    else:
      print("Actualmente no hay brigadas registradas.")

  #Sistema para controlar los levantamientos
  def Levantamiento(self):
    opcion = ""
    while (opcion != "2"):
      print("\nBienvenido al sistema de levantamientos")
      print(
          "Para registrar un levantamiento, necesita los siguientes requerimientos:"
      )
      print(
          "\t1- Haber creado las regiones y los conglomerados en los que se desea registrar el levantamiento."
      )
      print("\t2- Haber creado las brigadas que registraron el levantamiento.")
      print("1) Registrar un levantamiento")
      print("2) Salir")
      opcion = input("Ingrese una opcion: ")
      match opcion:
        case "1":
          self.RegistrarLevantamiento()
        case "2":
          print("Sistema de levantamientos cerrado.")
        case _:
          print("La opción no está disponible en el sistema.")

  #Sistema para registrar un levantamiento
  def RegistrarLevantamiento(self):
    print("\n¡ATENCIÓN! Estás apunto de registrar una especie!")
    especie = Especie()
    especie.NombreCientifico = Input(
        "Ingrese el nombre cientifico de la especie: ")
    EspecieEsta = False

    #Encontrar especie
    for especieL in ListaEspecies:
      if (especieL.NombreCientifico == especie.NombreCientifico):
        EspecieEsta = True
        print(
            "No se puede registrar la especie, porque ya está en el sistema.")

    if (not EspecieEsta):
      especie.Nombre = Input("Ingrese el nombre de la especie: ")
      especie.Reino = Input("Ingrese el reino de la especie: ")
      especie.Phylum = Input("Ingrese el phylum de la especie: ")
      especie.Clase = Input("Ingrese la clase de la especie: ")
      especie.Orden = Input("Ingrese el orden de la especie: ")
      especie.Familia = Input("Ingrese la familia de la especie: ")
      especie.Genero = Input("Ingrese el género de la especie:  ")
      especie.Especie = Input("Ingrese el epiteto específico de la especie: ")
      especie.Ocurrencia = int(
          Input("Ingrese la ocurrencia de la especie en el sector: "))

      RegionEncontrada = False
      ConglomeradoEncontrado = False
      BrigadaEncontrada = False

      departamento = Region()
      conglomito = Conglomerado()

      #Encontrar region
      while (not RegionEncontrada):
        print("\n(Si la región no está en el sistema, lo pedirá nuevamente)")
        departa = Input(
            "Ingrese el departamento al que pertenece la especie: ")
        for region in ListaRegiones:
          if (departa.lower() == region.Nombre.lower()):
            RegionEncontrada = True
            especie.Ubicacion["Departamentos"].append(region)
            departamento = region
            break

      while (not ConglomeradoEncontrado):
        print(
            "\n(Si el conglomerado no está en la región, lo pedirá nuevamente)"
        )
        conglo = int(
            Input(
                "Ingrese el número del conglomerado de esa región a la que pertenece la especie: "
            ))
        #Encontrar conglomerado
        for conglomerado in departamento.ListaConglomerados:
          if (conglo == conglomerado.Numero):
            ConglomeradoEncontrado = True
            especie.Ubicacion["Conglomerados"].append(conglomerado)
            conglomito = conglomerado
            break

      while (not BrigadaEncontrada):
        print(
            "\n(Si la brigada no está en el conglomerado, lo pedirá nuevamente)"
        )
        brig = int(
            Input("Ingrese el número de la brigada que registró la especie: "))
        #Encontrar brigada
        for brigada in conglomito.Brigadas:
          if (brig == brigada.NumBrigada):
            BrigadaEncontrada = True
            especie.Ubicacion["Brigadas"].append(brigada)
            break

      if ("amazonas" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COAMA"

      if ("antioquia" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COANT"

      if ("arauca" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COARA"

      if ("atlantico" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COATL"

      if ("bolivar" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COBOL"

      if ("boyaca" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COBOY"

      if ("caldas" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COCAL"

      if ("caqueta" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COCAQ"

      if ("casanare" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COCAS"

      if ("cauca" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COCAU"

      if ("cesar" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COCES"

      if ("choco" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COCHO"

      if ("cordoba" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COCOR"

      if ("cundinamarca" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COCUN"

      if ("guainia" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COGUA"

      if ("guaviare" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COGUV"

      if ("huila" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COHUI"

      if ("guajira" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COLAG"

      if ("magdalena" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COMAG"

      if ("meta" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COMET"

      if ("nariño" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "CONAR"

      if ("norte de santander" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "CONSA"

      if ("putumayo" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COPUT"

      if ("quindio" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COQUI"

      if ("risaralda" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "CORIS"

      if ("san andres y providencia" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COSAP"

      if ("santander" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COSAN"

      if ("sucre" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COSUC"

      if ("tolima" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COTOL"

      if ("valle del cauca" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COVAC"

      if ("vaupes" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COVAU"

      if ("vichada" in especie.Ubicacion["Departamentos"][0].Nombre.lower()):
        especie.Ubicacion["IdDepartamento"] = "COVID"

      print("La especie fue agregada al sistema.")
      ListaEspecies.append(especie)
    else:
      print("No se puede registrar la especie, porque ya está en el sistema.")

  #Sistema para mostrar los resultados en la página
  def MostrarResultadosGraficos(self):
    pass

  #Main principal
  def Main(self):
    opcion = ""
    while (opcion != "5"):
      print("\n\n¡Bienvenido al sistema de inventario forestal florística!")
      print("¿Qué desea hacer?")
      print("1) Ingresar al sistema de brigadas")
      print("2) Ingresar al sistema de regiones")
      print("3) Registrar un levantamiento")
      print("4) Mostrar resultados gráficos")
      print("5) Salir")
      opcion = input("Opción: ")
      match (opcion):
        case "1":
          self.SistemaBrigadas()
        case "2":
          self.SistemaRegiones()
        case "3":
          self.Levantamiento()
        case "4":
          datos = Datos()
          datos.GrabarExportacion()
        case "5":
          print("Saliendo del sistema.")
        case _:
          print("La opción no está disponible en el sistema.")


class Datos():

  def __init__(self):
    self.ExportacionPrograma = open("Exportacion.json", "w")

  def GrabarExportacion(self):
    suma = 0
    #Halar las especies estimadas en Colombia
    for especie in ListaEspecies:
      suma += especie.Ocurrencia

    data = {"especies": {"Total": len(ListaEspecies), "CantidadTotal": suma}}

    #Registrar las especies
    for especie in ListaEspecies:
      data[f"{especie.Nombre}"] = {
          "Nombre": especie.Nombre,
          "NombreCientifico": especie.NombreCientifico,
          "Reino": especie.Reino,
          "Phylum": especie.Phylum,
          "Clase": especie.Clase,
          "Orden": especie.Orden,
          "Familia": especie.Familia,
          "Genero": especie.Genero,
          "Especie": especie.Especie,
          "Departamento": especie.Ubicacion["Departamentos"][0].Nombre,
          "Conglomerado": especie.Ubicacion["Conglomerados"][0].Numero,
          "Brigada": especie.Ubicacion["Brigadas"][0].NumBrigada,
          "IdDepartamento": especie.Ubicacion["IdDepartamento"]
      }

    #Cerrar dcocumento json
    json.dump(data, self.ExportacionPrograma)
    self.ExportacionPrograma.close()


presentacion = Presentacion()
presentacion.Main()
