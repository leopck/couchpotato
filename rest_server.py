import json
from plugin.youtube import Youtube
from plugin.anime9 import Anime9
from plugin.ffmovies import Ffmovies
from plugin.pornhub import Pornhub
from control import WebControl
from flask import Flask, request

app = Flask(__name__)
handle = None

def removeFuncWUnderscore(funcName):
    return not '__' in funcName

def getAllFunctionsForURL():
    funcCall = []
    if "youtube" in handle.getURL():
        print("youtube")
        # method = getattr(Youtube, "getTitle")
        # print(method(handle))
        funcCall = list(filter(removeFuncWUnderscore, dir(Youtube)))
    elif "9anime" in handle.getURL():
        print("9anime")
        funcCall = list(filter(removeFuncWUnderscore, dir(Anime9)))
    elif "ffmovie" in handle.getURL():
        print("ffmovies")
        funcCall = list(filter(removeFuncWUnderscore, dir(Ffmovies)))
    elif "pornhub" in handle.getURL():
        print("pornhub")
        funcCall = list(filter(removeFuncWUnderscore, dir(Pornhub)))
    return json.dumps(funcCall)

def getAllFunctionsForURLObj():
    funcCall = []
    objHandle = None
    if "youtube" in handle.getURL():
        print("youtube")
        # method = getattr(Youtube, "getTitle")
        # print(method(handle))
        objHandle = Youtube
        funcCall = list(filter(removeFuncWUnderscore, dir(Youtube)))
    elif "9anime" in handle.getURL():
        print("9anime")
        objHandle = Anime9
        funcCall = list(filter(removeFuncWUnderscore, dir(Anime9)))
    elif "ffmovie" in handle.getURL():
        print("ffmovies")
        objHandle = Ffmovies
        funcCall = list(filter(removeFuncWUnderscore, dir(Ffmovies)))
    elif "pornhub" in handle.getURL():
        print("pornhub")
        objHandle = Pornhub
        funcCall = list(filter(removeFuncWUnderscore, dir(Pornhub)))
    return json.dumps(funcCall), objHandle

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/go', methods=['GET'])
def go(url = None):
    if url == None:
        url = request.args.get('url')
    handle.go(url)
    return getAllFunctionsForURL()

@app.route('/geturl')
def geturl():
    return handle.getURL()

@app.route('/getcommands')
def getcommands():
    return getAllFunctionsForURL()

@app.route('/command', methods=['GET'])
def runcommand(command = None):
    if command == None:
        command = request.args.get('command')
    
    listofallcommands, webPlugins = getAllFunctionsForURLObj()
    if command in listofallcommands:
        plugin = webPlugins(handle)
        method = getattr(plugin, command)
        results = method()
    return results

@app.route('/testfunc')
def testfunc():
    getAllFunctionsForURL()
    return 'Server Works!'

if __name__ == "__main__":
    handle = WebControl()
    app.run()