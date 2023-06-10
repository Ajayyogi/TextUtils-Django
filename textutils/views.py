# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>hello Harry Bhai</h1>
#     <a href="https://www.facebook.com/login/">Facebook</a>
#     <a href="https://www.instagram.com/">Instagram</a>
#     <a href="https://www.google.com/">Google</a>
#     <a href="https://twitter.com/i/flow/login">Twitter</a>
#     <a href="https://in.search.yahoo.com/?fr2=inr">Yahoo</a>
#     ''')
#
# def about(request):
#     return HttpResponse("About Harry Bhai")

# def index(request):
#     params = { "name": "Harry", "place": "Mars"}
#     return render(request, "index.html", params)
#     # return HttpResponse("Home")

# --------------------------------------------------------

# def index(request):
#     return render(request, "index.html")
#
#
# def removepunc(request):
#     # Get the text
#     djtext = request.GET.get("text", "default")
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("Capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("char count")

# -----------------------------------------------

def index(request):
    return render(request, "index.html")

def analyze(request):
    # Get the text
    djtext = request.POST.get("text", "default")

    # Check checkbox values
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    # charcount = request.GET.get("charcount", "off")

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Removed Punctuations", "analyzed_text": analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Changed to Uppercase", "analyzed_text": analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Extra Space Remover", "analyzed_text": analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "/n":
                analyzed = analyzed + char
        params = {"purpose": "Removed NewLines", "analyzed_text": analyzed}

    # if (charcount == "on"):
    #     analyzed = ""
    #     for char in djtext:
    #         if char != "/n":
    #             analyzed = analyzed + char
    #     params = {"purpose": "Removed NewLines", "analyzed_text": analyzed}
    #     # Analyze the text
    #     return render(request, "analyze.html", params)

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("Please select sny operation and try again! ")
