from django.conf                                    import settings
from rest_framework                                 import generics, status, views, mixins
from rest_framework.response                        import Response
from rest_framework_simplejwt.serializers           import TokenObtainPairSerializer
from rest_framework.mixins import UpdateModelMixin
from loginIPS.models.user                    import User
from loginIPS.serializers.userSerializerT     import UserSerializerT
from loginIPS.serializers.userSerializerT   import  UserSerializerTUpdate



class FormDetailView(generics.RetrieveAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializerT
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class FormsView(generics.ListAPIView):
  serializer_class   = UserSerializerT
  queryset           = User.objects.all()

  def get(self, request, *args, **kwargs):
      return super().get(request, *args, **kwargs)

class FormUpdateView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class   = UserSerializerTUpdate
    queryset           = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
