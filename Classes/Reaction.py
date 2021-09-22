from Data.Token import TokenDiscord
from Classes.Gamification import Gamification

tokenDiscord = TokenDiscord()
gamification = Gamification()
nice_emojis = open('Data/NiceEmojis.txt', 'r').read().split('\n')
bad_emojis = open('Data/BadEmojis.txt', 'r').read().split('\n')

id_apresentacao = tokenDiscord.uploadToken()['idapresentacao']
id_aviso = tokenDiscord.uploadToken()['idaviso']

class Reaction:

    def channel_reaction(self, event):
        if event.channel_id == id_apresentacao or event.channel_id == id_aviso:
            if not self.nice_reaction(event) and not self.bad_reaction(event):
                user = event.user_id
                gamification.channel_reaction(user)
        return False

    def nice_reaction(self, event):
        if event.emoji.name in nice_emojis:
            user = event.user_id
            gamification.nice_reaction(user)
            return True
        return False

    def bad_reaction(self, event):
        if event.emoji.name in bad_emojis:
            user = event.user_id
            gamification.bad_reaction(user)
            return True
        return False