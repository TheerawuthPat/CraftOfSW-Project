from django.urls import path
from .views import HomePageView, OverViewPageView, UxDesignPageView, UiDesignPageView, ResearchPageView, AboutPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('overview/', OverViewPageView.as_view(), name="overview"),
    path('uxdesign/', UxDesignPageView.as_view(), name="uxdesign"),
    path('uidesign/', UiDesignPageView.as_view(), name="uidesign"),
    path('research/', ResearchPageView.as_view(), name="research"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contact/', ContactPageView.as_view(), name="contact"),
]