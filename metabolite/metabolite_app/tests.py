from django.test import Client, TestCase
from rest_framework.test import APITestCase
from django.contrib.sessions.models import Session

from metabolite_app.models import Document

class DocumentTestCase(TestCase):

    def test_home(self):
        """
        Test Home Page GET Request
        """
        c = Client()
        get_response = c.get('')
        self.assertEqual(get_response.status_code, 200)
    
    def test_tasks(self):
        """
        Test Tasks Page GET Request
        """
        c = Client()
        get_response = c.get('/tasks')
        # redirect status response code cause request.session["doc_id"] not set
        self.assertEqual(get_response.status_code, 302)
        
        # set request.session["doc_id"]
        d1 = Document.objects.create(document='test_data/mass_spec_data_assgnmnt.xlsx')
        session = self.client.session
        session['doc_id'] = d1.id
        session.save()
        response2 = self.client.get('/tasks')
        self.assertEqual(response2.status_code, 200)

    def test_tasks_id(self):
        """
        Test Tasks_id Page GET Request
        """
        c = Client()
        get_response = c.get('/tasks/1')
        # redirect status response code cause request.session["doc_id"] not set
        self.assertEqual(get_response.status_code, 302)

class ApiTestCase(APITestCase):

    def test_filter_metabolites(self):
        """
        API Test Case : POST Request '/filter_metabolites'
        """
        c = Client()
        d1 = Document.objects.create(document='test_data/mass_spec_data_assgnmnt.xlsx')
        response = c.post('/filter_metabolites', data={'doc_id':d1.id})
        self.assertEqual(response.status_code, 201)
    
    def test_roundoff_retention(self):
        """
        API Test Case : POST Request '/roundoff_retention'
        """
        c = Client()
        d1 = Document.objects.create(document='test_data/mass_spec_data_assgnmnt.xlsx')
        response = c.post('/roundoff_retention', data={'doc_id':d1.id})
        self.assertEqual(response.status_code, 201)
    
    def test_mean_retention(self):
        """
        API Test Case : POST Request '/mean_retention'
        """
        c = Client()
        d1 = Document.objects.create(document='test_data/mass_spec_data_assgnmnt.xlsx')
        response = c.post('/mean_retention', data={'doc_id':d1.id})
        self.assertEqual(response.status_code, 201)