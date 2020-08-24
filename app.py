from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    """
    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('<svg height="24" class="octicon octicon-three-bars'
                                                                ' text-white" viewBox="0 0 16 16" version="1.1"'
                                                                ' width="24" aria-hidden="true"><path fill-rule='
                                                                '"evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0'
                                                                ' 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75'
                                                                ' 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75'
                                                                ' 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z">'
                                                                '</path></svg>')
            btn_sign_in.click()
        except Exception as e:
            print(f'Erro ao clicar em sign in: {e}')
     """

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('jacobkleuber@gmail.com')
            input_password.send_keys('kleuber201317')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print(f'Erro ao realizar login: {e}')

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            btn_perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper >'
                                                                  ' header > div.Header-item.position-relative.mr-0'
                                                                  ' > details > summary')
            btn_perfil.click()
        except Exception as e:
            print(f'Erro ao clicar no perfil: {e}')

    def sign_out(self):
        try:
            btn_sign_out = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper >'
                                                                    ' header > div.Header-item.position-relative.mr-0.'
                                                                    'd-none.d-md-flex > details > details-menu > form'
                                                                    ' > button')
            btn_sign_out.click()
        except Exception as e:
            print(f'Erro ao realizar logout no sistema: {e}')


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/login')
    # chrome.clica_sign_in()  # Nao esta sendo utilizado, pois estamos acessando diretamente a página de login do git
    # hub
    chrome.faz_login()
    sleep(5)
    chrome.clica_perfil()
    sleep(5)
    chrome.sign_out()
    sleep(5)
    chrome.sair()
