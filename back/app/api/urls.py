from django.urls import path

from app.api.views import (
    api_detail_comment_view, 
    ApiCommentList,
    api_post_comment_view,
    ApiUsersList,
    registration_view,
    ApiPreferenceList,
    api_post_preference_view,
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = "app"

# urlpatterns = [
#     path('<movie_id>/', api_detail_comment_view, name="detail"),
#     path('list', ApiCommentList.as_view(), name="list"),
#     path('create/',api_post_comment_view, name = "create"),

# ]

urlpatterns = [
    
    path('list', ApiCommentList.as_view(), name="list"),
    path('ulist', ApiUsersList.as_view(), name="ulist"),
    path('plist', ApiPreferenceList.as_view(), name="plist"),
    path('create',api_post_comment_view, name = "create"),
    path('create_pref',api_post_preference_view, name = "create pref"),
    path('register',registration_view, name = "register"),
    path('login',obtain_auth_token, name = "login"),

]