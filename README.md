# Purple
This repo contains the code to emulate and determine real time statistics during a game of purple.
## How to Play
There is one dealer and one player, however both positions rotate throughout gameplay. The action is on the player to successfully play a minimum of three additional cards to the run before passing the run to the next player. 

During a player's turn they may call any attribute of a card or series of cards in the deck as long as the odds are 50/50 or less. The play is always on the last card that was correctly played. If a player guesses wrong, they must drink the number of cards in the run, including the additional wrongly guessed cards. If a player guesses right, they continue guessing until they guessed a minimum of three cards correctly, at which point they may pass if they choose. 

When the play passes to the dealer's position, it is the dealer's turn to play and the dealer position rotates opposite player rotation. This continues until casual levels are achieved.

### Legal Moves
 - Purple: Two cards are drawn that are either (red, black), or (black, red)
 - Red: One card is drawn that is red
 - Black: One card is drawn that is black
 - Higher: One card is drawn that is higher than the previous card
 - Lower: One card is drawn that is lower than the previous card
 - Rainbow: Three cards are drawn that are either (red, black, red) or (black, red, black)
 - Push: One card is drawn that is the same rank as the previous card
 - 