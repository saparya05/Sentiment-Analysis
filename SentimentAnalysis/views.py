from django.shortcuts import render
from django.http import JsonResponse
from .nlp import process_text
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def SentimentAnalysis(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            if text.strip() == "":
                return JsonResponse({'error': 'Empty input'}, status=400)

            result = process_text(text)
            return JsonResponse(result)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)