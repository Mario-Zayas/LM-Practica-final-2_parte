from flask import Flask, render_template, request
import requests
import os
import json

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')

@app.route('/buscador1', methods=['GET', 'POST'])
def buscador1():
    jugador = None
    resultado= None
    url_base = "https://api.clashroyale.com/v1/"
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjUxYTcxYWU2LTA2MDgtNGYwOC04NjY1LTdmMzNhZGU5YjU2OCIsImlhdCI6MTY4NTA4MzcwOSwic3ViIjoiZGV2ZWxvcGVyL2FhY2Q5MTVjLTNmMTktNzY4Ni05NmRmLWVlM2U1OWVhODdjYSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNTguOTkuMS4yNCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.WxIJcZgO43QHOwM_6ugNy5E6ohqT2BSEPBGMQAh6qag9JJztVcFZZ8hG2I3cJTWBDnfncgp9wgfZiPfozOweXg'
    tag = request.form.get("tag")

    if tag is None:
        resultado = "resultado:  Tag no valido"
        return render_template('buscador1.html', jugador=None, resultado=resultado)

    url = url_base + "players/%23" + tag
    payload = {'Authorization': 'Bearer ' + key}
    r = requests.get(url, headers=payload)

    if r.status_code == 200:
        datos = r.json()
        jugador = datos 
    return render_template('buscador1.html', jugador=jugador, resultado=resultado)




@app.route('/buscador2', methods=['GET', 'POST'])
def buscador2():
    clans = None
    url_base = "https://api.clashroyale.com/v1/"
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFmN2U4ZTJiLTljMDgtNGNhNC05NzEwLWJiZDE4NmViNjNjYSIsImlhdCI6MTY4NTA0MDU1OCwic3ViIjoiZGV2ZWxvcGVyL2FhY2Q5MTVjLTNmMTktNzY4Ni05NmRmLWVlM2U1OWVhODdjYSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI4MC4zMS43Mi4xMDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.BkRZSsJMMZY5g0cPVjb0MtmJxeKc2AkRsw0KXvVN4Q6_UtV9rCbXa0PfOMoW2CQjjSINNnIWmRmGMgCNHw-k7w'  
    clan = request.form.get("clan")

    if clan is None:
        resultado = "resultado: Nombre inválido"
        return render_template('buscador2.html', clans=None, resultado=resultado)

    url = url_base + "clans?name=" + clan
    payload = {'Authorization': 'Bearer ' + key}
    r = requests.get(url, headers=payload)

    if r.status_code == 200:
        datos = r.json() 
        clans = datos["items"]
        resultado = None
        if clans:
            clan = clans[0]
        else:
            resultado = f'Jugador no encontrado. Prueba con otro código'
            return render_template("buscador2.html", resultado=resultado)
    else:
        resultado = "resultado al buscar: " + str(r.status_code)

    return render_template('buscador2.html', clans=clans, clan=clan, resultado=resultado)




@app.route('/buscador3', methods=['GET', 'POST'])
def buscador3():
    url_base = "https://api.clashroyale.com/v1/"
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFmN2U4ZTJiLTljMDgtNGNhNC05NzEwLWJiZDE4NmViNjNjYSIsImlhdCI6MTY4NTA0MDU1OCwic3ViIjoiZGV2ZWxvcGVyL2FhY2Q5MTVjLTNmMTktNzY4Ni05NmRmLWVlM2U1OWVhODdjYSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI4MC4zMS43Mi4xMDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.BkRZSsJMMZY5g0cPVjb0MtmJxeKc2AkRsw0KXvVN4Q6_UtV9rCbXa0PfOMoW2CQjjSINNnIWmRmGMgCNHw-k7w'
    payload = {'Authorization': 'Bearer ' + key}
    url = url_base + "globaltournaments"

    r = requests.get(url, headers=payload)
    if r.status_code == 200:
        data = r.json()
        globaltournaments = data.get("items")
        if globaltournaments:
            tournaments = [tournament.get("title") for tournament in globaltournaments]
        else:
            tournaments = None
    else:
        tournaments = None
        print("resultado en la búsqueda:", r.status_code)

    return render_template('buscador3.html', tournaments=tournaments)


@app.route('/jugadores', methods=['GET', 'POST'])
def jugadores():
    url_base = "https://api.clashroyale.com/v1/"
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFmN2U4ZTJiLTljMDgtNGNhNC05NzEwLWJiZDE4NmViNjNjYSIsImlhdCI6MTY4NTA0MDU1OCwic3ViIjoiZGV2ZWxvcGVyL2FhY2Q5MTVjLTNmMTktNzY4Ni05NmRmLWVlM2U1OWVhODdjYSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI4MC4zMS43Mi4xMDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.BkRZSsJMMZY5g0cPVjb0MtmJxeKc2AkRsw0KXvVN4Q6_UtV9rCbXa0PfOMoW2CQjjSINNnIWmRmGMgCNHw-k7w'
    payload = {'Authorization': 'Bearer ' + key}
    url = url_base + "locations/global/seasons/2022-01/rankings/players"

    r = requests.get(url, headers=payload)
    if r.status_code == 200:
        data = r.json()
        topjugador = data.get("items")
        if topjugador:
            jugadores = [jugador for jugador in topjugador]
        else:
            jugadores = None
    else:
        jugadores = None
        print("resultado en la búsqueda:", r.status_code)

    return render_template('jugadores.html', jugadores=jugadores)

@app.route('/clanes', methods=['GET', 'POST'])
def clanes():
    url_base = "https://api.clashroyale.com/v1/"
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFmN2U4ZTJiLTljMDgtNGNhNC05NzEwLWJiZDE4NmViNjNjYSIsImlhdCI6MTY4NTA0MDU1OCwic3ViIjoiZGV2ZWxvcGVyL2FhY2Q5MTVjLTNmMTktNzY4Ni05NmRmLWVlM2U1OWVhODdjYSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI4MC4zMS43Mi4xMDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.BkRZSsJMMZY5g0cPVjb0MtmJxeKc2AkRsw0KXvVN4Q6_UtV9rCbXa0PfOMoW2CQjjSINNnIWmRmGMgCNHw-k7w'
    payload = {'Authorization': 'Bearer ' + key}
    url = url_base + "locations/57000218/rankings/clans"

    r = requests.get(url, headers=payload)
    if r.status_code == 200:
        data = r.json()
        clanes = data.get("items")
        if clanes:
            clans = [clan for clan in clanes]
        else:
            clans = None
    else:
        clans = None
        print("resultado en la búsqueda:", r.status_code)

    return render_template('clanes.html', clans=clans)

@app.route('/torneos', methods=['GET', 'POST'])
def torneos():
    return render_template('torneos.html')

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
