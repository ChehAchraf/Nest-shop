from core.models import Category
def default(request):
    return {
        'categories': Category.objects.all(),
    }

