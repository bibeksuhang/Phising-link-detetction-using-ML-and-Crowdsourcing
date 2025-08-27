from django.shortcuts import render
from django.http import JsonResponse
from .models import URLRecord
from .utils import load_model
import json

model = load_model()

def index(request):
    return render(request, 'detector/index.html')

def predict(request):
    if request.method == "POST":
        url = request.POST.get("url", "").strip()
        if not url:
            return JsonResponse({"error": "URL is required"}, status=400)
        
        try:
            prediction = model.predict([url])[0]
            proba = model.predict_proba([url])[0]
            confidence = max(proba)
            
            record = URLRecord.objects.create(
                url=url,
                prediction=prediction,
                confidence=confidence
            )
            
            return JsonResponse({
                "prediction": prediction,
                "confidence": float(confidence),
                "record_id": record.id
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid method"}, status=405)

def feedback(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            record_id = data.get("record_id")
            feedback = data.get("feedback")
            
            if not record_id or not feedback:
                return JsonResponse({"error": "Missing data"}, status=400)
                
            record = URLRecord.objects.get(id=record_id)
            record.feedback = feedback
            record.save()
            
            return JsonResponse({"status": "success", "message": "Feedback saved!"})
            
        except URLRecord.DoesNotExist:
            return JsonResponse({"error": "Record not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid method"}, status=405)