
from rest_framework.generics import CreateAPIView
#from rest_framework.permissions import IsAdminUser

from mpesa.models import LNMOnline
from mpesa.api.serializers import LNMOnlineSerializer

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    

    def create(self,request):
        print(request.data,"this is request.data")