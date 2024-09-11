from rest_framework                   import serializers
from loginIPS.models.user      import User

class UserSerializerT(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','firstQuestion', 'secondQuestion', 'thirdQuestion', 'lastChangeDate'] 
    

    def to_representation_two(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'username': username,
            'firstQuestion' : firstQuestion,
            'secondQuestion': secondQuestion,
            'thirdQuestion': thirsQuestion,
            'lastChangeDate': lastChangeDate
        }


class UserSerializerTUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstQuestion', 'secondQuestion', 'thirdQuestion', 'image'] 
    

    def to_representation_two(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'firstQuestion' : firstQuestion,
            'secondQuestion': secondQuestion,
            'thirdQuestion': thirsQuestion,
            'this.image': image
        }

    

