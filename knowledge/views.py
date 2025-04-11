from django.shortcuts import render, get_object_or_404
from .models import Knowledge, Category

def knowledge_list(request):
    print("knowledge_list: Начало выполнения")  # Добавьте эту строку
    print("knowledge_list: request.GET =", request.GET) # Добавьте эту строку
    category_id = request.GET.get('category')
    if category_id:
        knowledges = Knowledge.objects.filter(category_id=category_id)
    else:
        knowledges = Knowledge.objects.all()

    categories = Category.objects.all()

    context = {
        'knowledges': knowledges,
        'categories': categories,
    }
    print("knowledge_list: context =", context)  # Добавьте эту строку
    return render(request, 'knowledge/knowledge_list.html', context)


def knowledge_detail(request, pk):
    print("knowledge_detail: Начало выполнения, pk =", pk)  # Добавьте эту строку
    knowledge = get_object_or_404(Knowledge, pk=pk)
    context = {
        'knowledge': knowledge,
    }
    print("knowledge_detail: context =", context)  # Добавьте эту строку
    return render(request, 'knowledge/knowledge_detail.html', context)