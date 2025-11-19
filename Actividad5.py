# ============================================
#        SISTEMA DE GESTIÓN ACADÉMICA
# ============================================

# Listas principales
student_list = []
subject_list = []
assign_list = []       # Relación estudiante ↔ materia
grades_list = []       # Notas


# ============================================
#               MENÚ PRINCIPAL
# ============================================
def run_program():
    while True:
        print("\n=== Bienvenidos a la academia el Rosario ===\n")
        print("===== Menú principal =====")
        print("1. Gestión de Estudiantes")
        print("2. Gestión de Materias")
        print("3. Asignaciones")
        print("4. Notas y Calificaciones")
        print("5. Reportes y Estadísticas")
        print("6. Salir\n")

        option = input("Ingrese la Opción deseada: ")

        if option == "1":
            menu_student()
        elif option == "2":
            menu_subject()
        elif option == "3":
            menu_assign()
        elif option == "4":
            menu_notes()
        elif option == "5":
            menu_report()
        elif option == "6":
            print("\nGracias por preferirnos, ¡Hasta Luego!")
            break
        else:
            print("Dato inválido\n")


# ============================================
#             MENÚ ESTUDIANTES
# ============================================
def menu_student():
    while True:
        print("\n===== Menú Estudiantes =====")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("3. Consultar estudiante")
        print("4. Eliminar estudiante")
        print("5. Volver al menú principal\n")

        option = input("Ingrese la Opción deseada: ")

        if option == "1":
            add_student()
        elif option == "2":
            list_students()
        elif option == "3":
            search_student()
        elif option == "4":
            delete_student()
        elif option == "5":
            break
        else:
            print("Dato inválido\n")


# Registrar estudiante
def add_student():
    print("\n=== Registrar estudiante ===")
    name = input("Nombre: ")
    age = int(input("Edad: "))
    document = input("Documento: ")

    info_student = {"nombre": name, "edad": age, "documento": document}
    student_list.append(info_student)

    print("\nEstudiante registrado correctamente.\n")


# Listar estudiantes
def list_students():
    print("\n=== Lista de estudiantes ===\n")
    if len(student_list) == 0:
        print("No hay estudiantes registrados.")
    else:
        for i, est in enumerate(student_list, start=1):
            print(f"{i}. Nombre: {est['nombre']} | Edad: {est['edad']} | Documento: {est['documento']}")


# Consultar por documento
def search_student():
    print("\n=== Consultar estudiante ===")
    doc = input("Documento a buscar: ")
#Por cada elemento dentro de student_list, asigna temporalmente ese elemento a la variable est
    for est in student_list:
        if est["documento"] == doc:
            print(f"Nombre: {est['nombre']} | Edad: {est['edad']} | Documento: {est['documento']}")
            break
    else:
        print("No se encontró ningún estudiante con ese documento.")


# Eliminar estudiante
def delete_student():
    print("\n=== Eliminar estudiante ===")
    for i, est in enumerate(student_list, start=1):
        print(f"{i}. {est['nombre']} | Doc: {est['documento']}")

    id_eliminar = int(input("\nSeleccione el ID: ")) - 1

    if 0 <= id_eliminar < len(student_list):
        eliminado = student_list.pop(id_eliminar)
        print(f"Eliminado: {eliminado['nombre']}")
    else:
        print("ID inválido.")


# ============================================
#           MENÚ MATERIAS
# ============================================
def menu_subject():
    while True:
        print("\n===== Menú Materias =====")
        print("1. Registrar materia")
        print("2. Listar materias")
        print("3. Consultar materia")
        print("4. Eliminar materia")
        print("5. Volver al menú principal\n")

        option = input("Ingrese la Opción deseada: ")

        if option == "1":
            add_subject()
        elif option == "2":
            list_subject()
        elif option == "3":
            search_subject()
        elif option == "4":
            delete_subject()
        elif option == "5":
            break
        else:
            print("Dato inválido\n")


# Registrar materia
def add_subject():
    print("\n=== Registrar materia ===")
    name = input("Nombre de la materia: ")
    code = input("Código: ")

    info_subject = {"nombre": name, "codigo": code}
    subject_list.append(info_subject)

    print("\nMateria registrada correctamente.\n")


# Listar materias
def list_subject():
    print("\n=== Lista de materias ===\n")
    if len(subject_list) == 0:
        print("No hay materias registradas.")
    else:
        for i, sub in enumerate(subject_list, start=1):
            print(f"{i}. Materia: {sub['nombre']} | Código: {sub['codigo']}")


# Consultar materia
def search_subject():
    print("\n=== Consultar materia ===")
    cod = input("Código a buscar: ")

    for sub in subject_list:
        if sub["codigo"] == cod:
            print(f"Materia: {sub['nombre']} | Código: {sub['codigo']}")
            break
    else:
        print("No se encontró ninguna materia con ese código.")


# Eliminar materia
def delete_subject():
    print("\n=== Eliminar materia ===")
    for i, sub in enumerate(subject_list, start=1):
        print(f"{i}. {sub['nombre']} | Código: {sub['codigo']}")

    id_eliminar = int(input("\nSeleccione el ID: ")) - 1

    if 0 <= id_eliminar < len(subject_list):
        eliminado = subject_list.pop(id_eliminar)
        print(f"Materia eliminada: {eliminado['nombre']}")
    else:
        print("ID inválido.")


# ============================================
#              MENÚ ASIGNACIONES
# ============================================
def menu_assign():
    while True:
        print("\n===== Menú Asignaciones =====")
        print("1. Asignar materia a estudiante")
        print("2. Ver materias de un estudiante")
        print("3. Ver estudiantes de una materia")
        print("4. Retirar materia a estudiante")
        print("5. Volver al menú principal\n")

        option = input("Selecciona una opción: ")

        if option == "1":
            assign_subject()
        elif option == "2":
            list_subjects_by_student()
        elif option == "3":
            list_students_by_subject()
        elif option == "4":
            remove_assigned_subject()
        elif option == "5":
            break
        else:
            print("Opción inválida.")


# Asignar materia a estudiante
def assign_subject():
    print("\n=== Asignar materia ===")
    doc = input("Documento del estudiante: ")
    cod = input("Código de la materia: ")

    # Validar existencia del estudiante
    student_exists = any(est["documento"] == doc for est in student_list)
    if not student_exists:
        print("Error: el estudiante no existe.")
        return

    # Validar existencia de la materia
    subject_exists = any(sub["codigo"] == cod for sub in subject_list)
    if not subject_exists:
        print("Error: la materia no existe.")
        return

    # Verificar que la asignación no exista ya
    already_assigned = any(a["documento"] == doc and a["codigo"] == cod for a in assign_list)
    if already_assigned:
        print("Esta materia ya está asignada a este estudiante.")
        return

    relation = {"documento": doc, "codigo": cod}
    assign_list.append(relation)
    print("Materia asignada correctamente.")


# Ver materias de un estudiante
def list_subjects_by_student():
    print("\n=== Materias asignadas a estudiante ===")
    doc = input("Documento del estudiante: ")

    # Validar existencia del estudiante
    student_exists = any(est["documento"] == doc for est in student_list)
    if not student_exists:
        print("Error: el estudiante no existe.")
        return

    found = False
    for a in assign_list:
        if a["documento"] == doc:
            print(f"- Código: {a['codigo']}")
            found = True

    if not found:
        print("Este estudiante no tiene materias asignadas.")


# Ver estudiantes inscritos en una materia
def list_students_by_subject():
    print("\n=== Estudiantes inscritos en una materia ===")
    cod = input("Código de materia: ")

    # Validar existencia de la materia
    subject_exists = any(sub["codigo"] == cod for sub in subject_list)
    if not subject_exists:
        print("Error: la materia no existe.")
        return

    found = False
    for a in assign_list:
        if a["codigo"] == cod:
            print(f"- Documento: {a['documento']}")
            found = True

    if not found:
        print("No hay estudiantes inscritos en esta materia.")


# Retirar materia de estudiante
def remove_assigned_subject():
    print("\n=== Retirar asignación ===")
    #Verificar si hay asignaciones
    if not assign_list:
        print("No hay asignaciones para eliminar.")
        return
#Mostrar todas las asignaciones con un índice
    for i, a in enumerate(assign_list, start=1):
        print(f"{i}. Estudiante: {a['documento']} | Materia: {a['codigo']}")
#Pedir el ID a eliminar
    try:
        index = int(input("Seleccione el ID: ")) - 1
    except ValueError:
        print("ID inválido.")
        return
#Verificar que el índice sea válido y eliminar
    if 0 <= index < len(assign_list):
        removed = assign_list.pop(index)
        print(f"Asignación retirada: {removed['documento']} - {removed['codigo']}")
    else:
        print("ID inválido.")


# ============================================
#         MENÚ NOTAS Y CALIFICACIONES
# ============================================
def menu_notes():
    while True:
        print("\n===== Menú Notas y Calificaciones =====")
        print("1. Registrar nota")
        print("2. Ver notas por materia")
        print("3. Ver promedio de estudiante")
        print("4. Eliminar nota")
        print("5. Volver al menú principal\n")

        option = input("Seleccione una opción: ")

        if option == "1":
            add_grade()
        elif option == "2":
            list_grades_by_subject()
        elif option == "3":
            student_average()
        elif option == "4":
            delete_grade()
        elif option == "5":
            break
        else:
            print("Opción inválida.")


# Registrar nota
def add_grade():
    print("\n=== Registrar nota ===")
    doc = input("Documento del estudiante: ")
    cod = input("Código de la materia: ")
    porc = float(input("Porcentaje: "))
    cal = float(input("Calificación (0 a 5): "))

    grade = {
        "documento": doc, "codigo": cod, "porcentaje": porc, "calificacion": cal}

    grades_list.append(grade)
    print("Nota registrada correctamente.")


# Notas por materia
def list_grades_by_subject():
    print("\n=== Notas por materia ===")
    cod = input("Código de la materia: ")

    found = False
    for g in grades_list:
        if g["codigo"] == cod:
            print(f"Estudiante: {g['documento']} | {g['porcentaje']}% | Nota: {g['calificacion']}")
            found = True

    if not found:
        print("No hay notas para esta materia.")


# Promedio por estudiante
def student_average():
    print("\n=== Promedio del estudiante ===")
    doc = input("Documento del estudiante: ")

    total = 0
    acum_porcentaje = 0

    for g in grades_list:
        if g["documento"] == doc:
            total += g["calificacion"] * (g["porcentaje"] / 100)
            acum_porcentaje += g["porcentaje"]

    if acum_porcentaje == 0:
        print("Este estudiante no tiene notas registradas.")
    else:
        print(f"Promedio acumulado: {round(total, 2)}")


# Eliminar nota
def delete_grade():
    print("\n=== Eliminar nota ===")
    for i, g in enumerate(grades_list, start=1):
        print(f"{i}. Est: {g['documento']} | Mat: {g['codigo']} | {g['porcentaje']}% | Nota: {g['calificacion']}")

    index = int(input("Seleccione el ID: ")) - 1

    if 0 <= index < len(grades_list):
        removed = grades_list.pop(index)
        print(f"✔ Nota eliminada: {removed['documento']} - {removed['codigo']}")
    else:
        print("ID inválido.")


# ============================================
#      MENÚ REPORTES Y ESTADÍSTICAS
# ============================================
def menu_report():
    while True:
        print("\n===== Menú de Reportes y Estadísticas =====")
        print("1. Promedios detallados por estudiante")
        print("2. Estudiante con mejor promedio")
        print("3. Porcentaje de aprobación del grupo")
        print("4. Promedio general del grupo")
        print("5. Ranking de estudiantes")
        print("6. Volver al menú principal\n")

        option = input("Seleccione una opción: ")

        if option == "1":
            report_student_averages()
        elif option == "2":
            best_student()
        elif option == "3":
            group_pass_percentage()
        elif option == "4":
            group_general_average()
        elif option == "5":
            ranking_students()
        elif option == "6":
            break
        else:
            print("Opción inválida.\n")

#promedio detallado por estudiante
def report_student_averages():
    print("\n=== Promedios detallados por estudiante ===")

    if len(student_list) == 0:
        print("No hay estudiantes registrados.")
        return

    if len(grades_list) == 0:
        print("No hay notas registradas.")
        return

    for est in student_list:
        doc = est["documento"]
        total = 0
        acum = 0

        for g in grades_list:
            if g["documento"] == doc:
                total += g["calificacion"] * (g["porcentaje"] / 100)
                acum += g["porcentaje"]

        if acum == 0:
            promedio = 0
        else:
            promedio = round(total, 2)

        print(f"- {est['nombre']} ({doc}) → Promedio: {promedio}")


#estudiante con mejor promedio
def best_student():
    print("\n=== Estudiante con mejor promedio ===")

    if len(grades_list) == 0:
        print("No hay notas registradas.")
        return

    mejores = []

    for est in student_list:
        doc = est["documento"]
        total = 0
        acum = 0

        for g in grades_list:
            if g["documento"] == doc:
                total += g["calificacion"] * (g["porcentaje"] / 100)
                acum += g["porcentaje"]

        if acum > 0:
            promedio = round(total, 2)
            mejores.append((promedio, est["nombre"], doc))

    if len(mejores) == 0:
        print("Ningún estudiante tiene notas.")
        return

    mejores.sort(reverse=True)
    mejor = mejores[0]

    print(f"Mejor estudiante: {mejor[1]} ({mejor[2]}) → Promedio: {mejor[0]}")


#porcentaje de aprobacion del grupo
def group_pass_percentage():
    print("\n=== Porcentaje de aprobación del grupo ===")

    if len(student_list) == 0:
        print("No hay estudiantes registrados.")
        return

    aprobados = 0
    total_estudiantes = 0

    for est in student_list:
        doc = est["documento"]
        total = 0
        acum = 0

        for g in grades_list:
            if g["documento"] == doc:
                total += g["calificacion"] * (g["porcentaje"] / 100)
                acum += g["porcentaje"]

        if acum > 0:
            total_estudiantes += 1
            promedio = round(total, 2)
            if promedio >= 3.0:
                aprobados += 1

    if total_estudiantes == 0:
        print("No hay estudiantes con notas.")
        return

    porcentaje = (aprobados / total_estudiantes) * 100
    print(f"Aprobación del grupo: {round(porcentaje, 2)}%")


#promedio general del grupo
def group_general_average():
    print("\n=== Promedio general del grupo ===")

    suma_promedios = 0
    count = 0

    for est in student_list:
        doc = est["documento"]
        total = 0
        acum = 0

        for g in grades_list:
            if g["documento"] == doc:
                total += g["calificacion"] * (g["porcentaje"] / 100)
                acum += g["porcentaje"]

        if acum > 0:
            suma_promedios += round(total, 2)
            count += 1

    if count == 0:
        print("No hay notas registradas.")
        return

    print(f"Promedio general del grupo: {round(suma_promedios / count, 2)}")


#ranking de estudiantes
def ranking_students():
    print("\n=== Ranking de estudiantes ===")

    ranking = []

    for est in student_list:
        doc = est["documento"]
        total = 0
        acum = 0

        for g in grades_list:
            if g["documento"] == doc:
                total += g["calificacion"] * (g["porcentaje"] / 100)
                acum += g["porcentaje"]

        if acum > 0:
            promedio = round(total, 2)
            ranking.append((promedio, est["nombre"], doc))

    if len(ranking) == 0:
        print("No hay datos para generar el ranking.")
        return

    ranking.sort(reverse=True)

    for pos, data in enumerate(ranking, start=1):
        print(f"{pos}. {data[1]} ({data[2]}) → Promedio: {data[0]}")





# ============================================
#             EJECUCIÓN DEL SISTEMA
# ============================================
run_program()
