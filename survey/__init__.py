from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    payment_constant=cu(5.00)
    nopayment = cu(0.00)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    points = models.CurrencyField()
    pass


class Player(BasePlayer):
    num = models.IntegerField(label='Tell me a number', min=13, max=125)
    palabra1= models.StringField(label='Escriba la palabra en su forma alfanumérica. Recuerde respetar minúsculas y mayúsculas')
    palabra2= models.StringField(label='Escriba la palabra en su forma alfanumérica', initial='') #Si no pongo initial, lo tomará como valor nulo
    palabra3 = models.StringField(label='Escriba la palabra en su forma alfanumérica. Recuerde respetar minúsculas y mayúsculas')
    palabra4 = models.StringField(label='Escriba la palabra en su forma alfanumérica',initial='')
    palabra5 = models.StringField(label='Escriba la palabra en su forma alfanumérica. Recuerde respetar minúsculas y mayúsculas')
    palabra6 = models.StringField(label='Escriba la palabra en su forma alfanumérica',  initial='')
    palabra7 = models.StringField(label='Escriba la palabra en su forma alfanumérica. Recuerde respetar minúsculas y mayúsculas')
    palabra8 = models.StringField(label='Escriba la palabra en su forma alfanumérica',initial='')
    palabra9 = models.StringField(label='Escriba la palabra en su forma alfanumérica. Recuerde respetar minúsculas y mayúsculas')
    palabra10 = models.StringField(label='Escriba la palabra en su forma alfanumérica', initial='')
    palabra11 = models.StringField(label='Escriba la palabra en su forma alfanumérica. Recuerde respetar minúsculas y mayúsculas')
    palabra12 = models.StringField(label='Escriba la palabra en su forma alfanumérica', initial='')
    palabra13 = models.StringField(label='Escriba la palabra en su forma alfanumérica. Recuerde respetar minúsculas y mayúsculas')
    palabra14 = models.StringField(label='Escriba la palabra en su forma alfanumérica', initial='')

# FUNCTIONS
"""def set_payoffs(player: Player):
    #participant = player.participant
    if player.age == 20:
         player.payoff = Constants.pago"""

"""def set_payoffs1(player: Player):
    if player.palabra1 == "ch":
        player.payoff = player.payoff + Constants.payment_constant"""

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

def set_payoffs3(group: Group):
    players = group.get_players()
    for p in players:
        if p.palabra3 == "ch":
            p.payoff = p.payoff + Constants.payment_constant

def set_payoffs4(group: Group):
    players = group.get_players()
    for p in players:
        if p.palabra4 == "añ":
            p.payoff = p.payoff + Constants.payment_constant

def set_payoffs5(group: Group):
    players = group.get_players()
    for p in players:
        if p.palabra5 == "ch":
            p.payoff = p.payoff + Constants.payment_constant

def set_payoffs6(group: Group):
    players = group.get_players()
    for p in players:
        if p.palabra6 == "añ":
            p.payoff = p.payoff + Constants.payment_constant

def set_payoffs7(group: Group):
    players = group.get_players()
    for p in players:
        if p.palabra7 == "ch":
            p.payoff = p.payoff + Constants.payment_constant

def set_payoffs8(group: Group):
    players = group.get_players()
    for p in players:
        if p.palabra8 == "añ":
            p.payoff = p.payoff + Constants.payment_constant



###WHY CAN'T I USE THIS?: Cuando hace el loop, cada vez que vea palabra 1 sumará 5 más, se sumará todo al final.
def set_payoffs(group: Group):
    players = group.get_players()
    for p in players:
        #p.payoff = Constants.nopayment
        if p.palabra1 == "ch" or p.palabra2 == "añ" or p.palabra3== "ch" or p.palabra4 == "añ" or p.palabra5 == "ch" or p.palabra6 == "añ" or p.palabra7 == "ch" or p.palabra8 == "añ":
           p.payoff = p.payoff + Constants.payment_constant
        else:
           p.payoff=p.payoff + Constants.nopayment


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['palabra1'] #'num',
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if player.palabra1 == "ch":
                player.payoff = player.payoff + Constants.payment_constant



class Demographics2(Page):
    form_model = 'player'
    form_fields = ['palabra2']


class Demographics3(Page):
    form_model = 'player'
    form_fields = ['palabra3'] #'num',


class Demographics4(Page):
    form_model = 'player'
    form_fields = ['palabra4']


class Demographics5(Page):
    form_model = 'player'
    form_fields = ['palabra5']  # 'num',


class Demographics6(Page):
    form_model = 'player'
    form_fields = ['palabra6']


class Demographics7(Page):
    form_model = 'player'
    form_fields = ['palabra7']  # 'num',


class Demographics8(Page):
    form_model = 'player'
    form_fields = ['palabra8']

class MyWaitPage1(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive= set_payoffs1


class MyWaitPage2(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive = set_payoffs2

class MyWaitPage3(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive = set_payoffs3

class MyWaitPage4(WaitPage):
     body_text = "Set payoff"
     after_all_players_arrive = set_payoffs4


class MyWaitPage5(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive = set_payoffs5


class MyWaitPage6(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive = set_payoffs6


class MyWaitPage7(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive = set_payoffs7


class MyWaitPage8(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive = set_payoffs8

"""
class MyWaitPage2(WaitPage):
    body_text = "Set payoff"
    after_all_players_arrive = set_payoffs2
"""
###Al tratarse de variables distintas usamos ResultsWaitPage distintos
class Results(Page):
     pass


page_sequence = [Demographics, Demographics2, MyWaitPage2,
                 Demographics3, MyWaitPage3, Demographics4, MyWaitPage4,
                 Demographics5, MyWaitPage5, Demographics6, MyWaitPage6,
                 Demographics7, MyWaitPage7, Demographics8, MyWaitPage8,
                 Results,
                 ] #Nunca olvides el ResultsWaitPage, sino no saldrán los nuevos valores
