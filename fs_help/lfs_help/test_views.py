import pytest
from django.core.urlresolvers import reverse

from fs_help.lfs_help.models import Language


@pytest.fixture
def english():
    return Language.objects.create(name='English', code='en')


@pytest.mark.django_db
def test_topics_with_no_query(admin_client, english):
    response = admin_client.get(reverse('topics'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_search_with_no_query(admin_client, english):
    response = admin_client.get(reverse('search'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_search_with_query(admin_client, english):
    response = admin_client.get(reverse('search') + '?query=something')
    assert response.status_code == 200
