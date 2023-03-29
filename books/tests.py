from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import json
from .models import Category,Book
from django.contrib.auth.models import User
from time import sleep

class Tests(APITestCase):
    def test_get_and_post_with_auth_as_superuser(self):  
        #Create Test SuperUser and authenticate
        user =User.objects.create_superuser(username="test",password="test")
        self.client.force_authenticate(user=user)
        url_book =reverse("books-list")
        url_category= reverse("category-list")

        data_book = {'title':"Example title","pub_date":"2023-01-01","author":"test","description":"test","category":[1]}
        data_category = {'title':"Example Category"}

        category_post_response= self.client.post(url_category,data_category,format="json")
        category_get_response = self.client.get(url_category,format="json")

        book_post_response = self.client.post(url_book,data_book,format="json")
        book_get_response = self.client.get(url_book,format="json")

        self.assertEqual(category_post_response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(category_get_response.status_code,status.HTTP_200_OK)
        self.assertEqual(book_post_response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(book_get_response.status_code,status.HTTP_200_OK)

        self.assertEqual(User.objects.count(),1)
        self.assertEqual(Category.objects.count(),1)
        self.assertEqual(Book.objects.count(),1)

    def test_unauth_post(self):
        #Test Auth
        url_category= reverse("category-list")
        data_category = {'title':"Example Category"}

        category_post_response= self.client.post(url_category,data_category,format="json")
        category_get_response = self.client.get(url_category,format="json")

        self.assertEqual(category_post_response.status_code,status.HTTP_403_FORBIDDEN)
        self.assertEqual(category_get_response.status_code,status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(),0)
    
    def test_search(self):
        #Test if search is working
        user =User.objects.create_superuser(username="test",password="test")
        self.client.force_authenticate(user=user)
        url_book =reverse("books-list")
        url_category= reverse("category-list")
        url_search = reverse("search-list")

        data_book = {'title':"Example title","pub_date":"2023-01-01","author":"test","description":"test","category":[1]}
        data_category = {'title':"Example Category"}
        
        url_search_title = url_search+ "?title=example"
        url_search_category = url_search+"?category=1"
        url_search_author = url_search+"?author=test"

        category_post_response= self.client.post(url_category,data_category,format="json")
        book_post_response = self.client.post(url_book,data_book,format="json")

        search_get_title = self.client.get(url_search_title,format="json")
        search_get_category = self.client.get(url_search_category,format="json")
        search_get_author = self.client.get(url_search_author,format="json")


        self.assertEqual(search_get_author.status_code,status.HTTP_200_OK)
        self.assertEqual(json.loads(search_get_author.content)["results"][0]["author"],"test")

        self.assertEqual(search_get_category.status_code,status.HTTP_200_OK)
        self.assertEqual(json.loads(search_get_category.content)["results"][0]["category"],[1])

        self.assertEqual(search_get_title.status_code,status.HTTP_200_OK)
        self.assertEqual(json.loads(search_get_title.content)["results"][0]["title"],"Example title")
        
        self.assertEqual(category_post_response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(book_post_response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(Category.objects.count(),1)
        self.assertEqual(Book.objects.count(),1)

    def test_if_paginations_works(self):  
            #Create Test SuperUser and authenticate
            user =User.objects.create_superuser(username="test",password="test")
            self.client.force_authenticate(user=user)
            url_book =reverse("books-list")
            url_category= reverse("category-list")

            data_category = {'title':"Example Category"}

            category_post_response= self.client.post(url_category,data_category,format="json")
            for i in range(0,55):
                title = f"Example {i}"
                data_book = {'title':title,"pub_date":"2023-01-01","author":"test","description":"test","category":[1]}
                book_post_response = self.client.post(url_book,data_book,format="json")

            book_get_response = self.client.get(url_book,format="json")
            self.assertEqual(category_post_response.status_code,status.HTTP_201_CREATED)

            self.assertEqual(book_post_response.status_code,status.HTTP_201_CREATED)
            self.assertEqual(book_get_response.status_code,status.HTTP_200_OK)

            self.assertEqual(User.objects.count(),1)
            self.assertEqual(Category.objects.count(),1)
            self.assertEqual(Book.objects.count(),55)
            self.assertNotEqual(json.loads(book_get_response.content)["next"],None)
