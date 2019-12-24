# -*-coding:Latin-1 -*
import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests"""
        self.liste = list(range(10))

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste)
        self.assertIn(elt, self.liste)
    
    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)))
        
    def test_sample(self):
        """Teste le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 9)
        for elt in extrait:
            self.assertIn(elt, extrait)
        
        self.assertRaises(ValueError, random.sample, self.liste, 20)
        with self.assertRaises(ValueError):
            random.sample(self.liste,20)

    def tearDown(self):
        """Finalisation du test"""
        print("Fin du test")

      