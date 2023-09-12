# from django.test import TestCase
from unittest import TestCase
import requests
from .models import Person


class APITestCase(TestCase):
    base_url = "https://basic-crud-api.onrender.com/api/"

    def test_list(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 201)

    def test_create(self):
        data = {"name": "James Cole"}
        response = requests.post(f"{self.base_url}create/", json=data)
        self.assertEqual(response.status_code, 201)
        user_id = response.json().get("id")
        self.assertIsNotNone(user_id)


    def test_read(self):
        id = Person.objects.last().id
        response = requests.get(f"{self.base_url}{id}/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], "James Cole")

    def test_update(self):
        id = Person.objects.last().id
        data = {"name": "James Updated"}
        response = requests.put(f"{self.base_url}update/{id}/", json=data)
        self.assertEqual(response.status_code, 200)

        response = requests.get(f"{self.base_url}{id}/")
        res_data = response.json()
        self.assertEqual(res_data["name"], "James Updated")


class DeleteCase(TestCase):
    base_url = "https://basic-crud-api.onrender.com/api/"

    def test_delete(self):
        id = Person.objects.last().id
        response = requests.delete(f"{self.base_url}delete/{id}/")
        self.assertEqual(response.status_code, 204)

        response = requests.get(f"{self.base_url}{id}/")
        self.assertEqual(response.status_code, 404)