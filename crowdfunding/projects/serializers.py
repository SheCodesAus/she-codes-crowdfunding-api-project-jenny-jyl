from rest_framework import serializers
from .models import Project
from .models import Pledge
from location_field.models.plain import PlainLocationField
from users.serializers import CustomUserSerializer

class PledgeSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    # amount = serializers.IntegerField()
    # comment = serializers.CharField(max_length=300)
    # anonymous = serializers.BooleanField()
    # supporter = serializers.CharField(max_length=200)
    # project_id = serializers.IntegerField()
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    location=serializers.CharField(max_length=100)
    organization=serializers.CharField(max_length=200)
    website=serializers.URLField()
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class DeleteProjectSerializer(serializers.Serializer):
    def delete(self, validated_data):
        return Project.objects.delete(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        # saying new instance title should be whatever we get from validated_data under the title column, but if we didn't get anything, use instance.title
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


    
