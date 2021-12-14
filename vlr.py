from bs4 import BeautifulSoup as bs
import requests
import itertools
import time
class Match:
    def __init__(self,link):
        match = requester(link)
        self.match=match

    def map(self):
        map=self.match.find_all('div',class_='map')
        maps=[]
        mapsf=[]
        for i in map:
            maps.append(i.span.text.strip())
        for i in maps:
            i= i.replace('\n', '')
            i= i.replace('\t', '')
            i= i.replace('PICK','')
            mapsf.append(i)
        return mapsf
    def event(self):
        event=self.match.find('div',style='font-weight: 700;').text.strip()
        return event
    def round(self):
        round=self.match.find('div',class_='match-header-event-series').text.strip()
        round= round.replace('\n','')
        round= round.replace('\t','')
        return round
    def scores(self):
        scores = self.match.find_all('div', class_='score')
        scorel=[]
        for i in scores:
            scorel.append(i.text.strip())
        return scorel
    def leftteam(self):
        leftteamname = ''
        leftteam=self.match.find('div', class_='team').text.strip()
        leftteam= leftteam.replace('\n','')
        leftteam= leftteam.replace('\t','')
        for i in leftteam:
            if i.isalpha() == True or i == ' ':
                leftteamname += i
        return leftteamname.strip()

    def rightteam(self):
        rightteamname = ''
        rightteam=self.match.find('div', class_='team mod-right').text.strip()
        rightteam= rightteam.replace('\n','')
        rightteam= rightteam.replace('\t','')
        for i in rightteam:
            if i.isalpha() == True:
                rightteamname += i
        return  rightteamname.strip()
    def mapscore(self):
        mapscore=[]
        maps=self.map()
        score=self.scores()
        x=0
        y=2
        if len(maps)==1:
            slist=[]
            mlist=[]
            mlist.append(maps[0])
            slist.append(score[0:2])
            mlist.extend(slist)
            mapscore.append(tuple(mlist))
            return mapscore
        else:
            for i in maps:
                mlist=[]
                slist=[]
                mlist.append(i)
                slist.append(score[x:y])
                mlist.extend(slist)
                mapscore.append(tuple(mlist))
                x+=2
                y+=2
            return mapscore
    def __str__(self):
        winner=''
        lwinner=0
        rwinner=0
        s=self.mapscore()
        rightteam= self.rightteam()
        leftteam= self.leftteam()
        map = self.map()
        if len(self.mapscore()) == 1:
            if int(s[0][1][0]) > int(s[0][1][1]):
                output = (str(leftteam) + ' beat ' + str(rightteam) + str(s[0][1][0]) + ' to ' + str(s[0][1][1]) + ' on' + str(map[0]) + '.')
                lwinner += 1
            else:
                output = (str(rightteam) + ' beats ' + str(leftteam) + str(s[0][1][1]) +  ' to ' + str(s[0][1][0]) + ' on ' + str(map[0]) + '.')
                rwinner +=1
        else:
            mbuff = 0
            sbuff = 0
            for i in s:
                if int(s[sbuff][1][0]) > int(s[sbuff][1][1]):
                    output += (leftteam + ' beats ' + rightteam +' '+ str(s[sbuff][1][0]) + ' to ' + str(s[sbuff][1][1]) + ' on ' +
                          str(map[mbuff]) + '.' +'\n')
                    mbuff += 1
                    sbuff += 1
                    lwinner += 1
                else:
                    output += (rightteam + ' beats ' + leftteam +' '+ str(s[sbuff][1][1]) + ' to ' + str(s[sbuff][1][0]) + ' on ' +
                          str(map[mbuff]) + '.'+'\n')
                    mbuff += 1
                    sbuff += 1
                    rwinner +=1
        mbuff=0
        sbuff=0

        if lwinner > rwinner:
            winner = leftteam +' '+ str(lwinner)+'-'+str(rwinner) + ' ' + rightteam
        else:
            winner = rightteam +' '+ str(rwinner) + '-' + str(lwinner)+' ' + leftteam

        final_score = self.event() +' '+ self.round()+'\n'+ winner.lstrip() +'\n'+ output

        if len(final_score) > 280:
            output=''
            for i in s:
                if int(s[sbuff][1][0]) > int(s[sbuff][1][1]):
                    output += (str(s[sbuff][1][0]) + ' to ' + str(s[sbuff][1][1])+' ' + leftteam +' on ' +
                          str(map[mbuff]) + '.' +'\n')
                    mbuff += 1
                    sbuff += 1
                else:
                    output += (str(s[sbuff][1][1]) + ' to ' + str(s[sbuff][1][0])+' ' + rightteam +' on ' +
                          str(map[mbuff]) + '.'+'\n')
                    mbuff += 1
                    sbuff += 1
            final_score = str(self.event()) +' '+ str(self.round())+'\n\n'+ winner.lstrip() +'\n\n'+ str(output)

        return f"{final_score}"

def live_matches():
    match = requester('https://www.vlr.gg/matches')
    m1=match.find_all('div',class_='wf-card')
    matchlist=[]
    for i in m1:
        m1link=i.find_all('a')
        for s in m1link:
                matchlist.append(s['href'])
    matchlist.pop(0)
    matchlist.pop(0)
    livelist=[]
    for i in matchlist:
        game = requester('https://www.vlr.gg'+i)
        final = game.find('div', class_='match-header-vs-note').text.strip()
        if final == 'live':
            livelist.append('https://www.vlr.gg'+i)
        else:
            pass
    return livelist

def is_completed(matchurl):
    game = requester(matchurl)
    final = game.find('div', class_='match-header-vs-note').text.strip()
    if final == 'final':
        return True
    else:
        return False
def requester(url):
    retry_count = itertools.count()
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    while True:
        try:
            src = requests.get(url, user_agent, timeout=10)
            src.raise_for_status()
        except:
            if next(retry_count) <= 5:
                print("timeout, wait and retry:")
                time.sleep(30)
                continue
            else:
                print("timeout, exiting")
                raise  # reraise exception to exit
        break
    html_text = src.text
    return bs(html_text, 'lxml')
