init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/sfx/type2.mp3", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

python:
    import os
default persistent.game_played = False

define p = Character("{gradient=#e0a803-#ffee93}Protagonist{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define k3k = Character("{gradient=#c6e2e9-#aec6cf}Kong{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define k1m = Character("{gradient=#94b0da-#b7d7e8}Mami{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")
define k2p = Character("{gradient=#ff6961-#ffb6b9}Papi{/gradient}", callback=callback, ctc="ctc_animation", ctc_position="fixed")

label easteregg:
    scene black
    # Imong kabet
    #HAHAH DON'T READ MUNA

    k3k "Pre,{w=0.3} wait lang ah, dito ka muna sa loob"
    p "'Yoko,{w=0.3} andyan papa mo eh."
    k3k "Dee, ako lang tapos si mama.{p}Dito ka muna sa loob, hintayin mo na q"
    p "Baka Mamaya-{w=0.3}{nw}"
    k3k "Dee, wala si papa dyan.{w=0.3} Magka-away sila ni mama.{w=0.3} Maupo ka muna dyan."
    p "Bilisan mo ah."

    scene room with dissolve
    #play audio door opens

    k2p "*Ehem* Hi Linda, Mahal.{w=0.4} Flowers para sayo"

    #play audio door closes

    k1m "Ano yan?{w=0.3} 'di ko kailangan niyan.{w=0.2} Umalis ka dito."
    k2p "Eto naman e. {w=0.3} Mahal, sorry na. Kalimutan na natin yung nangyare, patawarin mo na ako-{w=0.5}{nw}"
    k1m "ahe eh ano- ganun-ganun lang yon?{p}Gusto mo isang sorry lang, okay na lahat?"
    k2p "Oo nga-{w=0.2} kaya nga sorry na eh."
    k1m "Ay nako tigilan mo ko!"
    k2p "Sige naa{w=0.1} *kiss*{w=0.1} patawarin mo na ako{w=0.1} *kiss*" #HAHA
    k1m "Tigilan mo ako- bitawan mo ako!"
    k2p "Mahal- sorry naa"
    k1m "Bitawan mo ako!"
    k2p "Ano ba?"
    k1m "Tama na- sabing tama na e!"

    # play audio slap
    # play audio vase shatter
    play audio "audio/sfx/vine boom.mp3"

    k2p "Aray!"
    k1m "Ayan, nabasag na.{w=0.3} 'di ka kase magtigil!"
    k2p "Ano nanamang problema mo?{w=0.3} nanghihingi na nga ng tawag diba?"
    k1m "Oh- baket? Ganun-ganun lang yon?{p}Pag tapos mo mangbabae?{w=0.3} Oh pwes! Meron narin akong iba!" # HAHAHAHAH
    k1m "Ayon oh! Yung barkada ng anak mo!{w=0.4}{nw}"
    play audio "audio/sfx/vine boom.mp3"
    k2p "Ano!?"
    k2p "Sino!?"
    k2p "Eto!?"

    p "Di po! 'd-di po-!{w=-0.2}{nw}"
    play audio "audio/sfx/vine boom.mp3"

    k1m "Oo!{w=0.4} Mula nung umalis ka, nangliligaw na sakin yan dito-{w=0.4}{nw}"
    k2p "Aba tarantado ka ah!"
    k2p "Halika rito! Bubugbugin kita!"
    play audio "audio/sfx/vine boom.mp3"

    p "Ay d-di po! Kilala ko lang po d-"
    play audio "audio/sfx/vine boom.mp3"

    k1m "Hay ang sarap.{w=0.3} Para akong na promote nang na promote- naranasan ko lahat ng posisyon sakanya" #xDDDD
    play audio "audio/sfx/vine boom.mp3"

    k2p "TOTOO BA YON!? HINTAYIN MO ako DYAN"
    p "Hindi po!!---{w=0.2}{nw}"
    play audio "audio/sfx/vine boom.mp3"
    k2p "Hintayin mo ako dyan, KUKUNIN KO BARIL KO."
    play audio "audio/sfx/vine boom.mp3"

    k1m "Kukunin mo baril mo? Ay sorry- huli ka na, naputukan niya na ako kagabi"

    k2p "MGA TARANTADO KAYO- HALIKA NGA KAYO DITO"
    k2p "MGA PUTANGINA NIYO, KELAN NIYO PA AKO TINATARANTADO?"
    play audio "audio/sfx/vine boom.mp3"

    k1m "Edi mula nung nagloko ka, diba baby?"
    play audio "audio/sfx/vine boom.mp3"

    p "????????"

    k1m "Ang sabi niya pa, para akong chicharon. Ang ingay ko daw pag ako kinakain."
    play audio "audio/sfx/vine boom.mp3"

    k2p "MGA PU-TANG INA NYO-"
    play audio "audio/sfx/vine boom.mp3"
    k2p "AOUBGASUGBASOGASGASgASGAIGBi"
    play audio ["audio/sfx/vine boom.mp3", "audio/sfx/vine boom.mp3","audio/sfx/vine boom.mp3","audio/sfx/vine boom.mp3","audio/sfx/vine boom.mp3",]


