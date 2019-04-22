# OneMore

## Table of Contents

Mission        2

A word on &quot;Cheating&quot;        2

Functionality        3

Modes        3

_Fixed Mode_        3

_Flex Mode_        4

Sound        4

Gameplay        5

Getting Started        5

Save/Load Game        5

Player Menu        5

Adding Activities (Gaining Exp)        5

Checking Player Stats        6

Check My Exp        6

Check Nature Log        6

Interacting with Organisms        6

Attack        6

Flee        7

Befriend        7

Companion Attack        7

-        Ask your companion to attack on your behalf; this will bring the opponent&#39;s attention to your companion; if you&#39;re lucky enough to befriend a strong ally, this may help you gain experience faster, but be warned: _enemies will not drop items if driven off by your companion_!        7

Evolving Organisms        7

Exploration Menu        7

Explore a new Environment        7

Explore Your Current Environment        7

Organisms Menu        8

Set Companion        8

Examine Companion        8

Feed Companion        8

Rest Companion        8

Check Resting Organisms        8

View Bestiary        8

Breed        8

View Nursery        8

Settings Menu        8

Toggle Sound        8

Toggle Flex/Fixed        8



## Mission

OneMore seeks to help players produce greater productivity in their days by incentivizing them to do the things they care about with a classic, &quot;DnD-style&quot; RPG.

-
  - OneMore seeks to flip the &quot;Pokemon&quot; notion on its head by _first_ shuffling organisms into a more fantastical state and then gradually &quot;evolving&quot; them into an organism that exists in the world, today (without losing any of its cool game-powers!).
  - Ultimately, OneMore should marry the organizational, productivity-driving tools of yesteryear with the benefits of gamification, though it&#39;s worth nothing that the aim isn&#39;t to &quot;gamify&quot; productivity in the traditional sense but rather to treat productivity as fuel for a game.

## A word on &quot;Cheating&quot;

It&#39;s commonly asked, &quot;Can&#39;t I just cheat by giving myself more experience?&quot;

The _short_ answer:

- --yes.

The _more complete_ answer:

- --OneMore was designed for people who have an active interest in improving their motivation for tasks, both large and small, in day-to-day life.  In the same way that you can &quot;cheat&quot; while on a diet, exercising, or studying, so too can you manipulate the system in OneMore (although &quot;fixed&quot; mode offers some solutions for people concerned they&#39;ll be tempted to cheat).
- --That being said, just as with the examples mentioned above, the real-life rewards diminish greatly if you cheat.  Remember, there are many motivational tools in the world and many, many more classic RPGs, but there are far fewer programs that join the two!

## Functionality

Onemore uses a number of different tools to help you achieve your goals, including multiple modes, functions, and forms of gameplay.  Be sure to give these a look before you play.

##
## Modes

OneMore offers two basic modes: _Fixed_ and _Flex_.

## _Fixed Mode_

Fixed mode gives users the opportunity to work with a pre-loaded, pre-designated set of common goals (such as running, swimming, reading, etc) to get started fast!

&quot;_Fixed Mode_&quot; offers:

- --A pre-loaded set of goals for the user
- --An easier start to the game
- --The opportunity to focus on gameplay if you&#39;re interested in becoming more productive but aren&#39;t yet sure how to do it.
- --An additional buffer against &quot;cheating&quot;

## _Flex Mode_

&quot;Flex&quot; modes allows users to generate their own repository of activities with uniquely-assigned

- Activity Check
  - OneMore begins by prompting the user to offer up any given activity that he or she has done that day and, in Flex-Mode, to assign it any experience value.
  - If the user has completed the activity before, the activity is identified and the experience is awarded to the user.
  - Some activities may have &quot;once-a-day&quot; limitations or may prompt the user to indicate how many times the activity was performed (e.g. if you read, you may be asked how many pages, or if you run, you may be asked how many kilometers—this depends on whether you&#39;re running fixed mode or flex mode).
  - Experience Limitations:
    - Even in FlexMode, experience is fixed between 1 and 50 exp per instance.
    - Experience may only be available for a given activity once a day (e.g. &quot;go to work&quot;)

##
## Sound

Though entirely optional, OneMore offers sound support.  You&#39;ll be prompted to select &quot;on&quot; or &quot;off&quot; when initializing the game, and you can toggle the same throughout.

- --_Note:  Not all organisms will produce sound, but all organisms of a class share one sound in the current version._

## Gameplay

## Getting Started

OneMore is run through the bash command line.

_A note for users playing through remote access:_

- --_&quot;Pygame&quot; is used to produce game sound; an alternate (sound-free) version of the game is available for those who aren&#39;t able to load the module._

## Save/Load Game

- --OneMore uses the _pickle_ module for saving and loading, meaning that it will (attempt to) load any pickle file that you offer it.  All files are directed to a _Saves_ folder which is created if it doesn&#39;t already exist.
- --You can use the opening menu to choose either a _new game_ or to _load game_.

## Player Menu

## Adding Activities (Gaining Exp)

- --Central to the game, the addition of activities is far-and-away the best method of gaining exp.  You&#39;re able to accrue exp in four different categories:
  - Fitness
    - Chiefly affects _strength_ and _HP_ but may have other value in certain situations.
  - Intellect
    - Increases intellect stat; Speeds-up certain processes and makes others available to the user.
  - Naturalism
    - Increases the user&#39;s ability to successfully find dropped items/food and enhances the beneficial effects of organisms.
  - Happiness
    - Increases Luck which directly or indirectly affects most other stats and activities.

## Checking Player Stats

- --Allows you to quickly evaluate your current stats; can be useful in determining whether more exp should be gained before approaching a difficult area.

## Check My Exp

- --Makes visible the amount of current experience the user has in each category (100 exp in a category = +1 to its stat(s))

## Check Nature Log

- --All organisms seen are recorded in the nature log and remain there even if they&#39;re driven away, drive the player away, or are befriended/released.  This is the best way to determine how many unique organisms you&#39;ve encountered!

## Interacting with Organisms

## Attack

- --Use your _strength_ to deal damage to your opponent; note that while attacking, enemy attacks will be directed toward you.

## Flee

- --Use your _luck_ (competes with enemy _luck_) to try and escape.  Note that all organisms have this ability as well and those with a high _Skittishness_ stat may be inclined to attempt it more often.

## Befriend

- --Attempt to woo an organism to join your cause!  This is built largely around your _luck_ and _naturalism_ stats.  Any organism recruited will be eligible to become a companion and may use the &quot;attack companion&quot; feature, be bred, and be evolved.

## Companion Attack

- --Ask your companion to attack on your behalf; this will bring the opponent&#39;s attention to your companion; if you&#39;re lucky enough to befriend a strong ally, this may help you gain experience faster, but be warned: _enemies will not drop items if driven off by your companion_!

## Evolving Organisms

- --All organisms in the game are _real life organisms_ that have been shuffled and distorted from their true forms.  Leveling them past their evolution threshold (they gain experience while traveling as your _companion_) will produce a massive stat increase as well as a new, truer-to-reality moniker for your organism!  In its final form, your organism regains its true name, form, and significantly increased stats.

## Exploration Menu

## Explore a new Environment

- --Allows you to choose a new environment to explore and/or transition out of your existing environment.
  - _Note:  Environments are listed in order of difficulty._

## Explore Your Current Environment

- --If you return to the main menu while in an environment, you can re-enter it using this command without having to re-set your preference.

## Organisms Menu

## Set Companion

- --If any are available, you may choose any organism from the bestiary.
  - _Note that it may be easier to select the organism&#39;s_ **index** _than write out its entire name._

## Examine Companion

- --Check your companion&#39;s stats (useful for comparing potential companions with your current companion).

## Feed Companion

- --If you have anything to offer in your inventory, consider feeding it to your companion—this will raise at least one stat at least one point!

## Rest Companion

- --Allowing companions to rest takes them out of availability for at least one day, but per each day they spend resting, their stats will grow.  This is, in part, influenced by your _naturalism_ and _intellect_.

## Check Resting Organisms

- --Allows the user to check whether or not enough time has passed for the organism to return to the bestiary.

## View Bestiary

- --Produces a list of all organisms currently befriended.

## Breed

- --Allows the user to breed two organisms of the same type and opposite sex.
- --Certain circumstances may produce _hybrid vigor_ and increase the quality of the offspring&#39;s stats.
  - _Note: Offspring may not be evolved as they&#39;re hybridized forms of their parents._
  - _Note:  Only one mating may be performed at a time, and matings may take up to one full Earth day._

## View Nursery

- --Allows for the user to check whether or not the mating process is complete and the offspring are ready to join the other organisms in the bestiary.
  - _Note:  Only one pair of parents may occupy the nursery at a time._

## Settings Menu

## Toggle Sound

- --The user is given the choice to turn sound &quot;on&quot; or &quot;off&quot; mid-game.

## Toggle Flex/Fixed

- --The user can choose to return to either _fixed_ or _flex_ structure.
  - _Note:  Transitioning from flex-to-fixed will delete the user&#39;s personalized activity encyclopedia._
