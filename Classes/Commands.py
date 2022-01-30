from datetime import datetime
import random

timeNow = datetime.now()

class Commands:

    def reflection(self):
        reflexoes = ['''Já é outro dia e você ainda está com o mesmo problema? Está desanimado, cansado pensando em largar tudo e vender coco na praia?
Lembre-se do caminho que trilhou até chegar aqui e quantos problemas já venceu..
O problema que está passando é só mais um degrau, e depende de você utrapassa-lo ou evitá-lo.
Força!! :muscle::wink: ''',
'''O pensador Guimarães Rosa tem uma máxima sobre a dificuldades da vida que chega a ser interessante compartilhar: "Viver é muito perigoso... Porque aprender a viver é o que é o viver mesmo... Travessia perigosa, mas é a vida. Sertão que se alteia e abaixa... O mais difícil não é um ser bom e proceder honesto, dificultoso mesmo, é um saber definido o que quer, e ter o poder de ir até o rabo da palavra."
Temos vários sentidos para se retirar dessa máxima, mas o final é o que importa. Para você que se sente perdido em determinado momento enquanto programa, entenda que as vezes precisamos recuar alguns passos, e enxergar o campo ou bloco como um todo. Lembre-se pensar machuca, mas o que mais machuca é saber temos medo de não pensar. Então soltar esse comando e bora codar''']
        return random.choice(reflexoes)

    def morning(self):
        return '''Bom dia'''
    
    def afternoon(self):
        return '''Boa tarde'''
    
    def night(self):
        return '''Boa noite'''

    def salutation(self):
        if timeNow.hour < 12 and timeNow.hour >= 6:
            return self.morning()
        elif timeNow.hour >= 12 and timeNow.hour < 19:
            return self.afternoon()
        else:
            return self.night()

    def commands(self):
        return {
            '<3rafa': 'oh disus',
            '<3matan': 'Pergunte-me o que quiser, que eu te darei a resposta',
            '<3arthur': 'Vou comer vidro e chorar no banho dps dessa... :smiling_face_with_tear:',
            '<3ander': 'Boa cxr, ce merece',
            '<3kyle': f'E vamos pro off topic , esse chat ficou totalmente desvirtuado',
            '<3agua': '--> Bebam Água <--', 
            '<3joelzin': 'https://tenor.com/view/tohru-dragonmaid-anime-gif-9656401',
            '<3kaway': 'A vida é uma folha em branco, e eu não tenho uma caneta',
            '<3gentil': 'Gentileza gera gentileza',
            '<3dev': 'Bem vindo(a) ao mundo da programação, daqui pra frente é só pra baixo',
            '<3alura': 'Desconto da Rafa na Alura para você: https://www.alura.com.br/promocao/rafaballerini',
            '<3redes' : 'Redes sociais da Rafa: https://beacons.ai/rafaballerini',
            '<3instagram' : 'Siga a Rafa no instagram: https://instagram.com/rafaballerini',
            '<3youtube' : 'Se inscreva no canal da Rafa: https://youtube.com/RafaellaBallerini',
            '<3twitter' : 'Siga a Rafa no twitter: https://twitter.com/ballerinirafa',
            '<3github' : 'Veja o github da Rafa: https://github.com/rafaballerini',
            '<3org' : 'Nossa organização no Github: https://github.com/Ballerini-Server',
            '<3playlist' : 'Ouça a playlist de Rock da Rafa: https://open.spotify.com/embed/playlist/5TUxgTIxzLbLVh7RUf9V8i',
            'erro': 'Esse comando não existe! :alien: Utilize "<3help" para ver as opções'
        }
