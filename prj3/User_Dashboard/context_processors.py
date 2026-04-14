from datetime import datetime

def global_context(request):
    return {
        "username": "Enyinnaya",
        "role": "user",
        "current_year": datetime.now().year,
    }