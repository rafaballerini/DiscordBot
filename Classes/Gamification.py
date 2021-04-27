from Classes.Repository import Repository

repository = Repository()

class Gamification:

    def channel_reaction(self, user_id):
        # value = 100
        # data = {
        #     'user_id': user_id,
        #     'value': value
        # }
        # repository.insert_one_xp(data)
        return False

    def nice_reaction(self, user_id):
        # value = 200
        # data = {
        #     'user_id': user_id,
        #     'value': value
        # }
        # repository.update_one_xp(data)
        return False
        
        
    def bad_reaction(self, user_id):
        # value = -200
        # data = {
        #     'user_id': user_id,
        #     'value': value
        # }
        # repository.update_one_xp(data)
        return False