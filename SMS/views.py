from django.shortcuts import render
from .serializers import SMS_Serializer
from rest_framework.views import APIView
from .SMS import process_output
from sklearn.feature_extraction.text import TfidfVectorizer
from rest_framework.response import Response
from rest_framework import status
import joblib


class SMS_APIView(APIView):
    """ Handles Insert Operation """

    vectorizer = TfidfVectorizer()
    pipeline = joblib.load('ML_Models/svm_pipeline.pkl')

    def fit_vectorizer(self, text):
        # Get your training data here
        training_data = [text]
        self.vectorizer.fit(training_data)

    def post(self, request):
        # Extracting data from request
        serializer = SMS_Serializer(data=request.data)

        if serializer.is_valid():
            body = serializer.validated_data.get('body')

            # Setting up vectorized data
            self.fit_vectorizer(body)

            # Setting Custom Parameters
            result = process_output(str(body))

            print("Body is: ", body, "\nOutput is: ", result)

            # Storing Data
            serializer.validated_data['output'] = result
            serializer.save()

            return Response({"Output": result}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
