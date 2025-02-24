from rest_framework import serializers

from user.models import Account, User


class AccountBindSerializer(serializers.Serializer):
    account = serializers.SlugRelatedField(queryset=Account.objects.all(), slug_field='username', required=True)
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='email', required=True)
    session_user_id = serializers.CharField(required=True)
    session_id = serializers.CharField(required=True)

    def save(self):
        user = self.validated_data['user']
        account = self.validated_data['account']

        if account.user != user:
            raise serializers.ValidationError({
                "message": "Account has binded to another user"
            })

        account.session_user_id = self.validated_data['session_user_id']
        account.session_id = self.validated_data['session_id']
        account.status = Account.AccountStatus.CONFIRMED
        account.save()
