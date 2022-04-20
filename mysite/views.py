from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    if fullcaps =="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'purpose':'Changed to upper case','analyzed_text':analyzed}
        djtext =  analyzed
       
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose':'Remove New Lines','analyzed_text':analyzed}
        djtext =  analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index , char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose':'Remove Extra Space','analyzed_text':analyzed}
        djtext =  analyzed

    if removepunc == "on": 
        punctuation = '''!()-[]{};:'"\,.<>/?@#$%^&*__-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctutations','analyzed_text':analyzed}

    if (removepunc!="on" and fullcaps!="on" and extraspaceremover!="on" and newlineremover!="on"):
        if(charcount == "on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char

            params = {'purpose':'Character Count','analyzed_text':analyzed, 'charlen':len(djtext)}
            return render(request, 'charlen.html', params)
        else:
            return HttpResponse('<h1>Please Check atleast One box for further output</h1>')
        
    return render(request, 'analyze.html', params)
