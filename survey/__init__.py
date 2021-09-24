from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    payment_constant=cu(5.00)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    points = models.CurrencyField()
    pass


class Player(BasePlayer):
    num = models.IntegerField(label='Tell me a number', min=13, max=125)


# FUNCTIONS
"""def set_payoffs(player: Player):
    #participant = player.participant
    if player.age == 20:
         player.payoff = Constants.pago"""

def set_payoffs(group: Group):
    players = group.get_players()
    for p in players:
        if p.num == 20:
            p.payoff = Constants.payment_constant


#def set_payoffs(player, values):
#        if player.gender=='Mujer':
#            player.payoff= cu(5)



# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['num']

class ResultsWaitPage(WaitPage):
    body_text = "Waiting for the other participant to decide."
    after_all_players_arrive = set_payoffs


class Results(Page):
     pass


page_sequence = [Demographics,  Results]
