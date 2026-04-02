from rest_framework import serializers

class AttendanceSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    course_id = serializers.IntegerField()
    status = serializers.CharField()
    date = serializers.DateField()