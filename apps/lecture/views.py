from django.shortcuts import render

# Create your views here.
from .models import Lecture

# Create your views here.

from rest_framework import serializers,viewsets
# Create your views here.

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lecture
        fields= ('id','title','description','Lecture_name','duration' ,'date','is_required')
        
class LectureViewSet(viewsets.ModelViewSet):
    queryset=Lecture.objects.all()
    serializer_class=LectureSerializer
     