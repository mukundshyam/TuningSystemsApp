from flask import Blueprint, render_template, url_for, request, redirect
from .models import Sample, Megalovania, WetHands, Pigstep, FurElise, Otherside
from . import data
from sqlalchemy import select
import math
import random
from random import choice

main = Blueprint("main", __name__)

def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

#K-value chosen based on the fact that K for new chess players = 40, after 30 games K = 20. So I wanted something that could
#gave everyone equal-ish powers over the change in elo. Arbitrary!
def EloRating(Ra, Rb, d):
    # To calculate the Winning
    # Probability of Player B
    Pb = Probability(Ra, Rb)
    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(Rb, Ra)
    # Case -1 When Player A wins
    # Updating the Elo Ratings
    if (d == 1):
        up1 = Ra + 27 * (1 - Pa)
        up2 = Rb + 27 * (0 - Pb)
    # Case -2 When Player B wins
    # Updating the Elo Ratings
    else:
        up1 = Ra + 27 * (0 - Pa)
        up2 = Rb + 27 * (1 - Pb)
    return up1, up2

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/instructions")
def instructions():
    return render_template("instructions.html")

@main.route("/info")
def info():
    return render_template("info.html")

@main.route("/info", methods=['post'])
def infoPost():
    SampleInitials = request.form.get('initial')
    SampleAge = request.form.get('age')
    
    newSample = Sample(initials=SampleInitials, age=SampleAge)
    data.session.add(newSample)
    data.session.commit()

    return redirect(url_for('main.compare11'))

@main.route("/compare11")
def compare11():
    global id1
    global id2
    global Tab1
    global Tab2
    id1 = random.randint(1, 4)
    Tab1 = Megalovania.query.filter_by(id=id1).first()
    link1 = Tab1.link
    id2 = random.randint(1, 4)
    while id2 == id1:
        id2 = random.randint(1, 4) 
    Tab2 = Megalovania.query.filter_by(id=id2).first()
    link2 = Tab2.link
    return render_template("compare11.html", linkA=link1, linkB=link2)

@main.route("/compare11a", methods=['post'])
def compare11a_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 1)
    data.session.query(Megalovania).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(Megalovania).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare12'))

@main.route("/compare11b", methods=['post'])
def compare11b_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 0)
    data.session.query(Megalovania).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(Megalovania).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare12'))

@main.route("/compare12")
def compare12():
    global id3
    global id4
    global Tab3
    global Tab4
    id3 = random.randint(1, 4)
    while id3 == id1 or id3 == id2:
        id3 = random.randint(1, 4)
    Tab3 = Megalovania.query.filter_by(id=id3).first()
    link1 = Tab3.link
    id4 = random.randint(1, 4)
    while id4 == id1 or id4 == id2 or id4 == id3:
        id4 = random.randint(1, 4)
    Tab4 = Megalovania.query.filter_by(id=id4).first()
    link2 = Tab4.link
    return render_template("compare12.html", linkA=link1, linkB=link2)

@main.route("/compare12a", methods=['post'])
def compare12a_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 1)
    data.session.query(Megalovania).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(Megalovania).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare21'))

@main.route("/compare12b", methods=['post'])
def compare12b_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 0)
    data.session.query(Megalovania).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(Megalovania).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare21'))

@main.route("/compare21")
def compare21():
    global id1
    global id2
    global Tab1
    global Tab2
    id1 = random.randint(1, 4)
    Tab1 = WetHands.query.filter_by(id=id1).first()
    link1 = Tab1.link
    id2 = random.randint(1, 4)
    while id2 == id1:
        id2 = random.randint(1, 4) 
    Tab2 = WetHands.query.filter_by(id=id2).first()
    link2 = Tab2.link
    return render_template("compare21.html", linkA=link1, linkB=link2)

@main.route("/compare21a", methods=['post'])
def compare21a_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 1)
    data.session.query(WetHands).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(WetHands).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare22'))

@main.route("/compare21b", methods=['post'])
def compare21b_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 0)
    data.session.query(WetHands).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(WetHands).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare22'))

@main.route("/compare22")
def compare22():
    global id3
    global id4
    global Tab3
    global Tab4
    id3 = random.randint(1, 4)
    while id3 == id1 or id3 == id2:
        id3 = random.randint(1, 4)
    Tab3 = WetHands.query.filter_by(id=id3).first()
    link1 = Tab3.link
    id4 = random.randint(1, 4)
    while id4 == id1 or id4 == id2 or id4 == id3:
        id4 = random.randint(1, 4)
    Tab4 = WetHands.query.filter_by(id=id4).first()
    link2 = Tab4.link
    return render_template("compare22.html", linkA=link1, linkB=link2)

@main.route("/compare22a", methods=['post'])
def compare22a_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 1)
    data.session.query(WetHands).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(WetHands).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare31'))

@main.route("/compare22b", methods=['post'])
def compare22b_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 0)
    data.session.query(WetHands).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(WetHands).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare31'))

@main.route("/compare31")
def compare31():
    global id1
    global id2
    global Tab1
    global Tab2
    id1 = random.randint(1, 4)
    Tab1 = Pigstep.query.filter_by(id=id1).first()
    link1 = Tab1.link
    id2 = random.randint(1, 4)
    while id2 == id1:
        id2 = random.randint(1, 4) 
    Tab2 = Pigstep.query.filter_by(id=id2).first()
    link2 = Tab2.link
    return render_template("compare31.html", linkA=link1, linkB=link2)

@main.route("/compare31a", methods=['post'])
def compare31a_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 0)
    data.session.query(Pigstep).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(Pigstep).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare32'))

@main.route("/compare31b", methods=['post'])
def compare31b_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 0)
    data.session.query(Pigstep).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(Pigstep).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()
    return redirect(url_for('main.compare32'))

@main.route("/compare32")
def compare32():
    global id3
    global id4
    global Tab3
    global Tab4
    id3 = random.randint(1, 4)
    while id3 == id1 or id3 == id2:
        id3 = random.randint(1, 4)
    Tab3 = Pigstep.query.filter_by(id=id3).first()
    link1 = Tab3.link
    id4 = random.randint(1, 4)
    while id4 == id1 or id4 == id2 or id4 == id3:
        id4 = random.randint(1, 4)
    Tab4 = Pigstep.query.filter_by(id=id4).first()
    link2 = Tab4.link
    return render_template("compare32.html", linkA=link1, linkB=link2)

@main.route("/compare32a", methods=['post'])
def compare32a_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 1)
    data.session.query(Pigstep).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(Pigstep).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare41'))

@main.route("/compare32b", methods=['post'])
def compare32b_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 0)
    data.session.query(Pigstep).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(Pigstep).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare41'))

@main.route("/compare41")
def compare41():
    global id1
    global id2
    global Tab1
    global Tab2
    id1 = random.randint(1, 4)
    Tab1 = FurElise.query.filter_by(id=id1).first()
    link1 = Tab1.link
    id2 = random.randint(1, 4)
    while id2 == id1:
        id2 = random.randint(1, 4) 
    Tab2 = FurElise.query.filter_by(id=id2).first()
    link2 = Tab2.link
    return render_template("compare41.html", linkA=link1, linkB=link2)

@main.route("/compare41a", methods=['post'])
def compare41a_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 1)
    data.session.query(FurElise).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(FurElise).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare42'))

@main.route("/compare41b", methods=['post'])
def compare41b_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 0)
    data.session.query(FurElise).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(FurElise).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare42'))

@main.route("/compare42")
def compare42():
    global id3
    global id4
    global Tab3
    global Tab4
    id3 = random.randint(1, 4)
    while id3 == id1 or id3 == id2:
        id3 = random.randint(1, 4)
    Tab3 = FurElise.query.filter_by(id=id3).first()
    link1 = Tab3.link
    id4 = random.randint(1, 4)
    while id4 == id1 or id4 == id2 or id4 == id3:
        id4 = random.randint(1, 4)
    Tab4 = FurElise.query.filter_by(id=id4).first()
    link2 = Tab4.link
    return render_template("compare42.html", linkA=link1, linkB=link2)

@main.route("/compare42a", methods=['post'])
def compare42a_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 1)
    data.session.query(FurElise).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(FurElise).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare51'))

@main.route("/compare42b", methods=['post'])
def compare42b_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 0)
    data.session.query(FurElise).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(FurElise).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare51'))

@main.route("/compare51")
def compare51():
    global id1
    global id2
    global Tab1
    global Tab2
    id1 = random.randint(1, 4)
    Tab1 = Otherside.query.filter_by(id=id1).first()
    link1 = Tab1.link
    id2 = random.randint(1, 4)
    while id2 == id1:
        id2 = random.randint(1, 4) 
    Tab2 = Otherside.query.filter_by(id=id2).first()
    link2 = Tab2.link
    return render_template("compare51.html", linkA=link1, linkB=link2)

@main.route("/compare51a", methods=['post'])
def compare51a_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 1)
    data.session.query(Otherside).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(Otherside).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare52'))

@main.route("/compare51b", methods=['post'])
def compare51b_post():
    elo1 = Tab1.elo
    elo2 = Tab2.elo
    val = EloRating(elo1, elo2, 0)
    data.session.query(Otherside).filter_by(id=id1).update({"elo":val[0]})
    data.session.query(Otherside).filter_by(id=id2).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.compare52'))

@main.route("/compare52")
def compare52():
    global id3
    global id4
    global Tab3
    global Tab4
    id3 = random.randint(1, 4)
    while id3 == id1 or id3 == id2:
        id3 = random.randint(1, 4)
    Tab3 = Otherside.query.filter_by(id=id3).first()
    link1 = Tab3.link
    id4 = random.randint(1, 4)
    while id4 == id1 or id4 == id2 or id4 == id3:
        id4 = random.randint(1, 4)
    Tab4 = Otherside.query.filter_by(id=id4).first()
    link2 = Tab4.link
    return render_template("compare52.html", linkA=link1, linkB=link2)

@main.route("/compare52a", methods=['post'])
def compare52a_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 1)
    data.session.query(Otherside).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(Otherside).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.thanks'))

@main.route("/compare52b", methods=['post'])
def compare52b_post():
    elo3 = Tab3.elo
    elo4 = Tab4.elo
    val = EloRating(elo3, elo4, 0)
    data.session.query(Otherside).filter_by(id=id3).update({"elo":val[0]})
    data.session.query(Otherside).filter_by(id=id4).update({"elo":val[1]})
    data.session.commit()

    return redirect(url_for('main.thanks'))

@main.route("/thanks")
def thanks():
    return render_template("thanks.html")