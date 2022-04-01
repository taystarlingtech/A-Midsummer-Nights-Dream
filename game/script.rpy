﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define eil = Character("Eileen", callback = name_callback, cb_name = "eileen")
define e = Character("Eileen",color="#FF6347", callback = name_callback, cb_name = "eileen")#This is a placeholder character.

define Sus = Character("Theseus",color="#c8ffc8")#Duke of Athens
define Hip = Character("Hippolyta")#Queen of the Amazons
define Egg = Character("Egeus") #father of Hermia
define Her = Character("Hermia") #daughter of Egeus, in love with Lysander
define Lys = Character("Lysander")#in love with Hermia
define Dem = Character("Demetrius")#suitor to Hermia
define Hel = Character("Helena")#in love with Demetrius
define Phi = Character("Philostrate")#Master of the Revels
define Qui = Character("Peter Quince")#a carpenter
define Nic = Character("Nick Bottom")#a weaver
define Fra = Character("Francis Flute")#a bellows-mender
define Tom = Character("Tom Snout")#a tinker
define Snu = Character("Snug")#a joiner
define Rob = Character("Robin Starveling")#a tailor
define Obe = Character("Oberon")#King of the Fairies
define Tit = Character("Titania")#ueen of the Fairies
define Puck = Character("Robin Puck Goodfellow")#Robin "Puck" Goodfellow—a mischievous sprite with magical powers
define p = Character("Peaseblossom")#Peaseblossom, Cobweb, Moth and Mustardseed—fairy servants to Titania
define c = Character("Cobweb")
define mo = Character("Moth")
define mu = Character("Mustardseed")
define ling = Character("Indian changeling")#a ward of Titania
define Ned = Character("Nedar")#father of Helena

"""
Act 1, Scene 1: Athens. The palace of THESEUS.
Act 1, Scene 2: Athens. QUINCE'S house.
Act 2, Scene 1: A wood near Athens.
Act 2, Scene 2: Another part of the wood.
Act 3, Scene 1: The wood. TITANIA lying asleep.
Act 3, Scene 2: Another part of the wood.
Act 4, Scene 1: The same. LYSANDER, DEMETRIUS, HELENA, and HERMIA
Act 4, Scene 2: Athens. QUINCE'S house.
Act 5, Scene 1: Athens. The palace of THESEUS.
"""
image bg parkwatercolor = im.Scale("parkwatercolor.jpg",1920, 1080)
image bg stairs = im.Scale("autumnoldstairs.jpg",1920, 1080)
image bg tunnel = im.Scale("falltunnelwatercolorfoto.jpg", 1920, 1080)

# image eileen happy = At('eileen_happy', sprite_highlight('eileen'))
image smile01 = At("Sprite F PinkH Professional Smile01.png", sprite_highlight('eileen'))
image smile02 = "Sprite F PinkH Professional Smile02.png" 
image sad02 = "Sprite F PinkH Professional Sad02.png"

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/04. Carnival.mp3" fadeout 1.0 fadein 1.0
    scene bg tunnel
    show smile01:
        zoom 0.5
    show smile02 at right:
        zoom 0.5
    
    #--------SCENE I. Athens. The palace of THESEUS.--------

    #Characters in scene I:  
    #THESEUS, x
    #HIPPOLYTA, x
    #PHILOSTRATE, 
    #EGEUS,x

    #HERMIA, x
    #LYSANDER, x
    #DEMETRIUS, 
    #HELENA  x

    # --------ACT I Scene I--------

    #Enter THESEUS, HIPPOLYTA, PHILOSTRATE, and Attendants
    Sus "Now, fair Hippolyta, our nuptial hour
    Draws on apace; four happy days bring in
    Another moon: but, O, methinks, how slow
    This old moon wanes! she lingers my desires,
    Like to a step-dame or a dowager Long withering out a young man revenue."

    Hip "Four days will quickly steep themselves in night;
    Four nights will quickly dream away the time;
    And then the moon, like to a silver bow
    New-bent in heaven, shall behold the night Of our solemnities."

    Sus "Go, Philostrate, Stir up the Athenian youth to merriments;
    Awake the pert and nimble spirit of mirth;
    Turn melancholy forth to funerals;
    The pale companion is not for our pomp."

    #Exit PHILOSTRATE

    Sus "Hippolyta, I woo'd thee with my sword,
    And won thy love, doing thee injuries;
    But I will wed thee in another key,
    With pomp, with triumph and with revelling."

    #Enter EGEUS, HERMIA, LYSANDER, and DEMETRIUS

    Egg "Happy be Theseus, our renowned duke!"

    Sus "Thanks, good Egeus: what's the news with thee?"

    Egg "Full of vexation come I, with complaint
    Against my child, my daughter Hermia.
    Stand forth, Demetrius. My noble lord,
    This man hath my consent to marry her."

    Egg "Stand forth, Lysander: and my gracious duke,
    This man hath bewitch'd the bosom of my child;
    Thou, thou, Lysander, thou hast given her rhymes,
    And interchanged love-tokens with my child:"

    Egg "Thou hast by moonlight at her window sung,
    With feigning voice verses of feigning love,
    And stolen the impression of her fantasy
    With bracelets of thy hair, rings, gawds, conceits,"

    Egg "Knacks, trifles, nosegays, sweetmeats, messengers
    Of strong prevailment in unharden'd youth:
    With cunning hast thou filch'd my daughter's heart,
    Turn'd her obedience, which is due to me,"

    Egg "To stubborn harshness: and, my gracious duke,
    Be it so she; will not here before your grace
    Consent to marry with Demetrius,
    I beg the ancient privilege of Athens,"

    Egg "As she is mine, I may dispose of her:
    Which shall be either to this gentleman
    Or to her death, according to our law
    Immediately provided in that case."

    Sus "What say you, Hermia? be advised fair maid:
    To you your father should be as a god;
    One that composed your beauties, yea,"

    Sus "and one To whom you are but as a form in wax
    By him imprinted and within his power
    To leave the figure or disfigure it.
    Demetrius is a worthy gentleman."

    Her "So is Lysander."

    Sus "In himself he is;
    But in this kind, wanting your father's voice,
    The other must be held the worthier."

    Her "I would my father look'd but with my eyes."

    Sus "Rather your eyes must with his judgment look."

    Her "I do entreat your grace to pardon me.
    I know not by what power I am made bold,
    Nor how it may concern my modesty,"

    Her "In such a presence here to plead my thoughts;
    But I beseech your grace that I may know
    The worst that may befall me in this case,
    If I refuse to wed Demetrius."

    Sus "Either to die the death or to abjure
    For ever the society of men.
    Therefore, fair Hermia, question your desires;
    Know of your youth, examine well your blood,
    Whether, if you yield not to your father's choice,"

    Sus "You can endure the livery of a nun,
    For aye to be in shady cloister mew'd,
    To live a barren sister all your life,
    Chanting faint hymns to the cold fruitless moon."

    Sus "Thrice-blessed they that master so their blood,
    To undergo such maiden pilgrimage;
    But earthlier happy is the rose distill'd,
    Than that which withering on the virgin thorn
    Grows, lives and dies in single blessedness."

    Her "So will I grow, so live, so die, my lord,
    Ere I will my virgin patent up
    Unto his lordship, whose unwished yoke
    My soul consents not to give sovereignty."

    Sus "Take time to pause; and, by the next new moon--
    The sealing-day betwixt my love and me,
    For everlasting bond of fellowship--
    Upon that day either prepare to die"

    Sus "For disobedience to your father's will,
    Or else to wed Demetrius, as he would;
    Or on Diana's altar to protest
    For aye austerity and single life."

    Dem "Relent, sweet Hermia: and, Lysander, yield
    Thy crazed title to my certain right."

    Lys "You have her father's love, Demetrius;
    Let me have Hermia's: do you marry him."

    Egg "Scornful Lysander! true, he hath my love,
    And what is mine my love shall render him.
    And she is mine, and all my right of her
    I do estate unto Demetrius."

    Lys "I am, my lord, as well derived as he,
    As well possess'd; my love is more than his;
    My fortunes every way as fairly rank'd,
    If not with vantage, as Demetrius';"

    Lys "And, which is more than all these boasts can be,
    I am beloved of beauteous Hermia:
    Why should not I then prosecute my right?
    Demetrius, I'll avouch it to his head,"

    Lys "Made love to Nedar's daughter, Helena,
    And won her soul; and she, sweet lady, dotes,
    Devoutly dotes, dotes in idolatry,
    Upon this spotted and inconstant man."

    Sus "I must confess that I have heard so much,
    And with Demetrius thought to have spoke thereof;
    But, being over-full of self-affairs,
    My mind did lose it. But, Demetrius, come;"

    Sus "And come, Egeus; you shall go with me,
    I have some private schooling for you both.
    For you, fair Hermia, look you arm yourself
    To fit your fancies to your father's will;"

    Sus "Or else the law of Athens yields you up--
    Which by no means we may extenuate--
    To death, or to a vow of single life.
    Come, my Hippolyta: what cheer, my love?"

    Sus "Demetrius and Egeus, go along:
    I must employ you in some business
    Against our nuptial and confer with you
    Of something nearly that concerns yourselves."

    Egg "With duty and desire we follow you."

    #Exeunt all but LYSANDER and HERMIA

    scene bg stairs with dissolve
    play music "audio/03. Sad Sad Kiddie.mp3" fadeout 1.0 fadein 1.0
    show sad02:
        zoom .5

    Lys "How now, my love! why is your cheek so pale?
    How chance the roses there do fade so fast?"

    Her "Belike for want of rain, which I could well
    Beteem them from the tempest of my eyes."

    Lys "Ay me! for aught that I could ever read,
    Could ever hear by tale or history,
    The course of true love never did run smooth;
    But, either it was different in blood,--"

    Her "O cross! too high to be enthrall'd to low."

    Lys "Or else misgraffed in respect of years,--"

    Her "O spite! too old to be engaged to young."

    Lys "Or else it stood upon the choice of friends,--"

    Her "O hell! to choose love by another's eyes."

    Lys "Or, if there were a sympathy in choice,
    War, death, or sickness did lay siege to it,
    Making it momentany as a sound,
    Swift as a shadow, short as any dream;"

    Lys "Brief as the lightning in the collied night,
    That, in a spleen, unfolds both heaven and earth,
    And ere a man hath power to say 'Behold!'
    The jaws of darkness do devour it up:
    So quick bright things come to confusion."

    Her "If then true lovers have been ever cross'd,
    It stands as an edict in destiny:
    Then let us teach our trial patience,
    Because it is a customary cross,
    As due to love as thoughts and dreams and sighs,
    Wishes and tears, poor fancy's followers."

    Lys "A good persuasion: therefore, hear me, Hermia.
    I have a widow aunt, a dowager
    Of great revenue, and she hath no child:
    From Athens is her house remote seven leagues;"

    Lys "And she respects me as her only son.
    There, gentle Hermia, may I marry thee;
    And to that place the sharp Athenian law
    Cannot pursue us. If thou lovest me then,"

    Lys "Steal forth thy father's house to-morrow night;
    And in the wood, a league without the town,
    Where I did meet thee once with Helena,
    To do observance to a morn of May,
    There will I stay for thee."

    Her "My good Lysander!
    I swear to thee, by Cupid's strongest bow,
    By his best arrow with the golden head,
    By the simplicity of Venus' doves,"

    Her "By that which knitteth souls and prospers loves,
    And by that fire which burn'd the Carthage queen,
    When the false Troyan under sail was seen,
    By all the vows that ever men have broke,"

    Her "In number more than ever women spoke,
    In that same place thou hast appointed me,
    To-morrow truly will I meet with thee."

    Lys "Keep promise, love. Look, here comes Helena."

    #Enter Helena

    Her "God speed fair Helena! whither away?"

    Hel "Call you me fair? that fair again unsay.
    Demetrius loves your fair: O happy fair!
    Your eyes are lode-stars; and your tongue's sweet air
    More tuneable than lark to shepherd's ear,"

    Hel "When wheat is green, when hawthorn buds appear.
    Sickness is catching: O, were favour so,
    Yours would I catch, fair Hermia, ere I go;
    My ear should catch your voice, my eye your eye,"

    Hel "My tongue should catch your tongue's sweet melody.
    Were the world mine, Demetrius being bated,
    The rest I'd give to be to you translated.
    O, teach me how you look, and with what art
    You sway the motion of Demetrius' heart."

    Her "I frown upon him, yet he loves me still."

    Hel "O that your frowns would teach my smiles such skill!"

    Her "I give him curses, yet he gives me love."

    Hel "O that my prayers could such affection move!"

    Her "The more I hate, the more he follows me."

    Hel "The more I love, the more he hateth me."

    Her "His folly, Helena, is no fault of mine."

    Hel "None, but your beauty: would that fault were mine!"

    Her "Take comfort: he no more shall see my face;
        Lysander and myself will fly this place.
        Before the time I did Lysander see,
        Seem'd Athens as a paradise to me:
        O, then, what graces in my love do dwell,
        That he hath turn'd a heaven unto a hell!"

    Lys "Helen, to you our minds we will unfold:
        To-morrow night, when Phoebe doth behold
        Her silver visage in the watery glass,
        Decking with liquid pearl the bladed grass,
        A time that lovers' flights doth still conceal,
        Through Athens' gates have we devised to steal."

    Her "And in the wood, where often you and I
        Upon faint primrose-beds were wont to lie,
        Emptying our bosoms of their counsel sweet,
        There my Lysander and myself shall meet;
        And thence from Athens turn away our eyes,"

    Her "To seek new friends and stranger companies.
        Farewell, sweet playfellow: pray thou for us;
        And good luck grant thee thy Demetrius!
        Keep word, Lysander: we must starve our sight
        From lovers' food till morrow deep midnight."

    Lys "I will, my Hermia."

    #Exit HERMIA

    Lys "Helena, adieu: As you on him, Demetrius dote on you!"

    #Exit

    Hel "How happy some o'er other some can be!
        Through Athens I am thought as fair as she.
        But what of that? Demetrius thinks not so;
        He will not know what all but he do know:"

    Hel "And as he errs, doting on Hermia's eyes,
        So I, admiring of his qualities:
        Things base and vile, folding no quantity,
        Love can transpose to form and dignity:"

    Hel "Love looks not with the eyes, but with the mind;
        And therefore is wing'd Cupid painted blind:
        Nor hath Love's mind of any judgement taste;
        Wings and no eyes figure unheedy haste:"

    Hel "And therefore is Love said to be a child,
        Because in choice he is so oft beguiled.
        As waggish boys in game themselves forswear,
        So the boy Love is perjured every where:"

    Hel "For ere Demetrius look'd on Hermia's eyne,
        He hail'd down oaths that he was only mine;
        And when this hail some heat from Hermia felt,
        So he dissolved, and showers of oaths did melt."

    Hel "I will go tell him of fair Hermia's flight:
        Then to the wood will he to-morrow night
        Pursue her; and for this intelligence 
        If I have thanks, it is a dear expense:
        But herein mean I to enrich my pain,
        To have his sight thither and back again."

    #--------END ACT I, Scene I--------
    show smile02:
        zoom 0.5
    e "Hoory No Bugs!"

    # This ends the game.
    return
