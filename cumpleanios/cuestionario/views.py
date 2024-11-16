from django.shortcuts import render, redirect
from django.http import HttpResponse

def inicio(request):
    if request.method == 'POST':
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        
        # Aquí debes poner la fecha de nacimiento correcta de tu novia
        fecha_correcta = "2000-12-05"  # Cambia esta fecha por la correcta
        
        if fecha_nacimiento == fecha_correcta:
            return redirect('pregunta_1')  # Redirige a la primera pregunta si la fecha es correcta
        else:
            return HttpResponse("La fecha de nacimiento es incorrecta. No eres tatis.")
    return render(request, 'cuestionario/inicio.html')


def pregunta_1(request):
    pregunta = "¿Como se llama tu mamá?"
    respuesta_correcta = "martha"
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        
        # Aquí validamos la respuesta de la primera pregunta
        if respuesta.lower() == respuesta_correcta:
            return redirect('pregunta_2')  # Redirige a la siguiente pregunta si es correcta
        else:
            return HttpResponse("Respuesta incorrecta. Intenta de nuevo.")
    
    return render(request, 'cuestionario/pregunta_1.html', {'pregunta': pregunta})

def pregunta_2(request):
    pregunta = "¿Como se llama tu papá?"
    respuesta_correcta = "juan"
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        
        # Aquí validamos la respuesta de la segunda pregunta
        if respuesta.lower() == respuesta_correcta:
            return redirect('pregunta_3')  # Redirige a la siguiente pregunta si es correcta
        else:
            return HttpResponse("Respuesta incorrecta. Intenta de nuevo.")
    
    return render(request, 'cuestionario/pregunta_2.html', {'pregunta': pregunta})

def pregunta_3(request):
    pregunta = "¿Cual es tu grupo de música favorito??"
    respuesta_correcta = "one direction"
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        
        # Aquí validamos la respuesta de la segunda pregunta
        if respuesta.lower() == respuesta_correcta:
            return redirect('pregunta_4')  # Redirige a la siguiente pregunta si es correcta
        else:
            return HttpResponse("Respuesta incorrecta. Intenta de nuevo.")
    
    return render(request, 'cuestionario/pregunta_3.html', {'pregunta': pregunta})

def pregunta_4(request):
    pregunta = "¿Color favorito?"
    respuesta_correcta = "lila"
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        
        # Aquí validamos la respuesta de la segunda pregunta
        if respuesta.lower() == respuesta_correcta:
            return redirect('pregunta_5')  # Redirige a la siguiente pregunta si es correcta
        else:
            return HttpResponse("Respuesta incorrecta. Intenta de nuevo.")
    
    return render(request, 'cuestionario/pregunta_4.html', {'pregunta': pregunta})

def pregunta_5(request):
    pregunta = "¿NOMBRE DE SER HUMANO PELIRROJO QUE LA QUIERE DEMASIADO Y QUE QUIERE QUE SEAS LA MUJER MAS FELIZ DEL MUNDO?"
    respuesta_correcta = "pedro"
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        
        # Aquí validamos la respuesta de la segunda pregunta
        if respuesta.lower() == respuesta_correcta:
            return redirect('fin')  # Redirige a la siguiente pregunta si es correcta
        else:
            return HttpResponse("Respuesta incorrecta. Intenta de nuevo.")
    
    return render(request, 'cuestionario/pregunta_5.html', {'pregunta': pregunta})


def fin(request):
    return redirect('ramo_floras')

def ramo_floras(request):
    return render(request, 'myapp/ramo_floras.html')





