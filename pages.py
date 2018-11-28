from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import time, math

class Timer(Page):
    timeout_seconds = 15
    """Timer of 180 sec for the next 5 decisions starts when you click next"""
    def is_displayed(self):
        return ((self.round_number % 5) == 1)

    def before_next_page(self):
        # user has 3 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + (3*60) #Zeit für Feedback Choice wird wieder abgezogen

class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        return self.round_number == 1
    
    form_model = 'player'
    form_fields = ['name']
    pass

class PhasenFeedback(Page):
    def is_displayed(self):
        return ((self.round_number % 5)==0)
    def vars_for_template(self):
        return self.player.vars_for_template()
    
class FeedbackChoice(Page):
    form_model = 'player'
    form_fields = ['choicefeedback']
    
    def vars_for_template(self):
        return self.player.vars_for_template()
    
    def get_timeout_seconds(self):
        return self.player.get_timeout_seconds()
    #<div>
       # <button type="button" name="choicefeedback" value="True" class="btn btn-primary btn-large">Yes</button>
        #<button type="button" name="choicefeedback" value="False" class="btn btn-primary btn-large">No</button>
    #</div>
class Feedback(Page):
    
    def is_displayed(self):
        return self.player.choicefeedback
    
    def get_timeout_seconds(self):
        return self.player.get_timeout_seconds()
    
    def vars_for_template(self):
        return self.player.vars_for_template()

class Selection(Page):
    """Player: Choose how much to gain."""
    def vars_for_template(self):
        return self.player.vars_for_template()
    
    form_model = 'player'
    form_fields = ['selection']
    
    def get_timeout_seconds(self):
        return self.player.get_timeout_seconds()

    def is_displayed(self):
        return self.player.is_displayed()

    

 #   timeout_submission = {'contribution': c(Constants.endowment / 2)}

class Result(Page):
    def is_displayed(self):
        return (self.round_number == 15)
                
    def vars_for_template(self):
        return self.player.vars_for_template()
    
    form_model = 'player'
    form_fields = ['sabotage1', 'sabotage2', 'sabotage3', 'sabotage4', 'sabotage5', 'sabotage6']
    
    def error_message(self, values):
        print('values is', values)
        if values["sabotage1"] + values["sabotage2"] + values["sabotage3"]+values["sabotage4"] + values["sabotage5"] + values["sabotage6"]  > 200:
            return 'The numbers must add up to 200'

class Result1(Page):
    def is_displayed(self):
        return (self.round_number == 30)
    def vars_for_template(self):
        return self.player.vars_for_template()
    
    form_model = 'player'
    form_fields = ['sabotage11', 'sabotage22', 'sabotage33', 'sabotage44', 'sabotage55', 'sabotage66']
    
    def error_message(self, values):
        print('values is', values)
        if values["sabotage11"] + values["sabotage22"] + values["sabotage33"]+values["sabotage44"] + values["sabotage55"] + values["sabotage66"]  > self.participant.vars['sabotageleft15']:
            return 'The numbers must add up to 200'
        

class Result2(Page):
    def is_displayed(self):
        return (self.round_number == 45)
    def vars_for_template(self):
        return self.player.vars_for_template()
    
    form_model = 'player'
    form_fields = ['sabotage111', 'sabotage222', 'sabotage333', 'sabotage444', 'sabotage555', 'sabotage666']
    
    def error_message(self, values):
        print('values is', values)
        if values["sabotage111"] + values["sabotage222"] + values["sabotage333"]+values["sabotage444"] + values["sabotage555"] + values["sabotage666"]  > self.participant.vars['sabotageleft30']:
            return 'The numbers must add up to 200'

class ResultEnd(Page):
    def is_displayed(self):
        return (self.round_number == 60)
    def vars_for_template(self):
        return self.player.vars_for_template()
    

    
class WaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
    def after_all_players_arrive(self):
        print("Gruppenmatching")

class WaitPageResults(WaitPage):
    def is_displayed(self):
        return ((self.round_number % 15) == 0)
    def after_all_players_arrive(self):
        print("Warten auf Ergebnisse")



page_sequence = [
    Introduction,
    WaitPage,
    Timer,
    Selection,
    FeedbackChoice,
    Feedback,
    PhasenFeedback,
    WaitPageResults,
    Result,
    Result1,
    Result2,
    ResultEnd
]
