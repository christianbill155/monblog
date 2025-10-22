from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Article, Category
#from django.contrib.auth.models import User

User = get_user_model()

class ArticleModelTest(TestCase):

    def setUp(self):
         
        # Créer un utilisateur de test
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Test Category')
        

    def test_article_creation(self):
        article = Article.objects.create(
            title='Test Article',
            content='Test content',
            author=User.objects.get(username='testuser'),  # Utiliser l'instance de User
            category=self.category
        )
        self.assertEqual(article.title, 'Test Article')
        self.assertEqual(article.content, 'Test content')
        self.assertEqual(article.author, self.user)
        self.assertEqual(article.category, self.category)

    def test_str_representation(self):
        article = Article(
            title="my article",
            content="my content",
            author=self.user # Ajouter l'auteur
        )
        self.assertEqual(str(article), "my article")

## Additional tests can be added here for other models and views
from django.test import TestCase, Client
from django.urls import reverse

class ArticleViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'

        )   
        self.category = Category.objects.create(name='Test Category')
        self.article = Article.objects.create(
            title='Test Article',
            content='Test content',
            author=User.objects.get(username='testuser'),
            category=self.category
        )
    def test_article_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Test Article')
        # self.assertTemplateUsed(response, 'blog/article_list.html') 
    
    def test_creation_view_requires_login(self):
        response = self.client.get(reverse('create_article'))
        self.assertEqual(response.status_code, 302)  # Redirige vers la page de login

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('create_article'))
        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, 'blog/create_article.html')