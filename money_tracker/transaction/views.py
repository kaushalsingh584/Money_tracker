from django.shortcuts import render,HttpResponse,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .models import *
from authentication.models import User,Budget


class trans(APIView):

    def post(self,request):

        made_by = request.data.get("from")
        made_to = request.data.get("to")
        amount = request.data.get("amount")
        desc = request.data.get("desc")
        type = request.data.get("type")
        category = request.data.get("category")

        made_by = User.objects.get(pk = made_by)      
        made_to = User.objects.get(pk = made_to)

        
        try:
            trans_obj = Mas_trans(made_by = made_by, made_to = made_to, amount = amount,desc = desc,category = category,type = type)
            trans_obj.save()


            made_by.budget.income -= amount
            made_to.budget.income += amount
            made_by.budget.save()
            made_to.budget.save()

            #---------------------------------- group transaction -------------------------------------------------
            if type == "group":
                group_name = request.data.get("group_name")
                grp_members = request.data.get("group_members")
                no_of_per = request.data.get("no_of_per")
                desc = request.data.get("desc")
                type = request.data.get("type")
                category = request.data.get("category")

                try: 
                    
                    group = Groups_trans(
                        group_name = group_name,
                        grp_made_by = made_by,
                        grp_trans_made_to = made_to,
                        no_of_per = no_of_per,
                        desc = desc,
                        amount_pp = amount/no_of_per
                    )

                    group.save()
                    group.grp_members.set(grp_members)
                except Exception as e:
                    print(e)
                    return Response({'message':"not valid enteries for group transaction:"+str(e)},status=HTTP_400_BAD_REQUEST)

            # -----------grup transaction end here---------------------------------------------------------------
            return Response({
                "transaction_id" : trans_obj.id,
                "budget of receiver": made_to.budget.income,
                "budget of sender": made_by.budget.income,
                },status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message':"not valid enteries"},status=HTTP_400_BAD_REQUEST)

    def get(self,request):

        try:
            trans = Mas_trans.objects.filter(made_by = request.user).order_by('-created_at')

            spent = [ { 
                    "made_by" : obj.made_by.username,
                    "made_to" : obj.made_to.username,
                    "amount" : obj.amount,
                    "desc" : obj.desc,
                    "date" : obj.created_at
            }for obj in trans]

            trans = Mas_trans.objects.filter(made_to = request.user).order_by('-created_at')

            receive= [ { "made_by" : obj.made_by.username,
                    "made_to" : obj.made_to.username,
                    "amount" : obj.amount,
                    "desc" : obj.desc,
                    "date" : obj.created_at
            }for obj in trans]

            return Response({
                "spent": spent,
                "receive":receive
            },status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self,request):

        trans_id  = request.data.get("trans_id")
        
        try:
            trans_id = Mas_trans.objects.get(pk = trans_id)
            trans_id.made_by.budget.income += trans_id.amount
            trans_id.made_to.budget.income -= trans_id.amount
            trans_id.made_by.budget.save()
            trans_id.made_to.budget.save()
            trans_id.delete()
            return Response({'message' : "Deleted successfully"},status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message' : "trans_id does not exist"},status=HTTP_400_BAD_REQUEST)
        
    def patch(self,request):

        trans_id  = request.data.get("trans_id")
        made_by = request.data.get("from")
        made_to = request.data.get("to")
        amount = request.data.get("amount")
        desc = request.data.get("desc")
        type = request.data.get("type")
        print("accepted")

        try:


            trans_id = Mas_trans.objects.get(pk = trans_id)

            # cancelling the transaction 
            trans_id.made_by.budget.income += trans_id.amount
            trans_id.made_to.budget.income -= trans_id.amount
            trans_id.made_by.budget.save()
            trans_id.made_to.budget.save()
            print("accepted")

            made_by = User.objects.get(pk = made_by)
            made_to = User.objects.get(pk = made_to)

            # updating the transaction
            trans_id.made_by = made_by
            trans_id.made_to = made_to

            trans_id.made_by.budget.income -= amount
            trans_id.made_to.budget.income += amount
            trans_id.amount = amount
            trans_id.desc = desc
            trans_id.category = type

            print("accepted")
            trans_id.made_by.budget.save()
            trans_id.made_to.budget.save()
            trans_id.save()

            print("accepted")
            return Response({'message' : "Updated successfully"},status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message' : "trans_id does not exist"},status=HTTP_400_BAD_REQUEST)



    
class groups_list(APIView):
    def get(self,request):
        grp_obj = Groups_trans.objects.all()

        l = [{
            "group_name" : obj.group_name,
            "grp_made_by" : obj.grp_made_by.username,
            "grp_trans_made_to" : obj.grp_trans_made_to.username ,
            "grp_members" :[{"name" : ob.username} for ob in obj.grp_members.all()],
            "no_of_per" : obj.no_of_per,
            "amount_pp" : obj.amount_pp
        } for obj in grp_obj]

        return Response(l,status=HTTP_200_OK)
