import pytest
import json


@pytest.mark.django_db
class TestMyView:
    def test_home(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_post_view(self, client):
        data = {
            "movie": ""
        }
        url = '/getrecommendation'
        response = client.post(url, data, content_type='application/json')
        assert response.status_code == 400
