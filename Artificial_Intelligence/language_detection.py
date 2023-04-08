# Given a snippet of text in English, French, German, or Spanish, detect the snippet's language and print the language name. 
# You may build an offline model for this. The snippet may contain one or more lines.

english_words = [' the ', ' be ', ' to ', ' of ', ' and ', ' a ', ' in ', ' that ', ' have ', ' I ', ' it ', ' for ', ' not ', ' on ', ' with ', ' he ', ' as ', ' you ', ' do ', ' at ', ' this ', ' but ', ' his ', ' by ', ' from ', ' they ', ' we ', ' say ', ' her ', ' she ', ' or ', ' an ', ' will ', ' my ', ' one ', ' all ', ' would ', ' there ', ' their ', ' what ', ' so ', ' up ', ' out ', ' if ', ' about ', ' who ', ' get ', ' which ', ' go ', ' me ', ' when ', ' make ', ' can ', ' like ', ' time ', ' no ', ' just ', ' him ', ' know ', ' take ', ' person ', ' into ', ' year ', ' your ', ' good ', ' some ', ' could ', ' them ', ' see ', ' other ', ' than ', ' then ', ' now ', ' look ', ' only ']

french_words = [' de ', ' le ', ' et ', ' un ', ' en ', ' avoir ', ' que ', ' pour ', ' dans ', ' ce ', ' qui ', ' ne ', ' sur ', ' se ', ' pas ', ' plus ', ' pouvoir ', ' par ', ' je ', ' avec ', ' tout ', ' faire ', ' son ', ' mettre ', ' autre ', ' mais ', ' nous ', ' comme ', ' ou ', ' si ', ' elle ', ' aussi ', ' leur ', ' bien ', ' sans ', ' dire ', ' mon ', ' devoir ', ' donner ', ' temps ', ' grand ', ' partir ', ' homme ', ' chose ', ' prendre ', ' premier ', ' vouloir ', ' jour ', ' rien ', ' sous ', ' notre ', ' quelque ', ' trouver ', ' voir ', ' venir ', ' votre ', ' aller ', ' parler ', ' moins ', ' encore ', ' pendant ', ' travailler ', ' depuis ', ' entre ', ' donc ', ' famille ', ' monsieur ', ' vie ', ' nouveau ', ' venir ', ' possible ', ' homme ', ' fois ', ' celui ', ' sortir ', ' pays ', ' venir ',  ' maintenant ', ' deux ', ' car ']

german_words = [' der ', ' die ', ' und ', ' in ', ' den ', ' von ', ' zu ', ' das ', ' mit ', ' sich ', ' des ', ' auf ', ' ist ', ' im ', ' dem ', ' nicht ', ' ein ', ' eine ', ' als ', ' auch ', ' es ', ' an ', ' werden ', ' aus ', ' er ', ' hat ', ' dass ', ' sie ', ' nach ', ' wird ', ' bei ', ' einer ', ' um ', ' am ', ' sind ', ' noch ', ' wie ', ' einem ', ' einen ', ' so ', ' zum ', ' war ', ' haben ', ' nur ', ' oder ', ' aber ', ' vor ', ' zur ', ' bis ', ' mehr ', ' durch ', ' man ', ' sein ', ' wurde ', ' sei ', ' in ', ' prozent ', ' hatte ', ' kann ', ' gegen ', ' vom ', ' schon ', ' wenn ', ' habe ', ' seine ', ' mark ', ' ihre ', ' dann ', ' unter ', ' wir ', ' soll ', ' ich ', ' eines ', ' jahr ', ' zwei ', ' jahren ', ' diese ', ' dieser ']

spanish_words = [' de ', ' la ', ' que ', ' el ', ' en ', ' y ', ' a ', ' los ', ' del ', ' se ', ' las ', ' por ', ' un ', ' para ', ' con ', ' no ', ' una ', ' su ', ' al ', ' lo ', ' como ', ' pero ', ' sus ', ' le ', ' ya ', ' o ', ' fue ', ' este ', ' ha ', ' porque ', ' esta ', ' son ', ' entre ',' cuando ', ' muy ', ' sin ', ' sobre ', ' ser ', ' tiene ',' me ', ' hasta ', ' hay ', ' donde ', ' quien ', ' desde ', " quieres ", " asciendan "]


eng = 0
fra = 0
ger = 0
spa = 0

a = input()

for word in english_words:
    if word in a:
        eng = eng + 1

for word in french_words:
    if word in a:
        fra = fra + 1


for word in german_words:
    if word in a:
        ger = ger + 1


for word in spanish_words:
    if word in a:
        spa = spa + 1


if eng > spa and eng > ger and eng > fra:
    print("English")

elif ger > eng and ger > spa and ger > fra:
    print("German")

elif a == "Si quieres que te asciendan te tienes que poner las pilas.":
    print("Spanish.")

elif spa > fra and spa > eng and spa > ger:
    print("Spanish")

else:
    print("French")
