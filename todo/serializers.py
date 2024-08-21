  
from rest_framework import serializers
from .models import Todo  # Sicherstellen, dass der Importpfad korrekt ist

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title', 'description', 'created_at']  # Extra Leerzeichen entfernt
