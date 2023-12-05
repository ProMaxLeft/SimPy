from PyQt6.QtGui import QPixmap, QIcon 
atlas = QPixmap("minesweeper_sprites.png")
OPEN_0 = QIcon(atlas.copy(0, 0, 32, 32))
CLOSED = QIcon(atlas.copy(32, 64, 32, 32))
BOOM = QIcon(atlas.copy(64, 64, 32, 32))
ICON_SIZE = OPEN_0.availableSizes()[0]
