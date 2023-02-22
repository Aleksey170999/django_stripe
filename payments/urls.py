from django.urls import path

from payments import views

urlpatterns = [
    path('success/', views.SuccessView.as_view()),
    path('cancel/', views.CancelView.as_view()),
    path('buy/<int:id>/', views.StripeView.as_view(), name="buy"),
    path('item/<int:id>/', views.ItemRetrieve.as_view()),

]
