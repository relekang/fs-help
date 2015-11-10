import pytest
from django.core.urlresolvers import reverse

from fs_help.lfs_help.models import Language, Topic


@pytest.fixture
def english():
    return Language.objects.create(name='English', code='en')


@pytest.fixture
def topics(english):
    common = dict(language=english, active=True, need_auth=True)
    return [
        Topic.objects.create(title='SuperTopic', slug='1', **common),
        Topic.objects.create(title='Not Topic', slug='2', **common),
    ]


@pytest.mark.django_db
def test_topics_with_no_query(admin_client, english):
    response = admin_client.get(reverse('topics'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_search_with_no_query(admin_client, english):
    response = admin_client.get(reverse('search'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_search_with_query(admin_client, english, topics):
    response = admin_client.get(reverse('search') + '?query=Super')
    assert response.status_code == 200
    assert 'Not' not in response.content
    assert 'Super' in response.content
