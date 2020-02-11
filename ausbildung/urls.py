from django.urls import path

from ausbildung.views import IndexView, UbersetzenCreateView, AntwortenListView, PrufungCreateView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('ubersetzen/',UbersetzenCreateView.as_view(),name='ubersetzen'),
    path('<int:pk>/ubersetzen/',UbersetzenCreateView.as_view(),name='ubersetzen'),
    path('Antworten/', AntwortenListView.as_view(), name='Antworten'),
    path('Prufung/', PrufungCreateView.as_view(), name='Prufung'),
    path('<int:pk>/Prufung/', PrufungCreateView.as_view(), name='Prufung'),
]
