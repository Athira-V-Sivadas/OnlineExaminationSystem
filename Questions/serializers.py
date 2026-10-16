from rest_framework import serializers
from Questions.models import QuestionsDb

class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=100)
    option_a = serializers.CharField(max_length=100)
    option_b = serializers.CharField(max_length=100)
    option_c = serializers.CharField(max_length=100)
    option_d = serializers.CharField(max_length=100)
    correct_answer = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return QuestionsDb.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.question = validated_data.get(
            'question', instance.question
        )
        instance.option_a = validated_data.get(
            'option_a', instance.option_a
        )
        instance.option_b = validated_data.get(
            'option_b', instance.option_b
        )
        instance.option_c = validated_data.get(
            'option_c', instance.option_c
        )
        instance.option_d = validated_data.get(
            'option_d', instance.option_d
        )
        instance.correct_answer = validated_data.get(
            'correct_answer', instance.correct_answer
        )

        instance.save()
        return instance