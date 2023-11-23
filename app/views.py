from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def chat_ai(request):
    return render(request, 'chat/chat_ai.html')

def chat_prep(request):
    return render(request, 'chat/chat_prep.html')
