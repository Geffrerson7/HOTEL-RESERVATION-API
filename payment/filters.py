from django_filters import rest_framework as filters
from .models import Payment

class PaymentFilter(filters.FilterSet):
    user_id = filters.CharFilter(method='filter_by_user')

    def filter_by_user(self, queryset, name, value):
        return queryset.filter(reservation__user__id=self.request.user.id)

    class Meta:
        model = Payment
        fields = ['user_id']