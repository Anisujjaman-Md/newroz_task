from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuoteViewSet, BanglaQuoteViewSet

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet, basename="quotes")
router.register(r'qoutes-bangla-translate', BanglaQuoteViewSet, basename="bangla-quotes")

urlpatterns = [
    path('', include(router.urls)),
    path('random/quotes/', QuoteViewSet.as_view({'get': 'random'}), name='random-quote'),
]