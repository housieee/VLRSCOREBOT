import vlr
import twitter
import time

live_list=[]
while True:
    clist=[]
    matchlist = vlr.live_matches()
    for i in matchlist:
        if i not in live_list:
            live_list.append(i)
        else:
            pass
    for i in live_list:
        if vlr.is_completed(i) == True:
            live_list.remove(i)
            clist.append(i)
        else:
            pass
    print('current live matches are', live_list)
    for i in clist:
        twitter.tweet(str(vlr.Match(i)))
    print('matches completed in the last 60s', clist)
    clist=[]
    time.sleep(60)
