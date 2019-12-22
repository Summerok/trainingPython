# -*-coding:Latin-1 -*
import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        self.assertIn(elt, liste)
    
    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        liste = list(range(10))
        random.shuffle(liste)
        liste.sort()
        self.assertEqual(liste, list(range(10)))
        
    def test_sample(self):
        """Teste le fonctionnement de la fonction 'random.sample'."""
        liste = list(range(10))
        extrait = random.sample(liste, 9)
        for elt in extrait:
            self.assertIn(elt, extrait)
        
        self.assertRaises(ValueError, random.sample, liste, 20)



unittest.main()        