from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser, Paragraph, Word
from .serializers import CustomUserSerializer, ParagraphSerializer, WordSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticated]


class WordSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, word):
        word = word.lower()
        paragraphs = Paragraph.objects.filter(word__word=word)[:10]
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data)
