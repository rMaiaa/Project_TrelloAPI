import requests
import json as js

class trello:

    def __init__ (self):
        self.key = 'd1ca877043972e85fa7514f64eafffa0'
        self.token = '06cfead3d9cf5d1be6c4037563f253c14b9f41eda3da0d46edbfd05b9cf1f7d2'
        self.board = 'gz4bNzuU'


    def getBoard(self):
        url = "https://api.trello.com/1/boards/" + self.board

        querystring = {"actions":"all","boardStars":"none","cards":"none","card_pluginData":"false","checklists":"none","customFields":"false","fields":"name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames","lists":"open","members":"none","memberships":"none","membersInvited":"none","membersInvited_fields":"all","pluginData":"false","organization":"false","organization_pluginData":"false","myPrefs":"false","tags":"false","key":self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

    def getCards(self):
        self.limit = '30'
        url = 'https://api.trello.com/1/boards/' + self.board + '/cards/?limit=' + self.limit + '&fields=name&members=true&member_fields=fullName&key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)

        print(dic)


    def getCardID(self):
        self.idCard = '62cc95b1b5e87a01b6e32ae4'
        
        url = 'https://trello.com/1/boards/' + self.board + '/cards/' + self.idCard + '?key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)

        print(dic)

    def getMember(self):
        self.member = '62cc8f0b77c4cc1f18fa2268'

        url = "https://api.trello.com/1/members/" + self.member

        querystring = {"boardBackgrounds":"none","boardsInvited_fields":"name,closed,idOrganization,pinned","boardStars":"false","cards":"none","customBoardBackgrounds":"none","customEmoji":"none","customStickers":"none","fields":"all","organizations":"none","organization_fields":"all","organization_paid_account":"false","organizationsInvited":"none","organizationsInvited_fields":"all","paid_account":"false","savedSearches":"false","tokens":"none","key": self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)