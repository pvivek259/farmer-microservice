from deliveryapp.models import Farmer,ShippingAddress, PrimaryAddress
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
import json


@api_view(['POST'])
def create_farmer(request):
    # Get the param
    request_param=json.loads(request.body)
    print(request_param)
    phone_num = request_param.get("phone_no", None)
    if phone_num == None:
        error_response={"message":"please give phone Number."}
        return JsonResponse(error_response)

    #add other details and save
    farmer_object, ok =  Farmer.objects.get_or_create(phone_no = phone_num)
    farmer_object.name = request_param.get("name")
    farmer_object.email = request_param.get("email")
    farmer_object.save()


    #Create primary address
    primary_address_param = request_param.get("primary_address")
    primary_address_object = PrimaryAddress.objects.create(
        name = primary_address_param.get("name"),
        pin_code = primary_address_param.get("pin_code")
    )
    primary_address_object.address1 = primary_address_param.get("address1")
    primary_address_object.address2 = primary_address_param.get("address2")
    primary_address_object.village = primary_address_param.get("village")
    primary_address_object.city = primary_address_param.get("city")
    primary_address_object.country = primary_address_param.get("country")

    primary_address_object.save()

    farmer_object.primary_address = primary_address_object
    farmer_object.save()
    
    output={"success":True,
                "message":"Farmer added with primary address."}

    return JsonResponse(output)


# Able to add shipping address by phone number.

@api_view(['POST'])
def add_shipping_address(request):
    # Get the param
    request_param=json.loads(request.body)
    print(request_param)
    phone_number = request_param.get("phone_no")
    print(phone_number)
    # Get farmer object
    farmer_obj = Farmer.objects.get(phone_no = phone_number)
    #create  shipping address object, and add farmer ID
    shipping_address_object = ShippingAddress.objects.create(farmer = farmer_obj)

    shipping_address_object.name = request_param.get("name", None),
    shipping_address_object.address1 = request_param.get("address1", None),
    shipping_address_object.address2 =request_param.get("address2", None),
    shipping_address_object.pin_code = request_param.get("pin_code", None),
    shipping_address_object.village = request_param.get("village", None),
    shipping_address_object.city =request_param.get("city", None),
    shipping_address_object.country =request_param.get("country", None)

    #save shipping address object
    shipping_address_object.save()
    output={"success":True,
                "message":"succesfully added the address."}

    return JsonResponse(output)


@api_view(['GET'])
def farmer_list(request):
    if request.method == 'GET':
        all_farmer_objs = Farmer.objects.all()
        result = []
        for farmer_obj in all_farmer_objs:
            output={"id":farmer_obj.id, 
            "name": farmer_obj.name,
            "email": farmer_obj.email,
            "phone_no": farmer_obj.phone_no,
            "primary_address": parse_primary_address( farmer_obj.primary_address)
            }
            result.append(output)

        new_format_result_json ={"data":result}
        return JsonResponse(new_format_result_json)

@api_view(['PUT'])
def update_shipping_address(request):
    request_params=request.post()
    shipping_address_id=request_params.get(shipping_address_id,None)
    if shipping_address_id==None:
        error_response={"message":"please give shipping sddress id in request body."}
        return JsonResponse(error_response)

    shipping_address_object = ShippingAddress.objects.get(id=shipping_address_id)

    shipping_address_object.name = request_param.get("name")
    shipping_address_object.addressline1 = request_param.get("addressLine1")
    shipping_address_object.addressline2 = request_param.get("addressLine2")
    shipping_address_object.pin_code = request_param.get("pincode")
    shipping_address_object.village = request_param.get("village")
    shipping_address_object.city = request_param.get("city")
    shipping_address_object.country = request_param.get("country")


    shipping_address_object.save()
    output={"success":True,
                "message":"succesfully updated the address."}

    return JsonResponse(output)






#Able to get shipping addresses of farmer by phone number

@api_view(['GET'])
def get_shipping_address(request):
    request_param= request.GET  #get the param
    print (request_param)
    phone_number= request_param.get("phone_no")
    print(phone_number)
    #get the farmer object
    farmer_obj = Farmer.objects.get(phone_no = phone_number)
    #get shipping addresses object, and add farmer ID
    shipping_address_objs= farmer_obj.shippingaddress_set.all()
    
    result_json ={"data":parse_shipping_addresses(shipping_address_objs)}

    return JsonResponse(result_json)



def parse_shipping_addresses(shipping_address_objs):
    result = []
    for shipping_address_obj in shipping_address_objs:
        result.append(parse_shipping_address(shipping_address_obj))

    return result

def parse_shipping_address(shipping_address):
    shipping_address_json = {}
    shipping_address_json["id"] = shipping_address.id
    shipping_address_json["name"] = shipping_address.name
    shipping_address_json["address1"] = shipping_address.address1
    shipping_address_json["address2"] = shipping_address.address2
    shipping_address_json["pin_code"] = shipping_address.pin_code
    shipping_address_json["village"] = shipping_address.village
    shipping_address_json["city"] = shipping_address.city
    shipping_address_json["country"] = shipping_address.country
    return shipping_address_json

def parse_primary_address(primary_address):
    primary_address_json = {}
    primary_address_json["id"] = primary_address.id
    primary_address_json["name"] = primary_address.name
    primary_address_json["address1"] = primary_address.address1
    primary_address_json["address2"] = primary_address.address2
    primary_address_json["pin_code"] = primary_address.pin_code
    primary_address_json["village"] = primary_address.village
    primary_address_json["city"] = primary_address.city
    primary_address_json["country"] = primary_address.country
    return primary_address_json


#Able to get farmer by phone number.

@api_view(['GET'])
def get_farmer(request):
    request_param=request.GET
    print(request_param)
    phone_number = request_param.get("phone_no")
    print(phone_number)
    farmer_objects = Farmer.objects.get(phone_no = phone_number)
    farmer_objs= farmer_objects.name
    result_json ={"Farmer":farmer_objs}
    return JsonResponse(result_json)


