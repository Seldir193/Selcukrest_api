  
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo  # Sicherstellen, dass der Importpfad korrekt ist
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User 
        fields = ['id','first_name','last_name','username','email']  # Extra Leerzeichen entfernt
    
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = ['id','title', 'description', 'created_at','user','time_passed']  # Extra Leerzeichen entfernt
