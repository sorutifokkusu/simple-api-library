from rest_framework import viewsets
from .models import Category,Book
from .serializer import CategorySerializer,BookSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('title')

    
class SearchViewSet(viewsets.ModelViewSet):
     serializer_class = BookSerializer

     def get_queryset(self):  
        queryset = Book.objects.all().order_by('title')

        q_category = self.request.query_params.get('category')
        q_title = self.request.query_params.get('title')
        q_author = self.request.query_params.get('author')

        if q_category is not None:
          queryset = queryset.filter(category=q_category)

        if q_author is not None:
          queryset = queryset.filter(author__icontains=q_author)

        if q_title is not None:      
          queryset = queryset.filter(title__icontains =q_title)

        if (q_title==None) and (q_author==None) and (q_category==None):
          queryset=Book.objects.none()
        
        return queryset
