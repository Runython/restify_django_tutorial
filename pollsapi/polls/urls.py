from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .apiviewsets import PollViewSet, ChoiceList, CreateVote
from .apiview import UserCreate


router = DefaultRouter()
router.register(prefix='polls', viewset=PollViewSet, base_name='polls')

<<<<<<< HEAD
urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path('', include(router.urls)),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name=ChoiceList.name),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name=CreateVote.name),
    path('users/', UserCreate.as_view(), name='user_create'),
]

# urlpatterns += router.urls  # path('', include(router.urls)),
urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
=======
urlpatterns = format_suffix_patterns([
    path('polls/<int:pk>/choices', ChoiceList.as_view(), name=ChoiceList.name),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name=CreateVote.name)
])\
              + router.urls  # path('', include(router.urls)),
>>>>>>> e5307d534dc89c3e82188b648146177493f5c32f
