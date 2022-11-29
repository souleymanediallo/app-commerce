from django.shortcuts import render
from .models import MainCategory, Category, SubCategory


# Create your views here.
def home(request):
    main_category = MainCategory.objects.all()
    context = {
        'main_category': main_category,
    }
    return render(request, 'pages/index.html', context)