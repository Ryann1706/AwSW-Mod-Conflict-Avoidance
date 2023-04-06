
# Adine's good ending: 
# Freefall, Adine Romantic Ending and Adine Shopping

init python:
    ryann_mca_adine_good_endings = 0
    ryann_mca_anna_good_endings = 0


label ryann_mca_adine_good_ending:

if renpy.has_label("cm_freefall1"):
    $ ryann_mca_adine_good_endings += 1
if renpy.has_label("adine_romance_end"):
    $ ryann_mca_adine_good_endings += 1
if renpy.has_label("adine_shopping"):
    $ ryann_mca_adine_good_endings += 1
if renpy.has_label("adine_flight_of_love_start"):
    $ ryann_mca_adine_good_endings += 1

if ryann_mca_adine_good_endings > 1:
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (3.0)
    play sound "fx/system3.wav"
    s "Multiple Adine good ending mods detected. Jump to which one?"
    menu:
        "Freefall" if renpy.has_label("cm_freefall1"):
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            scene black with dissolveslow
            $ renpy.pause (3.0)
            jump cm_common_freefall

        "Adine Romantic Ending" if renpy.has_label("adine_romance_end"):
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            scene black with dissolveslow
            $ renpy.pause (3.0)
            jump thn_common_adine

        "Adine Shopping" if renpy.has_label("adine_shopping"):
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            scene black with dissolveslow
            $ renpy.pause (3.0)
            jump adine_shopping

        "Adine's Flight Of Love" if renpy.has_label("adine_flight_of_love_start"):
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            scene black with dissolveslow
            $ renpy.pause (3.0)
            jump adine_flight_of_love_start

else:
    pass

jump ryann_mca_adine_good_ending_return
    

#==================================================================================================================================

# Anna good ending:
# w/ 4 dates and impressed, and 3 Adine dates and impressed, Not So Tragic Hero, and Adine and Anna beter ending

# I'm removing the requirement for Adine to be impressed for NSTH, because it's much more convenient to just be able to skip the 3 dates


label ryann_mca_anna_good_ending:

if renpy.has_label("eck_annashappyend"):
    $ ryann_mca_anna_good_endings += 1
if renpy.has_label("wyv_betterannaending"):
    $ ryann_mca_anna_good_endings += 1
if renpy.has_label("ryann_atttw_start"):
    $ ryann_mca_anna_good_endings += 1

if ryann_mca_anna_good_endings > 1:
    scene black with dissolveslow
    $ renpy.pause (3.0)
    s "Multiple Anna good ending mods detected. Jump to which one?"
    menu:
        "Not-so-Tragic Hero" if renpy.has_label("eck_annashappyend"):
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            $ renpy.pause (3.0)
            $ adinestatus = "good"
            jump eck_common_anna

        "Anna and Adine ending" if renpy.has_label("wyv_betterannaending"):
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            $ renpy.pause (3.0)
            jump wyv_betterannaending

        "A Trip to the Woods" if renpy.has_label("ryann_atttw_start"):
            stop music fadeout 3.0
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            $ renpy.pause (3.0)
            jump ryann_atttw_mca_start

elif renpy.has_label("eck_annashappyend"):
    $ adinestatus = "good"
    jump eck_common_anna

elif renpy.has_label("wyv_betterannaending"):
    jump wyv_betterannaending

elif renpy.has_label("ryann_atttw_start"):
    jump ryann_atttw_mca_start

else:
    pass

jump ryann_mca_anna_good_ending_return


#==================================================================================================================================

# Anna 4 romance:
# Bangok, Lwed Anna scene

label ryann_mca_anna4_romance:

if renpy.has_label("bangok_anon_anna4_start") and renpy.has_label("a4romanceL"):
    An face "Alright, alright. So fussy."
    $ renpy.pause (1.0)
    play sound "fx/system3.wav"
    s "Multiple Anna romance mods detected. Jump to which one, or skip to the end?"
    menu:
        "BangOk":
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            $ renpy.pause(1.0)
            jump bangok_anon_anna4_start

        "Lewd Anna scene":
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            $ renpy.pause(1.0)
            jump ryann_mca_anna4_lewdannamerge

        "Skip to the end.":
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            scene black with dissolveslow
            $ renpy.pause (3.0)
            $ mp.annaromance = True
            $ mp.save()
            $ annastatus = "good"
            $ annascenesfinished = 4
            stop music fadeout 2.0
            $ renpy.pause (0.5)
            if chapter4unplayed == False:
                jump chapter4chars
            elif chapter3unplayed == False:
                jump chapter3chars
            elif chapter2unplayed == False:
                jump chapter2chars
            else:
                jump chapter1chars

elif renpy.has_label("bangok_anon_anna4_start"):
    An face "Alright, alright. So fussy."
    jump bangok_anon_anna4_skipmenu

else:
    jump ryann_mca_anna4_romance_return
