from django.urls import path
from . import views
from app_noticias.views import noticias_resumo_template, HomePageView, ContatoView, ContatoSucessoView, MensagemView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('noticias/resumo/', noticias_resumo_template, name='resumo'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('contato_sucesso/', ContatoSucessoView.as_view(), name='contato_sucesso'),
    path('mensagens/', MensagemView.as_view(), name='mensagens'),

]




