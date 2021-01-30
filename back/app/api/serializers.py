from rest_framework import serializers

from app.models import Comment, Account, Preferences

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('getUsername')

    class Meta:
        model = Comment
        fields = ['movie_id', 'user', 'content', 'date_submited', 'username']

    def getUsername(self,comment):
        username = comment.user.username
        return username

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['movie_id', 'content', 'date_submited', ]

  

class PreferencesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('getUsername')
    class Meta:
        model = Preferences
        fields = ['fav_movie', 'fav_genre', 'fav_actor', 'user', 'username']
    def getUsername(self,pref):
        username = pref.user.username
        return username

class PreferencePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferences
        fields = ['fav_movie', 'fav_genre', 'fav_actor', ]


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username' , 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        account = Account(
            email= self.validated_data['email'],
            username = self.validated_data['username'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account