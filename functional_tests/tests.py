# -*- coding: utf-8 -*-
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith ouviu falar sobre um novo app online muito legal.
        # Então ela foi dar uma olhada na homepage.
        self.browser.get(self.live_server_url)

        # Ela notou que a página tem To-Do escrito na título e em seu
        # cabeçalho.
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ela então é convidada a adicionar um item a lista de To-Do.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ela digitou "Buy peacock feathers" na text box.
        inputbox.send_keys('Buy peacock feathers')

        # Quando ela aperta enter, ela é levada a uma nova url, e
        # agora a página lista "1: Buy peacock feathers" como um item
        # em uma tabela de To-Do's.
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Ainda existe um text box sugerindo a ela que adicione outro
        # item. Ela então digita "Use peacock feathers to make a fly".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # A página atualiza de novo, e agora ela tem dois items em sua
        # lista.
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly'
        )
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Agora um novo usuário, Francis, acessa o site.

        # Nós utilizaremos uma nova sessão do navegador para termos
        # certeza de que nenhuma informação de Edith esteja presente
        # mesmo nos cookies do site.
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Francis visita a página e não há qualquer sinhal da lista de
        # Edith.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Use peacock feathers to make a fly', page_text)

        # Francis inicia uma nova lista adicionando um novo item. Ele
        # é menos interessante que Edith.
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys("Buy milk")
        input_box.send_keys(Keys.ENTER)

        # Francis vai para sua url única.
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Novamente, não há sinal da lista de Edith.
        page_text = self.broser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Edith se pergunta se o site vai se lembrar de sua lista.
        # Então ela nota que o site gerou uma URL única para ela.
        # -- Isto é mais um texto explicativo de um efeito.

        # Ela visita aquela URL - sua lista de To-do's continua lá.

        # Satisfeitos, os dois foram dormir.
        self.fail("Finish the test!")
