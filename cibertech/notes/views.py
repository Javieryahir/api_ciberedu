


from rest_framework import  permissions, viewsets, generics, permissions
from rest_framework import generics
from .models import noteBook, UsersM
from .serializers import noteBookSerializers, noteBookSerializersCreate
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class noteBookListView(generics.ListAPIView):
    queryset = noteBook.objects.all()
    serializer_class = noteBookSerializers

class noteBookCreateView(generics.CreateAPIView):
    queryset = noteBook.objects.all()
    serializer_class = noteBookSerializersCreate
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_instance = UsersM.objects.get(username=self.request.user.username)
        serializer.save(createdBy=user_instance)

        serializer.save(nameCreator=self.request.user.username)

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        
        return obj.createdBy == request.user
class noteBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = noteBook.objects.all()
    lookup_url_kwarg = 'noteBookId'
    serializer_class = noteBookSerializers   
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        
        if serializer.instance.createdBy == self.request.user:
            serializer.save(nameCreator=serializer.instance.nameCreator, createdBy=serializer.instance.createdBy, partial=True)
        

    def perform_destroy(self, instance):
        
        if instance.createdBy == self.request.user:
            instance.delete()
        




