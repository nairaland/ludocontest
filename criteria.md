- Nice opening page.
- Rules are provided and match the actual implementation.
- Freedom to setup all 4 colours as AI/Human/None intuitivelly.
- Allow bot v bot v bot v bot games.
- Board Layout is accurate.
- Board looks like an actual Ludo board.
- Pieces are well arranged inside their boxes.
- Pieces look really nice.
- The paths the pieces move are accurate.
- Dice are well animated.
- Dice throws for the user are automated to eliminate tedium.
- Double dice are set as the default or exclusively used.
- Piece animation when moving is fun (jump per tile)
- Good sound effects for the moves
- Good animation/glow highlighting legal moves.
- Music that can be turned off or that stops when the window loses focus.
- The AI moves pieces for players you when there is only one legal move.
- Implementing safe zones correctly. A common ommision.
- Bonus for putting useful labels on the board e.g. "naija ludo, AI, Nairaland"
- Indicate whose turn it is in an intuitive way.
- Highlight the pieces that can be moved.
- Getting the center of the Ludo game board right - 4 triangles making the box, correctly coloured..
- Rotating the board after each turn is neat.
- A wooden table or board is nice.


03
- Nice opening page. 1
    The game features a professional start screen modal with a "CHAMPIONSHIP EDITION" title, a list of features, and a pulsating "PLAY GAME" button, creating a strong first impression.
- Rules are provided and match the actual implementation. 0
    While the opening screen lists features, there are no explicit "How to Play" instructions or detailed rules provided within the game interface to guide new players.
- Freedom to setup all 4 colours as AI/Human/None intuitivelly. 0
    Configuration is limited to preset game modes (e.g., "1 Player vs 3 CPU", "2 Players"), lacking granular control to individually set each color to Human, CPU, or None.
- Allow bot v bot v bot v bot games. 0
    There is no option in the game selection menu (settings modal) to configure a fully automated game with 4 CPU players.
- Board Layout is accurate. 1
    The board grid size allows for the standard path length, and the track coordinates correctly map to a traditional Ludo layout.
- Board looks like an actual Ludo board. 1
    The procedural texture generation effectively recreates the look of a physical Ludo board with appropriate colored lanes, home columns, and spacing.
- Pieces are well arranged inside their boxes. 0
    Pieces spawn in a tight 2x2 cluster that ignores the four white circular slots painted on the board, resulting in a misaligned and crowded appearance within the base.
- Pieces look really nice. 1
    The use of `MeshPhysicalMaterial` with clearcoat and emissive properties gives the pieces a premium, "candy-like" polished appearance.
- The paths the pieces move are accurate. 1
    Piece movement logic correctly follows the main track and properly handles entering the home straights towards the center.
- Dice are well animated. 1
    The dice rolling uses 3D physics-like animations (rotation and vertical jumping) provided by Tween software, looking smooth and realistic.
- Dice throws for the user are automated to eliminate tedium. 0
    The user is required to manually click the "ROLL" button every turn; there is no auto-roll feature for human players to speed up the flow.
- Double dice are set as the default or exclusively used. 1
    The game logic hardcodes rolling 2 dice for every turn, satisfying the double dice criterion.
- Piece animation when moving is fun (jump per tile) 1
    The pieces perform a hopping animation for each step they take, which is visually engaging and fun.
- Good sound effects for the moves 1
    The game uses the Web Audio API to generate synthesized sound effects for stepping, rolling, landing, and winning, which functions well.
- Good animation/glow highlighting legal moves. 1
    Valid pieces are clearly identified by an emissive glow and a continuous "jumping" loop animation.
- Music that can be turned off or that stops when the window loses focus. 0
    No background music is implemented in the game, only sound effects.
- The AI moves pieces for players you when there is only one legal move. 0
    The game does not auto-play forced moves for human players; it waits for user interaction even if only one piece can move.
- Implementing safe zones correctly. A common ommision. 0
    The move resolution logic captures any opponent on the same tile without checking for "safe" star tiles, omitting this core rule.
- Bonus for putting useful labels on the board e.g. "naija ludo, AI, Nairaland" 0
    The board is texture-generated with geometric shapes but does not include any specific text labels or branding on the board surface.
- Indicate whose turn it is in an intuitive way. 1
    The UI highlights the active player badge, displays a text status, and the camera smoothy rotates to the active player's perspective.
- Highlight the pieces that can be moved. 1
    As noted, valid pieces are highlighted with animation and glow, making it obvious which pieces can be selected.
- Getting the center of the Ludo game board right - 4 triangles making the box, correctly coloured.. 1
    The board generation logic explicitly draws the four colored triangles meeting at the center, matching the correct visual design.
- Rotating the board after each turn is neat. 1
    The "Dynamic Camera Juice" feature rotates the view to the current player's perspective after every turn.
- A wooden table or board is nice. 1
    The board mesh includes a thick wooden-colored border base, giving it the appearance of a physical wooden game board.
Points: 15/24
