from rest_framework import serializers
from .models import User, Organization, DonationRequest, Donation

class UserSerializer(serializers.ModelSerializer):
  lat = serializers.CharField(allow_null=True)
  lon = serializers.CharField(allow_null=True)
  zipcode = serializers.CharField(allow_null=True)

  class Meta:
    model = User
    fields = ('id', 'name', 'phone', 'email', 'zipcode', 'lat', 'lon')

class DonationRequestSerializer(serializers.ModelSerializer):
    amount_received = serializers.IntegerField(allow_null=True)
    class Meta:
        model = DonationRequest
        fields = ('org', 'item', 'item_type', 'amount_requested', 'amount_received')

class DonationSerializer(serializers.ModelSerializer):
    status = serializers.CharField(allow_null=True)
    pickup_address = serializers.CharField(allow_null=True)

    class Meta:
        model = Donation
        fields = ('org', 'name', 'phone', 'email', 'status', 'item',
                'amount', 'created_at', 'city', 'pickup_address', 'delivery_type',
                'pickup_or_dropoff_times')

class OrganizationSerializer(serializers.ModelSerializer):
    donation_requests = DonationRequestSerializer(many=True, required=False)
    donations = DonationSerializer(many=True, required=False)
    auth_token = serializers.CharField(write_only=True)

    url = serializers.CharField(required=False, allow_null=True)
    pickup_times = serializers.CharField(required=False, allow_null=True)
    dropoff_times = serializers.CharField(required=False, allow_null=True)
    description = serializers.CharField(required=False, allow_null=True)
    email = serializers.CharField(required=False)
    auth_user_id = serializers.CharField(required=False)
    pickup_instructions = serializers.CharField(allow_null=True, required=False)
    dropoff_instructions = serializers.CharField(allow_null=True, required=False)
    mail_instructions = serializers.CharField(allow_null=True, required=False)
    class Meta:
        model = Organization
        fields = ('id', 'name', 'url', 'address', 'description', 'phone',
                  'org_type', 'email', 'is_dropoff', 'is_pickup', 'is_mail',
                  'pickup_instructions', 'zipcode', 'lat', 'lon', 'auth_user_id',
                  'pickup_times', 'dropoff_times', 'donation_requests', 'donations',
                  'dropoff_instructions', 'mail_instructions', 'auth_token')
