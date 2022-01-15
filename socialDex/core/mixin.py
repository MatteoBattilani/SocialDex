from django.contrib.auth.mixins import UserPassesTestMixin


class StaffMixin(UserPassesTestMixin):
    """
    Permissions for staff users only.
    """

    def test_func(self):
        return self.request.user.is_staff
