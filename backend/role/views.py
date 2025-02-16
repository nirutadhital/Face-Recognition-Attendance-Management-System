from rest_framework import generics, mixins
from role.serializers import RoleSerializer
from role.models import Role



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

