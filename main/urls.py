from django.urls import path

from main.apps import MainConfig
from main.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView, \
    NewsletterDeleteView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('newsletters/', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletters/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletters/create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletters/<int:pk>/update/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletters/<int:pk>/delete/', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

]
