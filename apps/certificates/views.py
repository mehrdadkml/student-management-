from .models import Certificate

# Create your views here.

from rest_framework import serializers,viewsets
# Create your views here.

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certificate
        fields= ('name','description', )
        
class CertificateViewSet(viewsets.ModelViewSet):
    queryset=Certificate.objects.all()
    serializer_class=CertificateSerializer
     