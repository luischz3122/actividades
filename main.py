calificacionesAlumno = [8, 7, 9, 10, 7, 7, 7]

calificacionTotal = 0
numeroParciales = len(calificacionesAlumno)
for calificacionParcial in calificacionesAlumno:
    calificacionTotal = calificacionTotal + calificacionParcial

p = calificacionTotal / numeroParciales
print("El promedio fue: " + str(p) )