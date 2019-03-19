ESC = '\033'
BLANK = ' '
TWENTYFIVE = '\u2591'
FIFTY = '\u2592'
SEVENTYFIVE = '\u2593'
FULL = '\u2588'
BEL = '\x07'

CursorUp = ESC + 'A'
CursorDown = ESC + 'B'
CursorRight = ESC + 'C'
CursorLeft = ESC + 'D'

SaveCursor = ESC + '7'
LoadCursor = ESC + '8'

InsertBlank = ESC + "[1@"
DeleteChar = ESC + "[1X"
InsertLine = ESC + "[1L"
DeleteLine = ESC + "[1M"

EndOfLine = CursorRight * 100
BeginOfLine = CursorLeft * 100

def SetWindowTitle(title):
    print(ESC + ']2;' + title + BEL)
