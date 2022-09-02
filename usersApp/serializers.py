from rest_framework import serializers
from usersApp.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name' , 'last_name', 'email', 'password')
        extra_kwargs = {
           'password': {
                'write_only': True, 
                'style': { 'input_type': 'password' }
                }
            }
    
    def create(self,validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']  
        )
        return user
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.username = instance.email
        instance.save()
        return instance


        