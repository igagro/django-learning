from django.core.management.base import BaseCommand
from pkg.models import Role, Permission, RolePermission


class Command(BaseCommand):

    help = 'Populate database with roles and permsissions'

    def _populate_db(self):
        unv_role = Role.objects.create(name='UniversityAdmin', role_type='UNV')
        sch_role = Role.objects.create(name='SchoolAdmin', role_type='SCH')

        add = Permission.objects.create(name='ADD')
        edit = Permission.objects.create(name='EDIT')
        delete = Permission.objects.create(name='DELETE')

        RolePermission.objects.create(role=unv_role, permission=add)
        RolePermission.objects.create(role=unv_role, permission=edit)
        RolePermission.objects.create(role=unv_role, permission=delete)
        RolePermission.objects.create(role=sch_role, permission=add)
        RolePermission.objects.create(role=sch_role, permission=edit)
        RolePermission.objects.create(role=sch_role, permission=delete)

    def handle(self, *args, **options):
        self._populate_db()
