from rest_framework.permissions import IsAuthenticated
from fruitables.helpers import custom_response
from user.serializers import UserAccountSerializer, UserAccountUpdateSerializer
from rest_framework import views

class UserAccountUpdateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserAccountSerializer(request.user)
        return custom_response('Get user successfully!', 'Success', serializer.data, 200)

    def put(self, request, *args, **kwargs):
        serializer = UserAccountUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return custom_response('Update user successfully!', 'Success', serializer.data, 200)
        return custom_response('Update user failed!', 'Error', serializer.errors, 400)
    def delete(self, request, *args, **kwargs):
        user_id = request.user.id
        try:
            user = UserAccount.objects.get(pk=user_id)
            user.delete()
            return Response({'message': 'User deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except UserAccount.DoesNotExist:
            return Response({'error': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)