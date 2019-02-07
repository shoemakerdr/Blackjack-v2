# Blackjack-v2
Text-based blackjack game written in Python

Main game will run from Game.py

### Comments
Here's my general comments:
1. If you want to make this more "pythonic", you should change the folder structure around a bit. Something like:
    ```
    + blackjack
      + src
        + blackjack
          + __init__.py
          + blackjack.py
          + card.py
          + deck.py
          + game.py
          + hand.py
          + player.py
      + test
        + blackjack
          + __init__.py
          + test_blackjack.py
          + test_card.py
          + test_deck.py
          + test_game.py
          + test_hand.py
          + test_player.py
      + README.md
      + play_blackjack  # maybe some script that calls the game
      ```
2. Having tests is important. It helps to prevent/catch bugs, so you'll definitely want to add tests here.
3. There's a lot of classes/methods that do a ton of work. These should be broken up into multiple classes/methods, following
   the Single Responsibility Principle (from S.O.L.I.D. Principles).
4. You may want to look into the S.O.L.I.D. Principles to help guide you as you write applications. They're very helpful. I
   highly recommend looking for any talks or books by Sandy Metz. She's an amazing mind when it comes to writing/designing 
   software.

