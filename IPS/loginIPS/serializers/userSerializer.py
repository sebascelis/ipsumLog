from rest_framework                   import serializers
from loginIPS.models.user      import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','lastname', 'email', "password"] 
    

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'id'      : user.id,
            'username': user.username,
            'lastname'  : user.lastname,
            'email'   : user.email,
        }


class UserSerializerUpdate(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ['username', 'lastname', 'password'] 
        
    def to_representationUpdate(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'username'      : username,
            'lastname'  : user.lastname
        }
        

    

