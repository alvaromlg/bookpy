from rest_framework import mixins
from rest_framework import generics


class CreateRetrieveAPIView(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            generics.GenericAPIView):
    """
    Concrete view for creating or retrieving a model instance.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

