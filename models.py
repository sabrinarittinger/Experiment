from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random, math, numpy, time

doc = """
This is an experiment with repeating 5 rounds of pay-off decisions in a tournament condition."""


class Constants(BaseConstants):
    name_in_url = 'tournament'
    players_per_group = 6
    num_rounds = 60 
    endowment = c(0)
    
    
                
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    name = models.StringField(label="Your name:")
    
    selection = models.PositiveIntegerField(
        verbose_name = "Please enter your choice of output on a scale from 1 to 20.",
        initial = 0,
        min=1, 
        max=20
    )
    
    sabotage1 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
        
    )
    sabotage2 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
        
    )
    sabotage3 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
       
    )
    sabotage4 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
      
    )
    sabotage5 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage6 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    
    sabotage11 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage22 = models.PositiveIntegerField(
       # widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage33 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage44 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage55 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage66 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    
    sabotage111 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage222 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage333 = models.PositiveIntegerField(
       # widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage444 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage555 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    sabotage666 = models.PositiveIntegerField(
        #widget=widgets.Slider(),
        verbose_name = "Please enter your amount you want to sabotage (subtract)! (Remember: 0 is also possible!)",
        initial = 0,
        min=0, 
        max=200
    )
    choicefeedback = models.BooleanField(
            verbose_name = "Display Feedback",
            widget=widgets.RadioSelect, choices=[[True, "Yes"],[False, "No"]]
            #was passiert bei keinem Anklicken ??
    )
    
    def vars_for_template(self):
        return{'reveal':self.reveallist(),'namecheck': self.namecheck(), 'resultphase':self.resultphase(),'sabotagelist':self.sabotagelist(),'sabotageleft15':self.sabotageleft15(), 'sabotageleft30':self.sabotageleft30(), 'sabotageleftend':self.sabotageleftend(),'rundennr': self.rundennr(), 'resultlistend':self.resultlistend(),
               'resultlist1': self.resultlist1(), 'resultlist2':self.resultlist2(),'resultlist':self.resultlist(),'name':self.playername(),'outcomefeedback': self.outcomefeedback(), 'feedback': self.feedyesno(), 'timebonus': self.time_bonus(), 
               'listfeedback': self.selectionlist(), 'periodfeedback': self.feedbacklist()}
    
    def sabotagelist(self):
        sabotagelist = []
        for i in range(0,18):
            sabotagelist.append(0)
        if (self.round_number>15):
            sabotagelist[0]=(self.in_round(15).sabotage1)
            sabotagelist[1]=(self.in_round(15).sabotage2)
            sabotagelist[2]=(self.in_round(15).sabotage3)
            sabotagelist[3]=(self.in_round(15).sabotage4)
            sabotagelist[4]=(self.in_round(15).sabotage5)
            sabotagelist[5]=(self.in_round(15).sabotage6)
            
        if(self.round_number>30):
            sabotagelist[6]=(self.in_round(30).sabotage11)
            sabotagelist[7]=(self.in_round(30).sabotage22)
            sabotagelist[8]=(self.in_round(30).sabotage33)
            sabotagelist[9]=(self.in_round(30).sabotage44)
            sabotagelist[10]=(self.in_round(30).sabotage55)
            sabotagelist[11]=(self.in_round(30).sabotage66)

        if(self.round_number>45):
            sabotagelist[12]=(self.in_round(45).sabotage111)
            sabotagelist[13]=(self.in_round(45).sabotage222)
            sabotagelist[14]=(self.in_round(45).sabotage333)
            sabotagelist[15]=(self.in_round(45).sabotage444)
            sabotagelist[16]=(self.in_round(45).sabotage555)
            sabotagelist[17]=(self.in_round(45).sabotage666)
            
        self.participant.vars['sabotagelist']=sabotagelist
        return self.participant.vars['sabotagelist']
    
    def sabotageleft15(self):
        sabotagesum = 0
        sabotageleft=200
        if(self.round_number>15):
            for i in range(0,6):
                sabotagesum = sabotagesum + self.in_round(15).sabotagelist()[i]
                sabotageleft = sabotageleft-sabotagesum 
        self.participant.vars['sabotageleft15']=sabotageleft
        return self.participant.vars['sabotageleft15']
    
    def sabotageleft30(self):
        sabotagesum = 0
        sabotageleft=200
        if(self.round_number>30):
            for i in range(0,12):
                sabotagesum = sabotagesum + self.in_round(30).sabotagelist()[i]
                sabotageleft = sabotageleft-sabotagesum 
        self.participant.vars['sabotageleft30']=sabotageleft
        return self.participant.vars['sabotageleft30']
    
    def sabotageleftend(self):
        sabotagesum = 0
        sabotageleft=200
        if(self.round_number>45):
            for i in range(0,18):
                sabotagesum = sabotagesum + self.in_round(45).sabotagelist()[i]
                sabotageleft = sabotageleft-sabotagesum 
        self.participant.vars['sabotageleftend']=sabotageleft
        return self.participant.vars['sabotageleftend']
    
    def sabotagereduction15(self):
        sabotagered = []
        grouplist = self.group.get_players()
        playerred = 0
        if(self.round_number>15):
            for i in range(0,6):
                for player in grouplist:
                    playerred = playerred + player.in_round(15).sabotagelist()[i]
                sabotagered.append(playerred)
        return sabotagered
    
    def sabotagereduction30(self):
        sabotagered = []
        grouplist = self.group.get_players()
        playerred = 0
        if(self.round_number>30):
            for i in range(6,12):
                for player in grouplist:
                    playerred = player.in_round(30).sabotagelist()[i]
                sabotagered.append(playerred)
        return sabotagered
    
    def sabotagereduction45(self):
        sabotagered = []
        grouplist = self.group.get_players()
        playerred = 0
        if(self.round_number>45):
            for i in range(12,18):
                for player in grouplist:
                    playerred = player.in_round(45).sabotagelist()[i]
                sabotagered.append(playerred)
        return sabotagered
    
    def feedyesno(self):
        self.participant.vars['feedback']= self.choicefeedback
        return self.participant.vars['feedback']
    
    def playername(self):
        groupnames = []
        grouplist = self.group.get_players()
        for player in grouplist:
            groupnames.append(str(player.in_round(1).name))
        self.participant.vars['name']=groupnames 
        return self.participant.vars['name']
    
    def reveallist(self):
        reveallist = []
        grouplist = self.group.get_players()
        reveallist.append(str(grouplist[3].in_round(1).name))
        reveallist.append(str(grouplist[4].in_round(1).name))
        reveallist.append(str(grouplist[2].in_round(1).name))
        reveallist.append(str(grouplist[5].in_round(1).name))
        reveallist.append(str(grouplist[1].in_round(1).name))
        reveallist.append(str(grouplist[5].in_round(1).name))
        reveallist.append(str(grouplist[0].in_round(1).name))
        reveallist.append(str(grouplist[4].in_round(1).name))
        reveallist.append(str(grouplist[0].in_round(1).name))
        reveallist.append(str(grouplist[3].in_round(1).name))
        reveallist.append(str(grouplist[1].in_round(1).name))
        reveallist.append(str(grouplist[2].in_round(1).name))
        counter=0
        for i in range(0,6):
            if(self.id_in_group == i+1):
                reveal = [reveallist[counter], reveallist[counter+1]]
                counter=counter+2
        self.participant.vars['reveal']=reveal
        return self.participant.vars['reveal']
            
    def namecheck(self):
        self.participant.vars['namecheck']=str(self.in_round(1).name)
        return self.participant.vars['namecheck']
    #<?phpecho({{name}});?> 
    def resultlist(self):
        resultlist = []
        grouplist = self.group.get_players()
        calc = 0
        if(self.round_number >= 15):
            for player in grouplist:
                for i in range(0,15):
                    calc = calc + self.outputfromtable(player.selectionlist()[i], i+1)
                resultlist.append(calc)
        self.participant.vars['resultlist']=resultlist
        return self.participant.vars['resultlist']
    
    def resultlist1(self):
        resultlist1 = []
        grouplist = self.group.get_players()
        calc = 0
        if(self.round_number >= 30):
            for player in grouplist:
                for i in range(0,30): #16
                    calc = calc + self.outputfromtable(player.selectionlist()[i], i+1)
                resultlist1.append(calc)
            for i in range(0,6):
                resultlist1[i] = resultlist1[i]-self.sabotagereduction15()[i]
        self.participant.vars['resultlist1']=resultlist1
        return self.participant.vars['resultlist1']
    
    def resultlist2(self):
        resultlist2 = []
        grouplist = self.group.get_players()
        calc = 0
        if(self.round_number >= 45):
            for player in grouplist:
                for i in range(0,45): #31
                    calc = calc + self.outputfromtable(player.selectionlist()[i], i+1)
                resultlist2.append(calc)
            for i in range(0,6):
                resultlist2[i] = resultlist2[i]-self.sabotagereduction30()[i]
        self.participant.vars['resultlist2']=resultlist2
        return self.participant.vars['resultlist2']
    
    def resultlistend(self):
        resultlistend = []
        grouplist = self.group.get_players()
        calc = 0
        if(self.round_number ==60):
            for player in grouplist:
                for i in range(0,60):
                    calc = calc + self.outputfromtable(player.selectionlist()[i], i+1)
                resultlistend.append(calc)
            for i in range(0,6):
                resultlistend[i] = resultlistend[i]-self.sabotagereduction45()[i]
        self.participant.vars['resultlistend']=resultlistend
        return self.participant.vars['resultlistend']
    
    def selectionlist(self):
        selectionlist = []
        #outcomelist = []
        for i in range(60):
            selectionlist.append(0)
            selectionlist[i]=self.in_round(i+1).selection
        self.participant.vars['listfeedback']=selectionlist
        return self.participant.vars['listfeedback']
    
    def results(self, fromround, toround):
        result = 0
        if(self.round_number >= toround):
            for i in range(fromround, toround+1):
                result = result + (self.outputfromtable(self.selectionlist()[i-1], i))
        return result
    
    def resultphase(self):
        resultphase = self.results(self.round_number-4,self.round_number)
        sumuntilphase = self.results(1,self.round_number)
        self.participant.vars['resultphase']=[resultphase,sumuntilphase]
        return self.participant.vars['resultphase']
    
    
    def feedbacklist(self):
        feedbacklist = []
        start = [1,6,11,16,21,26,31,36,41,46,51,56,60]
        for j in range(12):
            if (self.round_number in range(start[j], start[j+1])):
                for i in range(start[j], start[j]+5):
                    if i >= self.round_number+1:
                        feedbacklist.append('Noch keine Eingabe')
                    else:
                        feedbacklist.append(self.participant.vars['listfeedback'][i-1])
        self.participant.vars['periodfeedback']=feedbacklist
        return self.participant.vars['periodfeedback']
            
    def outcomefeedback(self):
        outcomefeedback = []
        start = [1,6,11,16,21,26,31,36,41,46,51,56,60]
        for j in range(12):
            if (self.round_number in range(start[j], start[j+1])):
                for i in range(start[j], start[j]+5):
                    if i >= self.round_number+1:
                        outcomefeedback.append('Noch kein Ergebnis')
                    else:
                        outcomefeedback.append(self.outputfromtable(self.selectionlist()[i-1], self.round_number))
                    
        self.participant.vars['outcomefeedback']=outcomefeedback
        return self.participant.vars['outcomefeedback']
                    
   
    def time_bonus(self):
        bonus = math.floor((self.in_round(self.round_number).get_timeout_seconds())) #durch 5 teilen weil Umrechnung in Bonuspunkte??
        return bonus
    
    
    def rundennr(self):
        rundennr = self.round_number
        self.participant.vars['rundennr']=rundennr
        return self.participant.vars['rundennr']
       
       #<p> Rundennummer {{rundennr}} von 60 </p>
   
    def outputfromtable(self, select, number):
        payoffmatrix = [0] * 20
        for k in range(20):
            payoffmatrix[k] = [0]*20
        #matrix = [[0 for x in range(w)] for y in range(h)] 
        outcomes = [5,5,10,20,20,30,30,30,45,45,60,60,60,80,80,95,95,95,100,100]
        for i in range(20):
            for j in range(20):
                if(j>=i):
                    payoffmatrix[i][j]=outcomes[i]
        matrixnew = payoffmatrix
        stateofnature= [17,17,17,17,17,6,6,6,6,6,14,14,14,14,14,10,10,10,10,10,7,7,7,7,7,12,12,12,12,12,4,4,4,4,4,16,16,16,16,16,11,11,11,11,11,6,6,6,6,6,14,14,14,14,14,17,17,17,17,17]
        state = stateofnature[number-1]
        result = 0 
        if (select > 0):
            result = matrixnew[select-1][state-1]
        return result
    
    
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry'] - time.time() > 3
    