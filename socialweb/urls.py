from django.urls import path
from socialweb import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [
    path("signup",views.SignUpView.as_view(),name="register"),
    path("",views.LoginView.as_view(),name="signin"),
    path("home",views.HomeView.as_view(),name="home"),
    path("userprofile",views.ProfileCreateView.as_view(),name="userprofile"),
    path("profile",views.UserprofileView.as_view(),name="profile_detail"),
    path("posts/<int:id>/comments/add",views.AddCommentView.as_view(),name="add-comment"),
    path("profile/<int:id>/change",views.ProfileUpdateView.as_view(),name="profile-edit"),
    path("posts/<int:id>/upvote/add",views.UpvoteView.as_view(),name="upvote"),
    path("posts/<int:id>/remove",views.PostDeleteView.as_view(),name="post-delete"),
    path("signout",views.SignoutView.as_view(),name="signout"),
    path("posts/<int:id>/upvote/remove",views.UpvoteRemoveView.as_view(),name="upvote-remove"),
    path("profile/add",views.ProfileCreateView.as_view(),name="profile-add"),
    path("comments/<int:id>/upvote/add",views.Commentupvoteview.as_view(),name="comment-like"),
    path("comments/<int:id>/remove",views.CommentdeleteView.as_view(),name="comment-delete")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)