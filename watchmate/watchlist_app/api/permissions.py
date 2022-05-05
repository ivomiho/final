from rest_framework import permissions

class AdminoRReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
      if request.method  in permissions.SAFE_METHODS:
          return True
      else:
          return bool(request.user and request.user.is_staff)


    
class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return object.review_user == request.user or request.user.is_staff
    
        
    