from rest_framework import serializers
from RestApi.models import Employee

class EmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=253)
    age = serializers.IntegerField(default=0)
    date_created = serializers.DateTimeField()


    def create(self, validated_data):
        return Employee.objects.create(validated_data)

        # We are creating a new Employee and saving it to the validated data
        #  Employee.cretae and the ojects created are called the validated data(data created)

    def update(self, instance, validated_data):
        return super(Employee).update(instance, validated_data)

        # we are updating the instance of the EMployee then saving it with the validated data we got
        # earlier from the the create method
        #  Get an EMployee Model => Update the instance of the Employee And Resplace it with the esixting validated data

    def update(self,instance,validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.age = validated_data.get('age',instance.age)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.save
        return instance

        # In thid method which is the same as earlier, we get the instance of the validated data as Employee.validatet data.get
        # After getting it with the instance key,then we save it with a new instance ojects

