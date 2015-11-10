import pytest
from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_admin_user_groups(admin_client):
    response = admin_client.get(reverse('admin_user_groups'))
    assert response.status_code == 200
