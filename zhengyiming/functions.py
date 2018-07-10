from django.http import HttpResponse
from django.shortcuts import render


def home(ruquest):
    return render(ruquest, 'home.html')



def count(ruquest):
    text = ruquest.GET['text']
    total_count = len(ruquest.GET['text'])
    texts_dict = {}
    for texts in text:
        if texts not in texts_dict:
            texts_dict[texts] = 1
        else:
            texts_dict[texts] += 1
    sorted_dict = sorted(texts_dict.items(), key=lambda w:w[1], reverse=True)


    return render(ruquest, 'count.html', {'count':total_count, 'sortedict':sorted_dict})

def about(ruquest):
    return render(ruquest, 'about.html')