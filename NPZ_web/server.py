from flask import Flask, render_template, redirect, request
from human import *
import random


app = Flask(__name__)



@app.route('/')          
def hello_world():
    return render_template('index.html') 

@app.route('/display')          
def display():
    
    bob = Ninja('bob',37)
    carl = Pirate('carl',22,'sword')

    zb1 = Zombie('freddie',567,'Hazel')
    return render_template('ninja.html',ninja = bob,pirate=carl,zombie = zb1)

@app.route('/tie')          
def tie_result():
    return render_template('tiedresult.html')

@app.route('/win')          
def win_result():
    return render_template('winresult.html')

@app.route('/lose')          
def lose_result():
    return render_template('loseresult.html')

@app.route('/choice',methods=['POST'])          
def choice():
    
    choice = request.form['choice']
    serverchoice = random.randint(0,2)
    choices = ['ninja','pirate','zombie']
    serverchoice = choices[serverchoice]
    WL = 'lose'
    dict = {
        'ninja':  'win' if (serverchoice == 'pirate') else 'lose',
        'pirate': 'win' if (serverchoice == 'zombie') else 'lose',
        'zombie': 'win' if (serverchoice == 'ninja') else 'lose' 
    }
    if serverchoice == choice:
        return redirect ('/tie')
    else:
        WL = dict[choice]
        return redirect('/'+WL)
    return render_template('choice.html',choice = choice) 

if __name__=="__main__":       
    app.run(debug=True) 


    