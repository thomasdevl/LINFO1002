import unittest
import os
import pathlib

from moon import dico_naiss_lune
from db.dat import data

class Testmoon(unittest.TestCase):
    '''
    ce que la fonction dico_naiss_lune est censé renvoyer :

    Pre: liste de tuple avec les naissances au format dd/mm/yyyy
    Post: un dictionnaire avec en key la date et en def le nombre de naissance en période lunaire(1) ou en période normalle(0)
    '''

    def setUp(self):
        self.d1 = ('01/01/1999',) #pleine lune
        self.d2 = ('29/12/1999',)
        self.d3 = ('01/02/2015',) #pleine lune
        self.d4 = ('12/04/1994',)
        self.d5 = ('01/05/2015',) #pleine lune
        self.lst_naiss = [self.d1,self.d2,self.d3,self.d4,self.d5]
        
    def test_moon(self):

        dico = dico_naiss_lune(self.lst_naiss)
        keys = dico.keys()

        self.assertEqual(type(dico),dict,"la fonction ne renv pas un dictionnaire")
        self.assertEqual(dico['01/01/1999'],'1',"la fonction ne renv pas 1 pour la pleine lune")
        self.assertEqual(dico['29/12/1999'],'0',"la fonction ne renv pas 0 pour une nuit normale")

        for key in keys:
            self.assertEqual(type(key),str,"les clés du dictionnaire ne sont pas des strings")
            self.assertEqual(type(dico[key]),str,"les déf du dico ne sont pas des strings")
            
        
class Testdb(unittest.TestCase):

    def setUp(self):
        self.db =  data(os.path.join(pathlib.Path(__file__).parent.absolute(), "db/database.sqlite"))
        self.db.connect()

        self.lst_naiss = [('01/01/1999',),('29/12/1999',),('01/02/2015',) ,('12/04/1994',),('01/05/2015',) ]

    def test_db(self):
        self.assertEqual(type(self.db.naissances()),list,"la fonction naissances ne renv pas une liste")
        self.assertEqual(type(self.db.familles()),list,"la fonction familles ne renv pas une liste")
        self.assertEqual(type(self.db.famille_en_vie()),list,"la fonction famille_en_vie ne renv pas une liste")
        self.assertEqual(type(self.db.lst_type_pourct()),list,"la fonction lst_type_pourct ne renv pas une liste")

        self.assertEqual(type(self.db.race_naissance(self.lst_naiss)),list,"la fonction race_naissance ne renv pas une liste")
        self.assertEqual(type(self.db.fam_naissance(self.lst_naiss)),list,"la fonction fam_naissance ne renv pas une liste")

        self.db.deco()


if __name__ == "__main__":
    unittest.main(verbosity=2)