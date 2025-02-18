from rest_framework import generics, mixins
from role.serializers import RoleSerializer, UserInRoleSerializer
from role.models import Role, UserInRole



class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset=Role.objects.all()
    serializer_class=RoleSerializer
    
    def perform_create(self, serializer):
        serializer.save(company_id=1)

role_list_create_view=RoleListCreateAPIView.as_view()


class RoleUpdateAPIView(generics.UpdateAPIView):
    queryset=Role.objects.all()
    serializer_class=RoleSerializer

role_update_view=RoleUpdateAPIView.as_view()



class RoleDestroyAPIView(generics.DestroyAPIView):
    queryset=Role.objects.all()
    serializer_class=RoleSerializer

role_destroy_view=RoleDestroyAPIView.as_view()



#UserInRole
class UserInRoleListCreateAPIView(generics.ListCreateAPIView):
    queryset=UserInRole.objects.all()
    serializer_class=UserInRoleSerializer
    

userinrole_list_create_view=UserInRoleListCreateAPIView.as_view()


class UserInRoleUpdateAPIView(generics.UpdateAPIView):
    queryset=UserInRole.objects.all()
    serializer_class=UserInRoleSerializer

userinrole_update_view=UserInRoleUpdateAPIView.as_view()


class UserInRoleDestroyAPIView(generics.DestroyAPIView):
    queryset=UserInRole.objects.all()
    serializer_class=UserInRoleSerializer

userinrole_destroy_view=UserInRoleDestroyAPIView.as_view()
