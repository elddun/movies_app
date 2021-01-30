from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from app.models import Comment, Preferences, Account

from app.api.serializers import CommentSerializer, CommentListSerializer, RegistrationSerializer, CommentPostSerializer, PreferencesSerializer, PreferencePostSerializer


from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated


@permission_classes((IsAuthenticated,))
class ApiPreferenceList(ListAPIView):
    queryset = Preferences.objects.all()
    serializer_class = PreferencesSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('user__email',)

#http://127.0.0.1:8000/api/comments/list?search=123
class ApiCommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('movie_id',)


@permission_classes((IsAuthenticated,))
class ApiUsersList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = CommentListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('email',)
    

@api_view(['GET',])
def api_detail_comment_view(request, movie_id):
    try:
        comment = Comment.objects.get(movie_id=movie_id)
    except Comment.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


# @api_view(['POST',])
# def api_post_comment_view(request):
#     account = Account.objects.get(pk = 1)
#     comment = Comment(user = account)

#     if request.method == "POST":
#         serializer = CommentSerializer(comment, data = request.data)        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_post_comment_view(request):
    # account = request.user
    comment = Comment(user = request.user)
    
    if request.method == "POST":
        serializer = CommentPostSerializer(comment, data = request.data)
                
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_post_preference_view(request):
    # account = request.user
    pref = Preferences(user = request.user)
    
    if request.method == "POST":
        serializer = PreferencePostSerializer(pref, data = request.data)
                
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST',])
@permission_classes(())
def registration_view(request):
    if request.method == 'POST':
        data = {}
        serializer = RegistrationSerializer(data = request.data)
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'succesfully registered a new user'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)