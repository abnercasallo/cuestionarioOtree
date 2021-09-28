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
    palabra1= models.StringField(label='Escriba la palabra en su forma alfanumérica. Recuerde respetar minúsculas y mayúsculas')
    palabra2= models.StringField(label='Escriba la palabra en su forma alfanumérica')


# FUNCTIONS
"""def set_payoffs(player: Player):
    #participant = player.participant
    if player.age == 20:
         player.payoff = Constants.pago"""

def set_payoffs1(group: Group):
    players = group.get_players()
    for p in players:
        if p.palabra1 == "ch":
            p.payoff = p.payoff + Constants.payment_constant

def set_payoffs2(group: Group):
    players = group.get_players()
    for p in players:
        if p.palabra2 == "añ":
            p.payoff = p.payoff + Constants.payment_constant

###WHY CAN'T I A USE THIS?:
"""def set_payoffs(group: Group):
    players = group.get_players()
    for p in players:
  #      if p.num == 20:
  #          p.payoff = Constants.payment_constant
        if p.palabra1 == "ch" or p.palabra2 == "añ": ##Si no lo haces separado el palabra 2 se llenara como null y no correrá
            p.payoff = p.payoff + Constants.payment_constant
     
        #if p.palabra2 == "añ":
        #    p.payoff = p.payoff + Constants.payment_constant
"""


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['palabra1'] #'num',


class Demographics2(Page):
    form_model = 'player'
    form_fields = ['palabra2']

class MyWaitPage1(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive = set_payoffs1



class MyWaitPage2(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive = set_payoffs2

###Al tratarse de variables distintas usamos ResultsWaitPage distintos
class Results(Page):
     pass


page_sequence = [Demographics, MyWaitPage1, Demographics2, MyWaitPage2,   Results] #Nunca olvides el ResultsWaitPage, sino no saldrán los nuevos valores
