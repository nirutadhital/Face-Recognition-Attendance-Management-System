from rest_framework import generics, mixins
from department.serializers import DepartmentSerializer
from department.models import Department



class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    
    def perform_create(self, serializer):
        serializer.save(company_id=1)

department_list_create_view=DepartmentListCreateAPIView.as_view()


class DepartmentUpdateAPIView(generics.UpdateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

department_update_view=DepartmentUpdateAPIView.as_view()



class DepartmentDestroyAPIView(generics.DestroyAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

department_destroy_view=DepartmentDestroyAPIView.as_view()
