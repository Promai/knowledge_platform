from django.shortcuts import render, get_object_or_404
from .models import Knowledge, Category

def knowledge_list(request):
    category_id = request.GET.get('category')  # Получаем ID выбранной категории из GET-параметров
    if category_id:
        knowledges = Knowledge.objects.filter(category_id=category_id)
    else:
        knowledges = Knowledge.objects.all()

    categories = Category.objects.all() # Получаем список всех категорий

    context = {
        'knowledges': knowledges,
        'categories': categories, # Передаем список категорий в шаблон
    }
    return render(request, 'knowledge/knowledge_list.html', context)


def knowledge_detail(request, pk):
    knowledge = get_object_or_404(Knowledge, pk=pk)
    context = {
        'knowledge': knowledge,
    }
    return render(request, 'knowledge/knowledge_detail.html', context)