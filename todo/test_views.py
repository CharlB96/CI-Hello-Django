from django.test import TestCase
from .model import Item

# Create your tests here.


class TestViews():

    def test_get_todo_list(self):
        self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')


    def test_get_edit_item_page(self):
        item = Item.objects.create(name = "test todo item")
         self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    
    def test_can_add_item(self):
        response = self.client.post('/add', {'name': Test Added Item})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):


    def test_can_toggle_item(self):