from .models import Student, Mark 
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','register_num', 'name', 'place', 'admn_year']


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['id','register_num', 'english', 'maths', 'physics','cs','chemistry']