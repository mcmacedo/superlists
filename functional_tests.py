# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith ouviu falar sobre um novo app online muito legal.
        # Então ela foi dar uma olhada na homepage.
        self.browser.get('http://localhost:8000')

        # Ela notou que a página tem To-Do escrito na título e em seu
        # cabeçalho.
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # Ela então é convidada a adicionar um item a lista de To-Do.

        # Ela digitou "Buy peacock feathers" na text box.

        # Quando ela aperta enter, a página atualiza, e agora a página
        # lista. #1: Buy peacock feather como uma item da lista de
        # To-Do's.

        # Ainda existe um text box sugerindo a ela que adicione outro
        # item. Ela então digita "Use peacock feathers to make a fly".

        # A página atualiza de novo, e agora ela tem dois items em sua
        # lista.

        # Edith se pergunta se o site vai se lembrar de sua lista.
        # Então ela nota que o site gerou uma URL única para ela.
        # -- Isto é mais um texto explicativo de um efeito.

        # Ela visita aquela URL - sua lista de To-do's continua lá.

        # Satisfeita, ela vai dormir.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
