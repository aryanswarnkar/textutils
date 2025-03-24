# views.py
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import string


def index(request):
    """Render the home page"""
    return render(request, 'index.html')


def analyze(request):
    """Process and analyze text based on user selections"""
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)

    djtext = request.POST.get('text', '')

    if not djtext.strip():
        return render(request, 'analyze.html', {
            'purpose': 'Error',
            'analyzed_text': 'No text provided for analysis',
            'current_date': datetime.date.today().strftime('%B %d, %Y')
        })

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    operations = []
    analyzed = djtext

    if removepunc == "on":
        punctuations = string.punctuation
        analyzed = "".join(char for char in analyzed if char not in punctuations)
        operations.append("Removed Punctuation")

    if fullcaps == "on":
        analyzed = analyzed.upper()
        operations.append("Converted to Uppercase")

    if extraspaceremover == "on":
        temp = " ".join(analyzed.split())
        analyzed = temp
        operations.append("Removed Extra Spaces")

    if newlineremover == "on":
        analyzed = analyzed.replace("\n", "").replace("\r", "")
        operations.append("Removed Newlines")

    if not operations:
        return render(request, 'analyze.html', {
            'purpose': 'Error',
            'analyzed_text': 'Please select at least one operation to perform',
            'current_date': datetime.date.today().strftime('%B %d, %Y')
        })

    purpose = " | ".join(operations) if operations else "Text Analysis"
    params = {
        'purpose': purpose,
        'analyzed_text': analyzed,
        'current_date': datetime.date.today().strftime('%B %d, %Y'),
        'original_text': djtext,
    }
    return render(request, 'analyze.html', params)


# Add these error handlers
def error_404(request, exception):
    """Handle 404 - Page Not Found errors"""
    return render(request, '404.html', status=404)


def error_500(request):
    """Handle 500 - Server Error"""
    return render(request, '500.html', status=500)