from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')



def count(request):
    text = request.GET['text']
    total_count = len(request.GET['text'])
    texts_dict = {}
    for texts in text:
        if texts not in texts_dict:
            texts_dict[texts] = 1
        else:
            texts_dict[texts] += 1
    sorted_dict = sorted(texts_dict.items(), key=lambda w:w[1], reverse=True)


    return render(request, 'count.html', {'count':total_count, 'sortedict':sorted_dict})

def about(request):
    return render(request, 'about.html')