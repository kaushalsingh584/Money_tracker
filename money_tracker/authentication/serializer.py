from rest_framework import serializers
from .models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email','password','income','job_type']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def create(self,validated_data):

        # instance = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance