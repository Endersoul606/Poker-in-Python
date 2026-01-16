"""
    colourTheory v1.2 by Endersoul__606
"""

def print_colour(text, colour="default"):
    """A way to use colours in print statements"""
    fg_map={"black":30,"red":31,"green":32,"yellow":33,"blue":34,"magenta":35,"cyan":36,"white":37}
    if colour not in fg_map:print(text);return
    esc,reset=f"\033[{fg_map[colour]}m","\033[0m"
    print(f"{esc}{text}{reset}")

def input_colour(prompt, colour="default"):
    """A way to use colours in input statements"""
    fg_map={"black":30,"red":31,"green":32,"yellow":33,"blue":34,"magenta":35,"cyan":36,"white":37}
    if colour not in fg_map:print(prompt);return
    esc,reset = f"\033[{fg_map[colour]}m","\033[0m"
    a = input(f"{esc}{prompt}{reset}")
    return a

def help(choise):
    """Welcome to the colourTheory library 
    
    What do you need help on?
     1) Hex Codes
     2) Custom Functions
     3) Audio
     4) Colour Changing Window
     5) Keypress Programs"""
    if choise == 1:
        print_colour("Section - Hex Codes", "black")
        print_colour("In the colourTheory library, we have set hex codes for main colours.", "black")
        print_colour("To access them you refer to the name of your imported library, then the colour.", "black")
        print_colour("For example colourTheory.cyan or cT.cyan depending on how you imported this library", "black")
    elif choise == 2:
        print_colour("Section - Functions", "black")
        print_colour("In the colourTheory library, we have many useful functions", "black")
        print_colour("[print_colour] prints in text in one of 8 custom colours", "black")
        print_colour("[input_colour] gets an input from the user using a custom prompt in one of 8 custom colours", "black")
        print_colour("[brighten_colour] brightens a colour by (amount) amount", "black")
        print_colour("[darkern_colour] darkerns a colour by (amount) amount", "black")
        print_colour("[random_colour] gives a random colour", "black")
        print_colour("[indexes] contains all set colours and outputs a given index from it", "black")
        print_colour("[get_index] returns the amount of colours available", "black")
        print_colour("[help] gives help with any problems with this library")
    elif choise == 3:
        print_colour("Section - Audio", "black")
        print_colour("Colour Theory also gives Easy access to using Audio in your python tracks", "black")
        print_colour("We have made a class for Audio files that supports .mp3, .wav and .ogg files", "black")
        print_colour("There are also built in functions that your audio files will have", "black")
        print_colour("[.play()] plays the track and you choose if you want to loop it", "black")
        print_colour("[.pause()] pauses the track and lets you resume later", "black")
        print_colour("[.resume()] resumes the track in the position where it was paused", "black")
        print_colour("[.stop()] stops the track completely", "black")
    elif choise == 4:
        print_colour("Section - Colour Changing Windows", "black")
        print_colour("Colour Theory has an inbuilt class for colour-changing windows")
        print_colour("You can edit width and height with set parameters")
        print_colour("You can also draw ontop with commands in string form in the objects list")
    elif choise == 5:
        print_colour("Section - Keypress Programs")
        print_colour("We have a program which does a set action on a password")

def brighten_colour(colour:str, amount=1, logChanges=False):
    """Brightens a colour by (amount) amount"""
    if (amount>15) or (amount<1): return
    hex_digits,outputList,cannot_be=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"],[],[];colour.replace("#", "")
    for a in range(amount+1):cannot_be.append(hex_digits[-a])
    cannot_be.pop(0)
    if logChanges:print_colour(cannot_be)
    for letter in colour:
        for index in range(len(hex_digits)):
            if letter == hex_digits[index]:
                if hex_digits[index] in cannot_be:outputList.append("F")
                else:index += amount;outputList.append(hex_digits[index])
    new_colour=f"#{outputList[0]}{outputList[1]}{outputList[2]}{outputList[3]}{outputList[4]}{outputList[5]}"
    if logChanges:print_colour(new_colour, "magenta")
    return new_colour

def darkern_colour(colour:str, amount=1, logChanges=False):
    """Darkern a colour by (amount) amount"""
    if (amount>15) or (amount<1):return
    hex_digits,outputList,cannot_be=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"],[],[];colour.replace("#", "")
    for a in range(amount+1):cannot_be.append(hex_digits[a])
    if logChanges:print_colour(cannot_be)
    for letter in colour:
        for index in range(len(hex_digits)):
            if letter == hex_digits[index]:
                if hex_digits[index] in cannot_be:outputList.append("0")
                else:index -= amount;outputList.append(hex_digits[index])
    new_colour=f"#{outputList[0]}{outputList[1]}{outputList[2]}{outputList[3]}{outputList[4]}{outputList[5]}"
    if logChanges:print_colour(new_colour, "magenta")
    return new_colour


def random_colour():
    """Returns a truly random colour"""
    import random
    hex_digits,ol=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"],[]
    for i in range(6):random.shuffle(hex_digits);ol.append(hex_digits[random.randint(2, 9)])
    output = f"#{ol[0]}{ol[1]}{ol[2]}{ol[3]}{ol[4]}{ol[5]}"
    return output

def indexes(index):
    """A list containing all colourTheory colours in colour order"""
    global l
    return l[index]

def len_indexes():
    """Returns the amount of colours available in the colour list"""
    global l
    return len(l)


# Colour Hex Codes
white =          "#FFFFFF"
rose_pink =      "#FFDBFF"
light_pink =     "#EEB2EE"
pink =           "#F576F5"
magenta =        "#DF2BDF"
coral =          "#BD527F"
dark_coral =     "#934666"
dark_red =       "#9A1F29"
falu =           "#801818"
red =            "#DF2828"
burntorange =    "#E05A17"
pholox =         "#FF8D8D"
brown =          "#A78456"
orange =         "#E6AA26"
sun_orange =     "#E0C217"
yellow =         "#E4E117"
eburnean =       "#FFFF00"
lime =           "#B1FF29"
flour_green =    "#3DFF0D"
light_green =    "#4CBF2F"
green =          "#3E9B27"
dark_green =     "#2C6A1C"
teal =           "#008080"
smaragdine =     "#4A9976"
turquoise =      "#24D3BC"
cyan =           "#41D9F0"
light_blue =     "#41BBF0"
blue =           "#1B82D5"
dark_blue =      "#154AA6"
atrovirens =     "#0000FF"
navy =           "#0E2D63"
indigo =         "#410082"
purple =         "#651591"
maroon =         "#330949"
dark_gray =      "#303030"
black =          "#000000"
gray =           "#585858"
olive =          "#808000"
sarcoline =      "#FFBFBF"
warm_white =     "#FFDDDD"
light_gray =     "#AAAAAA"
watchet =        "#8FBABC"
frost =          "#D3FAFF"
cold_white =     "#F1FEFF"
off_white =      "#DDDDDD"

l = [white,brighten_colour(rose_pink),rose_pink,light_pink,pink,magenta,coral,dark_coral,dark_red,red,burntorange,pholox,
     brown,orange,sun_orange,yellow,eburnean,lime,flour_green,light_green,green,dark_green,teal,smaragdine,turquoise,cyan,light_blue,
     blue,darkern_colour(blue),darkern_colour(blue,2),dark_blue,atrovirens,navy,indigo,maroon,dark_gray,black,gray,olive,
     sarcoline,warm_white,light_gray,cold_white,off_white]

class ColourChangingWindow:
    """A Window which Colour Changes:
    Width) Width of Window
    Height) Height of Window
    Objects) Objects to draw ontop of the window"""
    def __init__(self, width:int = 300, height:int = 300, objects:list = []):
        import tkinter as tk
        self.to_draw = objects
        self.window = tk.Tk()
        self.window.title("LED Square")
        self.width,self.height = width, height
        self.index = 0
        self.FirstTime = True
        self.colourChange()

    def colourChange(self):
        import tkinter as tk
        self.index += 1
        if self.index > len_indexes()-1:
            self.index = 0
        colour = indexes(self.index)
        if self.FirstTime:
            self.canvas = tk.Canvas(self.window, height=self.height, width=self.width, bg=colour)
            self.canvas.pack()
            self.FirstTime = False
        self.canvas.create_rectangle(self.width, self.height, 0, 0, fill=colour)
        self.draw()
        self.canvas.after(70, self.colourChange)
    
    def draw(self):
        for object in self.to_draw:
            try: eval(object)
            except: raise SyntaxError(f"Invalid Command: Could not complete [{object}]")
        return
    
    def run(self):
        self.window.mainloop()
    

class KeypressProgram:
    def __init__(self, password:list = ["`", "`", "`"], action:str = "subprocess.run(['shutdown', '-s', '-f', '-t', '0'])"):
        """A Program which does an action on a set keypress"""
        import keyboard, subprocess
        try:
            self.password = password
        except:
            self.password = ["`", "`", "`"]

        self.attempt_password = []
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if len(self.attempt_password) == len(self.password):
                    self.attempt_password.pop(0)

                self.attempt_password.append(event.name)
                        
                if self.attempt_password == self.password:
                    try:
                        eval(action)
                    except:
                        subprocess.run(['shutdown', '-s', '-f', '-t', '0'])

            
class AudioPlayer:
    def __init__(self, file_path: str):
        import pygame
        from pygame import mixer
        from os import path
        pygame.init()
        mixer.init()

        if not path.isfile(file_path):
            raise FileNotFoundError(f"Audio file not found: [{file_path}]")

        if not file_path.lower().endswith(('.mp3', '.wav', '.ogg')):
            raise ValueError("Unsupported file format. Use .mp3, .wav, or .ogg")

        self.file_path = file_path
        self.is_paused = False

        try:
            self.sound = pygame.mixer.Sound(self.file_path)
        except pygame.error as e:
            raise RuntimeError(f"Failed to load audio: {e}")

        self.channel = pygame.mixer.find_channel()
        if self.channel is None:
            self.channel = pygame.mixer.Channel(0)

    def play(self, loops: int = 0):
        """Play the audio on this instance's channel."""
        self.channel.play(self.sound, loops=loops)
        self.is_paused = False
        return f"Playing: {self.file_path}"

    def pause(self):
        """Pause this instance's channel."""
        if not self.is_paused:
            self.channel.pause()
            self.is_paused = True
            return "Audio Paused"

    def resume(self):
        """Resume this instance's channel."""
        if self.is_paused:
            self.channel.unpause()
            self.is_paused = False
            return "Audio Resumed"

    def stop(self):
        """Stop this instance's channel."""
        self.channel.stop()
        self.is_paused = False
        return "Audio stopped."


if __name__ == "__main__":
    window = ColourChangingWindow(300, 300, objects=[])
    window.run()

else:
    print_colour("\nYou are using the colourTheory library. Learn more by typing the function help()", "black")