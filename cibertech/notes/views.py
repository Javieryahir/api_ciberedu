


from rest_framework import  permissions, viewsets, generics, permissions
from rest_framework import generics
from .models import noteBook, notesPages
from .serializers import noteBookSerializers, notePagesSerializers, notePagesBookSerializers, UserSerializer
# Create your views here.

class noteBookListView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = noteBook.objects.all()
    serializer_class = noteBookSerializers

class notesPagesListView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = notesPages.objects.all()
    serializer_class = notePagesSerializers

class noteBookPagesView(generics.RetrieveAPIView):
    queryset =noteBook.objects.all()
    lookup_url_kwarg = 'BookId'
    serializer_class = notePagesBookSerializers
    
class noteBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = noteBook.objects.all()
    lookup_url_kwarg = 'noteBookId'
    serializer_class = noteBookSerializers
class notePagesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = notesPages.objects.all()
    lookup_url_kwarg = 'notePageId'
    serializer_class = notePagesSerializers
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user. """
        return self.request.user