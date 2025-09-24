from rest_framework.permissions import BasePermission



class IsAuthor(BasePermission):
    message = "This user is not an author."
    def has_permission(self, request, view):
        print(request.user.role, request.method, "FROM PERMISSIONS")
        if request.method in ["POST", "PUT", "PATCH", "DELETE"] and request.user.role == "author":
           return True
        else:
           return False