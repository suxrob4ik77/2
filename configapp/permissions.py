from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadPatchOnly(BasePermission):
    """
    Admin userga to'liq CRUD ruxsat.
    Teacher userga faqat GET va PATCH ruxsat.
    Student userga faqat GET ruxsat.
    """

    def has_permission(self, request, view):
        user = request.user

        # Admin foydalanuvchiga barcha ruxsat
        if user.is_authenticated and (user.is_admin or user.is_superuser):
            return True

        # Teacher foydalanuvchiga faqat GET va PATCH ruxsat
        elif user.is_authenticated and user.is_teacher:
            return request.method in SAFE_METHODS or request.method == 'PATCH'

        # Student foydalanuvchiga faqat GET ruxsat
        elif user.is_authenticated and user.is_student:
            return request.method in SAFE_METHODS
        # Parents foydalanuvchiga
        elif user.is_authenticated and user.is_parents:
            return request.method in SAFE_METHODS
        # Department uchun
        elif user.is_authenticated and user.is_course:
            return request.method in SAFE_METHODS
        # Course uchun
        elif user.is_authenticated and user.is_department:
            return request.method in SAFE_METHODS

        return False


class IsGetOrPatchOnly(BasePermission):
    """
    Faqat GET va PATCH metodlariga ruxsat beradi
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.method == 'PATCH'


class IsAdminOrTeacher(BasePermission):
    """
    Admin va Teacher foydalanuvchilarga ruxsat beradi
    Admin - to'liq ruxsat
    Teacher - faqat o'z ma'lumotlariga ruxsat
    """

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        if user.is_admin or user.is_superuser:
            return True

        if user.is_teacher:
            # Teachers can only access their own data
            if hasattr(view, 'get_queryset'):
                view.queryset = view.queryset.filter(user=user)
            return request.method in SAFE_METHODS or request.method == 'PATCH'

        return False


class IsAdminOnly(BasePermission):
    """
    Faqat Admin foydalanuvchilarga ruxsat beradi
    """

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_admin or user.is_superuser)


class IsTeacherOnly(BasePermission):
    """
    Faqat Teacher foydalanuvchilarga ruxsat beradi
    """

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_teacher


class IsStudentOnly(BasePermission):
    """
    Faqat Student foydalanuvchilarga ruxsat beradi
    """

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_student


class IsAdminOrReadOnly(BasePermission):
    """
    Admin - to'liq ruxsat
    Boshqa foydalanuvchilar - faqat o'qish ruxsati
    """

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        if user.is_admin or user.is_superuser:
            return True

        return request.method in SAFE_METHODS
