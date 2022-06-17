from django.urls import path

from seeds import views


app_name='seeds'
urlpatterns = [
    path('seeds', views.SeedsListView.as_view(), name='seeds-list'),
    path('seeds/add/', views.SeedsCreateView.as_view(), name='seeds-add'),
    path('seeds/<int:pk>/detail', views.SeedsDetailView.as_view(), name='seeds-detail'),
    path('seeds/<int:pk>/update', views.SeedsUpdateView.as_view(), name='seeds-update'),
    path('seeds/<int:pk>/delete', views.SeedsDeleteView.as_view(), name='seeds-delete'),
]
