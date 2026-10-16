from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from Questions.models import QuestionsDb
from Questions.serializers import QuestionSerializer

# Create your views here.

class QuestionListCreateView(APIView):
    def get(self,request):
        questions = QuestionsDb.objects.all()       #Fetches all question records from the database

        serializer = QuestionSerializer(questions,many=True)        #Converts the collection of question objects into serializable data. many=True is necessary because we are handling multiple questions

        return Response(serializer.data)        #.data contains the serialized result.


    def post(self,request):
        serializer = QuestionSerializer(data=request.data)      #asses that incoming data to the serializer for validation.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    #returns the saved question data.

        return Response(serializer.errors)


class QuestionsRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        question = QuestionsDb.objects.get(id=pk)

        serializer = QuestionSerializer(question)   #converts that single question into API-friendly data. We don't need many=True because we're fetching just one record.
        return Response(serializer.data)





    def put(self, request, pk):
     question = QuestionsDb.objects.get(id=pk)

     serializer = QuestionSerializer(
        question,
        data=request.data
     )

     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
     else:
        return Response(serializer.errors)




    def delete(self,request,pk):
        question = QuestionsDb.objects.get(id=pk)
        question.delete()

        return Response({"message": "Question deleted successfully"})