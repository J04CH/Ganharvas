#!/usr/bin/env python3

import pygame
import threading
import os

def FirstPygameWindow():
    pygame.init()
    window = pygame.display.set_mode((200, 200))
    pygame.display.set_caption("Gandharvas")

    window.fill([255, 255, 255])

    #Instance of Button
    button1 = ButtonPygame(40, 50, 125, 44, 0, "Make A Song")
    button2 = ButtonPygame(38, 110, 130, 44, 1, "Reuse A Song")

    buttons = [button1, button2]

    running = True

    #Main Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            for button in buttons:
                button.handle_event(event, window)

        for button in buttons:
            button.draw(window)

            pygame.display.update()

def Refill(window):
    window.fill([255, 255, 255])

    #Draw First Five Lines
    pygame.draw.line(window, [0, 0, 0], (80, 77.5), (810, 77.5), 4)
    pygame.draw.line(window, [0, 0, 0], (90, 112.5), (810, 112.5), 4)
    pygame.draw.line(window, [0, 0, 0], (78, 147.5), (810, 147.5), 4)
    pygame.draw.line(window, [0, 0, 0], (95, 182.5), (810, 182.5), 4)
    pygame.draw.line(window, [0, 0, 0], (80, 217.5), (810, 217.5), 4)

    #Draw Second Five Lines
    pygame.draw.line(window, [0, 0, 0], (80, 357.5), (810, 357.5), 4)
    pygame.draw.line(window, [0, 0, 0], (80, 392.5), (810, 392.5), 4)
    pygame.draw.line(window, [0, 0, 0], (80, 427.5), (810, 427.5), 4)
    pygame.draw.line(window, [0, 0, 0], (80, 462.5), (810, 462.5), 4)
    pygame.draw.line(window, [0, 0, 0], (80, 497.5), (810, 497.5), 4)

    #Draw Third Five Lines
    pygame.draw.line(window, [0, 0, 0], (80, 637.5), (810, 637.5), 4)
    pygame.draw.line(window, [0, 0, 0], (80, 672.5), (810, 672.5), 4)
    pygame.draw.line(window, [0, 0, 0], (80, 707.5), (810, 707.5), 4)
    pygame.draw.line(window, [0, 0, 0], (80, 742.5), (810, 742.5), 4)
    pygame.draw.line(window, [0, 0, 0], (80, 777.5), (810, 777.5), 4)

    CDS = pygame.image.load("player/resources/img/cle-de-sol.png")

    #Put Image Onto Screen
    window.blit(CDS, (0, 75))

def PlaceTheNotes(window, beginning, ending, note = ""):
    global list_note

    if note == "Au" or note == "Al" or note == "B" or \
        note == "Cu" or note == "Cl" or note == "Du" or \
        note == "Dl" or note == "Eu" or note == "El" or \
        note == "Fu" or note == "Fl" or note == "Gu" or note == "Gl":
        list_note.append(note)

    else:
        for one_note in note.split():
            list_note.append(one_note)

    Refill(window)

    list_range_x = [100, 180, 260, 340, 420, 500, 580, 660, 740]

    #Load images
    note_img_high = pygame.image.load("player/resources/img/note-high.png")
    note_img_low = pygame.image.load("player/resources/img/note-low.png")

    for note in list_note:
        if note != "Au" and note != "Al" and note != "B" and \
        note != "Cu" and note != "Cl" and note != "Du" and \
        note != "Dl" and note != "Eu" and note != "El" and \
        note != "Fu" and note != "Fl" and note != "Gu" and note != "Gl":
            list_note.remove(note)

    RealList = list_note[beginning:ending]

    global times

    for i in range(len(list_note)):
        if len(list_note) > 26*i + i:
            times = i+1

    indices_Au = [i for i, x in enumerate(RealList) if x == "Au"]
    list_Au = [0, 280, 560]
    index_Au = 0

    for count in indices_Au:
        count += 1

        if count > 18:
            count = count - 18
            index_Au = 2

        if count == 18:
            count = 0
            index_Au = 2

        if count > 9 :
            count = count - 9
            index_Au = 1

        if count == 9:
            count = 0
            index_Au = 1

        if count < 9:
            for note in RealList:
                if note == "Au":
                    window.blit(note_img_high, (list_range_x[count], list_Au[index_Au]))

    indices_Al = [i for i, x in enumerate(RealList) if x == "Al"]
    list_Al = [45, 325, 605]
    index_Al = 0

    for count in indices_Al:
        count += 1

        if count > 18:
            count = count - 18
            index_Al = 2

        if count == 18:
            count = 0
            index_Al = 2

        if count > 9:
            count = count - 9
            index_Al = 1

        if count == 9:
            count = 0
            index_Al = 1

        if count < 9:
            for note in RealList:
                if note == "Al":
                    window.blit(note_img_low, (list_range_x[count], list_Al[index_Al]))

    indices_B = [i for i, x in enumerate(RealList) if x == "B"]
    list_B = [115, 395, 675]
    index_B = 0
    note_B = 0

    for count in indices_B:
        count += 1

        if count > 18:
            count = count - 18
            index_B = 2

        if count == 18:
            count = 0
            index_B = 2

        if count > 9:
            count = count - 9
            index_B = 1

        if count == 9:
            count = 0
            index_B = 1

            if note == "B":
                window.blit(note_img_high, (100, list_B[index_B]))

        if count < 9:
            for note in RealList:
                if note == "B":
                    window.blit(note_img_high, (list_range_x[count], list_B[index_B]))

    indices_Cu = [i for i, x in enumerate(RealList) if x == "Cu"]
    list_Cu = [97, 377, 657]
    index_Cu = 0

    for count in indices_Cu:
        count += 1

        if count > 18:
            count = count - 18
            index_Cu = 2

        if count == 18:
            count = 0
            index_Cu = 2

        if count > 9:
            count = count - 9
            index_Cu = 1

        if count == 9:
            count = 0
            index_Cu = 1

        if count < 9:
            for note in RealList:
                if note == "Cu":
                    window.blit(note_img_high, (list_range_x[count], list_Cu[index_Cu]))

    indices_Cl = [i for i, x in enumerate(RealList) if x == "Cl"]
    list_Cl = [140, 420, 700]
    index_Cl = 0

    for count in indices_Cl:
        count += 1

        if count > 18:
            count = count - 18
            index_Cl = 2

        if count == 18:
            count = 0
            index_Cl = 2

        if count > 9:
            count = count - 9
            index_Cl = 1

        if count == 9:
            count = 0
            index_Cl = 1

        if count < 9:
            for note in RealList:
                if note == "Cl":
                    window.blit(note_img_low, (list_range_x[count], list_Cl[index_Cl]))

    indices_Du = [i for i, x in enumerate(RealList) if x == "Du"]
    list_Du = [80, 360, 640]
    index_Du = 0

    for count in indices_Du:
        count += 1

        if count > 18:
            count = count - 18
            index_Du = 2

        if count == 18:
            count = 0
            index_Du = 2

        if count > 9:
            count = count - 9
            index_Du = 1

        if count == 9:
            count = 0
            index_Du = 1

        if count < 9:
            for note in RealList:
                if note == "Du":
                    window.blit(note_img_high, (list_range_x[count], list_Du[index_Du]))

    indices_Dl = [i for i, x in enumerate(RealList) if x == "Dl"]
    list_Dl = [115, 395, 675]
    index_Dl = 0

    for count in indices_Dl:
        count += 1

        if count > 18:
            count = count - 18
            index_Dl = 2

        if count == 18:
            count = 0
            index_Dl = 2

        if count > 9:
            count = count - 9
            index_Dl = 1

        if count == 9:
            count = 0
            index_Dl = 1

        if count < 9:
            for note in RealList:
                if note == "Dl":
                    window.blit(note_img_low, (list_range_x[count], list_Dl[index_Dl]))

    indices_Eu = [i for i, x in enumerate(RealList) if x == "Eu"]
    list_Eu = [62, 342, 622]
    index_Eu = 0

    for count in indices_Eu:
        count += 1

        if count > 18:
            count = count - 18
            index_Eu = 2

        if count == 18:
            count = 0
            index_Eu = 2

        if count > 9:
            count = count - 9
            index_Eu = 1

        if count == 9:
            count = 0
            index_Eu = 1

        if count < 9:
            for note in RealList:
                if note == "Eu":
                    window.blit(note_img_high, (list_range_x[count], list_Eu[index_Eu]))

    indices_El = [i for i, x in enumerate(RealList) if x == "El"]
    list_El = [97, 377, 657]
    index_El = 0

    for count in indices_El:
        count += 1

        if count > 18:
            count = count - 18
            index_El = 2

        if count == 18:
            count = 0
            index_El = 2

        if count > 9:
            count = count - 9
            index_El = 1

        if count == 9:
            count = 0
            index_El = 1

        if count < 9:
            for note in RealList:
                if note == "El":
                    window.blit(note_img_low, (list_range_x[count], list_El[index_El]))

    indices_Fu = [i for i, x in enumerate(RealList) if x == "Fu"]
    list_Fu = [47, 327, 607]
    index_Fu = 0

    for count in indices_Fu:
        count += 1

        if count > 18:
            count = count - 18
            index_Fu = 2

        if count == 18:
            count = 0
            index_Fu = 2

        if count > 9:
            count = count - 9
            index_Fu = 1

        if count == 9:
            count = 0
            index_Fu = 1

        if count < 9:
            for note in RealList:
                if note == "Fu":
                    window.blit(note_img_low, (list_range_x[count], list_Fu[index_Fu]))

    indices_Fl = [i for i, x in enumerate(RealList) if x == "Fl"]
    list_Fl = [80, 360, 640]
    index_Fl = 0

    for count in indices_Fl:
        count += 1

        if count > 18:
            count = count - 18
            index_Fl = 2

        if count == 18:
            count = 0
            index_Fl = 2

        if count > 9:
            count = count - 9
            index_Fl = 1

        if count == 9:
            count = 0
            index_Fl = 1

        if count < 9:
            for note in RealList:
                if note == "Fl":
                    window.blit(note_img_low, (list_range_x[count], list_Fl[index_Fl]))

    indices_Gu = [i for i, x in enumerate(RealList) if x == "Gu"]
    list_Gu = [27, 307, 587]
    index_Gu = 0

    for count in indices_Gu:
        count += 1

        if count > 18:
            count = count - 18
            index_Gu = 2

        if count == 18:
            count = 0
            index_Gu = 2

        if count > 9:
            count = count - 9
            index_Gu = 1

        if count == 9:
            count = 0
            index_Gu = 1

        if count < 9:
            for note in RealList:
                if note == "Gu":
                    window.blit(note_img_high, (list_range_x[count], list_Gu[index_Gu]))

    indices_Gl = [i for i, x in enumerate(RealList) if x == "Gl"]
    list_Gl = [65, 345, 625]
    index_Gl = 0

    for count in indices_Gl:
        count += 1

        if count > 18:
            count = count - 18
            index_Gl = 2

        if count == 18:
            count = 0
            index_Gl = 2

        if count > 9:
            count = count - 9
            index_Gl = 1

        if count == 9:
            count = 0
            index_Gl = 1

        if count < 9:
            for note in RealList:
                if note == "Gl":
                    window.blit(note_img_low, (list_range_x[count], list_Gl[index_Gl]))

def PlayTheNotes():
    global list_note
    global CountPlayTN, done
    CountPlayTN, done = 0, False

    pygame.mixer.init()

    for note, index in zip(list_note, range(len(list_note))):
        if note == "Au":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/A_high.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Al":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/A_low.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "B":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/B.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Cu":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/C_high.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Cl":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/C_low.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Du":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/D_high.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Dl":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/D_low.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Eu":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/E_high.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "El":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/E_low.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Fu":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/F_high.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Fl":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/F_low.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Gu":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/G_high.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if note == "Gl":
            CountPlayTN += 1
            pygame.mixer.music.load("player/resources/snd/G_low.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                pygame.time.wait(250)
                continue

        if index == len(list_note)-1:
            done = True

def WriteToFile():
    global list_note

    if len(list_note) > 0:
        FileIndex = 0

        pathtofolder = "player/resources/txt"

        if not os.path.exists(pathtofolder):
            os.makedirs(pathtofolder)

        while True:
            FileIndex += 1
            exists = os.path.isfile("player/resources/txt/File {0}".format(FileIndex))

            if not exists:
                f = open("player/resources/txt/File {0}".format(FileIndex), "w+")
                break

        global times

        for n in range(times):
            for i in range(3):
                if i == 0:
                    f.write("{0}:\n".format(n))
                    for note in list_note[27*n:27*n+8]:
                        f.write("{0} ".format(note))
                    if 27*n < len(list_note) or 27*n+8 < len(list_note) or 27*n+17 < len(list_note):
                        f.write("\n")

                if i == 1:
                    for note in list_note[27*n+8:27*n+17]:
                        f.write("{0} ".format(note))
                    if 27*n+8 < len(list_note) or 27*n+17 < len(list_note):
                        f.write("\n")

                if i == 2:
                    for note in list_note[27*n+17:27*n+26]:
                        f.write("{0} ".format(note))
                    if 27*n+17 < len(list_note):
                        f.write("\n\n")

def ReadTheFile(window, FileName):
    global numb, ReadOccured
    
    ReadOccured = True

    pathtofolder = "player/resources/txt"

    if not os.path.exists(pathtofolder):
        print("The Folder Does Not Exist!")

    exists = os.path.isfile("player/resources/txt/{0}".format(FileName))

    if not exists:
        print("The File Does Not Exist!")

    if exists:
        with open("player/resources/txt/{0}".format(FileName), "r") as f:
            for line in f:
                lineFinal = line.replace(":", "")
                lineFinal = lineFinal.replace("\n", "")

                if lineFinal.isdigit():
                    numb = int(lineFinal)

                PlaceTheNotes(window, 26*numb, 26 + 26*numb, line)

class VarInitializer: #Gets called at @ decoration
    global list_note, tab, RealList
    list_note, tab, RealList = [], [], []
    global count, times, CountPlayTN, FileIndexRTF, numb
    count, times, CountPlayTN, FileIndexRTF, numb = 0, 1, 0, 0, 0
    global done, ReadOccured, PTNOccured
    done, ReadOccured, PTNOccured = False, False, False

    def __init__(self, aClass): #On @ decoration
        self.aClass = aClass
    def __call__(self, *args): #On instance creation
        self.wrapped = self.aClass(*args)
        return self
    def __getattr__(self, name): #Gets called when using Main method
        return getattr(self.wrapped, name)

@VarInitializer
class SecondPygameWindow:
    def __init__(self, FileName=""):
        pygame.init()
        self.window = pygame.display.set_mode((900, 840))
        pygame.display.set_caption("Gandharvas")

        self.white = pygame.image.load("player/resources/img/white-square.jpg")

        Refill(self.window)

        #Instance of InputBox
        input_box1 = InputBoxPygame(852, 795, 47, 44, 0)
        self.input_boxes = [input_box1]

        #Instance of Button
        button1 = ButtonPygame(828, 125, 72, 44, 3, "WRITE")
        button2 = ButtonPygame(840, 405, 60, 44, 2, "PLAY")
        button3 = ButtonPygame(840, 685, 60, 44, 4, "READ")
        self.buttons = [button1, button2, button3]

        self.running = True

        if FileName != "":
            ReadTF = threading.Thread(target=ReadTheFile, args=(self.window, FileName))
            ReadTF.daemon = True
            ReadTF.start()

        if len(list_note) == 1133: #26, 53, 80, 1133
            PlaceTheNotes(self.window, 1107, 1133) #[0, 26], [27, 53], [54, 80], [1107, 1133]

    def Main(self):
        global times
        global count
        global tab
        global list_note

        j = 0

        #Main Loop
        while self.running:
            for i in range(times):
                if i < times:
                    if count == i and times == i + 1 and times < 11:
                        count += 1
                        tab.append(TabsPygame(0, 35*i, 30, 35, "{0}".format(i), i))

                    elif count == i and times == i + 1 and times <= 24:
                        count += 1
                        tab.append(TabsPygame(0, 35*i, 41, 35, "{0}".format(i), i))

                    elif count == i and times == i + 1 and 24 < times < 43: #times < 43 = button 41 (button i)
                        count += 1
                        tab.append(TabsPygame(859, 35*j, 41, 35, "{0}".format(i), i))
                        j += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                for box in self.input_boxes:
                    box.handle_event(event, self.window)

                for button in self.buttons:
                    button.handle_event(event, self.window)

                for tabs, option in zip(tab, range(len(tab))):
                    tabs.handle_event(event, self.window, option)

            self.window.blit(self.white, (853, 795))

            for box in self.input_boxes:
                box.draw(self.window)

            for button in self.buttons:
                button.draw(self.window)

            for tabs in tab:
                tabs.draw(self.window)

            for i in range(times):
                if len(tab) > i:
                    if i == 0 or i == 1:
                        tab[i].draw_number(26*i, 26+27*i)
                    if i > 1:
                        tab[i].draw_number(26+27*(i-1), 53+27*(i-1))

            pygame.display.update()

class ThirdPygameWindow():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("ALERT!")

        self.font = pygame.font.Font("freesansbold.ttf", 18)
        self.label1 = self.font.render("Reached Limit", 1, [255, 255, 255])
        self.label2 = self.font.render("Press Space Bar To Quit", 1, [255, 255, 255])

        self.window.blit(self.label1, (90, 100))
        self.window.blit(self.label2, (50, 120))

        self.running = True

    def Main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.quit()
                        self.window_trd = SecondPygameWindow()
                        self.window_trd.Main()

            pygame.display.update()

class FourthPygameWindow():
    def __init__(self):
        global list_note
        list_note = []

        pygame.init()
        self.window = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Make Your Choice")

        self.running = True

        #Instance of InputBox
        input_box1 = InputBoxPygame(50, 120, 200, 50, 1)
        self.input_boxes = [input_box1]

    def Main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                for box in self.input_boxes:
                    box.handle_event(event, self.window)

                self.window.fill([0, 0, 0])

            for box in self.input_boxes:
                box.draw(self.window)

            pygame.display.update()

class ButtonPygame:
    def __init__(self, x, y, width, height, choice, text):
        self.COLOR_INACTIVE = [255, 255, 255]
        self.COLOR_ACTIVE = [0, 0, 0]
        self.COLOR = [160, 160, 160]
        self.FONT = pygame.font.Font(None, 25)
        self.rect = pygame.Rect(x, y, width, height)
        self.choice = choice
        self.text = text

    def handle_event(self, event, window):
        #If mouse hovers the button
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            #Define the text surface
            self.text_surface = self.FONT.render(self.text, True, self.COLOR_ACTIVE)
        else:
            #Define the text surface
            self.text_surface = self.FONT.render(self.text, True, self.COLOR_INACTIVE)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                if self.choice == 0:
                    pygame.quit()
                    window_fst = SecondPygameWindow()
                    window_fst.Main()

                if self.choice == 1:
                    pass

                if self.choice == 2:
                    PlayTN = threading.Thread(target=PlayTheNotes)
                    PlayTN.daemon = True
                    PlayTN.start()

                if self.choice == 3:
                    WriteToFile()

                if self.choice == 4:
                    pygame.quit()
                    window_frth = FourthPygameWindow()
                    window_frth.Main()

    def draw(self, window):
        #Blit the rectangle
        pygame.draw.rect(window, self.COLOR, self.rect)
        #Blit the text
        window.blit(self.text_surface, (self.rect.x+8, self.rect.y+15))

class InputBoxPygame:
    def __init__(self, x, y, w, h, choice, text = ""):
        self.COLOR_INACTIVE = [0, 255, 0]
        self.COLOR_ACTIVE = [255, 0, 0]
        self.color = self.COLOR_INACTIVE
        self.FONT = pygame.font.Font(None, 32)
        self.text_surface = self.FONT.render(text, True, self.color)
        self.rect = pygame.Rect(x, y, w, h)
        self.choice = choice
        self.text = text
        self.active = False

    def handle_event(self, event, window):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.choice == 0:
                        global list_note, ReadOccured, PTNOccured

                        if len(list_note) < 1133: #26, 53, 80, 1133
                            for i in range(len(list_note)+1):
                                if ReadOccured == False:
                                    if 27*i <= len(list_note) <= ((27*(i+1))-1):
                                        PlaceTheNotes(window, 27*i, ((27*(i+1))-1), self.text)

                            if ReadOccured == True:
                                if 0 <= len(list_note) <= 26:
                                    PlaceTheNotes(window, 0, 26, self.text)
                                    PTNOccured = True
                                if 27 <= len(list_note) <= 53:
                                    PlaceTheNotes(window, 27, 53, self.text)
                                    PTNOccured = True

                        elif len(list_note) > 1132: #25, 52, 79, 1132
                            pygame.quit()
                            window_snd = ThirdPygameWindow()
                            window_snd.Main()

                    if self.choice == 1:
                        pygame.quit()
                        window_ffth = SecondPygameWindow(self.text)
                        window_ffth.Main()

                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.text_surface = self.FONT.render(self.text, True, self.color)

    def draw(self, window):
        # Blit the rect.
        pygame.draw.rect(window, self.color, self.rect, 2)
        # Blit the text.
        window.blit(self.text_surface, (self.rect.x+7, self.rect.y+10))

class TabsPygame:
    def __init__(self, x, y, width, height, text, choice):
        self.COLOR_INACTIVE = [255, 255, 255]
        self.COLOR_ACTIVE = [255, 0, 0]
        self.COLOR = [80, 80, 80]
        self.FONT = pygame.font.Font(None, 32)
        self.text_surface = self.FONT.render(text, True, self.COLOR_INACTIVE)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.choice = choice

    def handle_event(self, event, window, option):
        global CountPlayTN, tab
        #If mouse hovers the button
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            #Define the text surface
            self.text_surface = self.FONT.render(self.text, True, self.COLOR_ACTIVE)
        else:
            if CountPlayTN == 0:
                #Define the text surface
                self.text_surface = self.FONT.render(self.text, True, self.COLOR_INACTIVE)

            for i in range(len(tab)):
                if option == i:
                    if 0 <  CountPlayTN < (27*i)-1: #0, 26, 53, 80, 107, 134
                        self.text_surface = self.FONT.render(self.text, True, self.COLOR_INACTIVE)

        if event.type == pygame.MOUSEBUTTONDOWN:
            global list_note, ReadOccured, PTNOccured
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                for i in range(len(list_note)):
                    if self.choice == i:
                        if ReadOccured == False:
                            PlaceTheNotes(window, 26*i + i, 26 + 26*i + i)

                        if ReadOccured == True and PTNOccured == False:
                            PlaceTheNotes(window, 26*i, 26 + 26*i)

                        if ReadOccured == True and PTNOccured == True:
                            print("I don't know")

    def draw(self, window):
        #Blit the rectangle
        pygame.draw.rect(window, self.COLOR, self.rect)
        #Blit the text
        window.blit(self.text_surface, (self.rect.x+8, self.rect.y+8))

    def draw_number(self, beginning, ending):
        global CountPlayTN, done

        if beginning < CountPlayTN <= ending:
            self.text_surface = self.FONT.render(self.text, True, self.COLOR_ACTIVE)

        if ending < CountPlayTN:
            self.text_surface = self.FONT.render(self.text, True, self.COLOR_INACTIVE)

            if self.rect.collidepoint(pygame.mouse.get_pos()):
                #Define the text surface
                self.text_surface = self.FONT.render(self.text, True, self.COLOR_ACTIVE)
            else:
                #Define the text surface
                self.text_surface = self.FONT.render(self.text, True, self.COLOR_INACTIVE)

        if done == True:
            self.text_surface = self.FONT.render(self.text, True, self.COLOR_INACTIVE)

            if self.rect.collidepoint(pygame.mouse.get_pos()):
                #Define the text surface
                self.text_surface = self.FONT.render(self.text, True, self.COLOR_ACTIVE)
            else:
                #Define the text surface
                self.text_surface = self.FONT.render(self.text, True, self.COLOR_INACTIVE)

if __name__ == "__main__":
    FirstPygameWindow()
