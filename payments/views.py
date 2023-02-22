from django.conf import settings
from django.shortcuts import render, redirect
import stripe
from rest_framework.views import APIView
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payments.models import Item
from payments.serializers import ItemSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class StripeView(APIView):

    def get(self, request, **kwargs):
        domain = "http://127.0.0.1:8000"
        id = kwargs['id']
        product = Item.objects.get(id=id)
        stripe_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return Response({"session_id": stripe_session.id})


class ItemRetrieve(TemplateView):
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = kwargs['id']
        product = Item.objects.get(id=id)
        context['public_key'] = settings.STRIPE_PUBLIC_KEY
        context['product'] = ItemSerializer(product, many=False).data
        return context
