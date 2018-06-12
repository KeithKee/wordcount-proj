from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'hello':'my dict value'})


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            #increase
            worddict[word] +=1
        else:
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist), 'sortedwords':sortedwords})