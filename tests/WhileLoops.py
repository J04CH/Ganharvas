import pygame
import threading
import time

def Tracer(aClass): #Gets called at @ decoration
    global list
    list = []
    global tab
    tab = []
    global count
    count = 0
    class Wrapper:
        calls = 0
        def __init__(self, *args): #Gets called at instanciation
            self.wrapped = aClass(*args) #Instances as argument
            Wrapper.calls += 1
            global times
            times = Wrapper.calls
        def __getattr__(self, name): #Gets called when using Main method
            return getattr(self.wrapped, name)
    return Wrapper

@Tracer
class SecondPygameWindow:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((900, 860))
        pygame.display.set_caption("Gandharvas")

        self.window.fill([255, 255, 255])

        #Load Images
        self.white = pygame.image.load("player/resources/img/white-square.jpg")
        self.CDS = pygame.image.load("player/resources/img/cle-de-sol.png")

        #Put Image Onto Screen
        self.window.blit(self.CDS, (0, 75))

        #Draw First Five Lines
        pygame.draw.line(self.window, [0, 0, 0], (80, 77.5), (810, 77.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 112.5), (810, 112.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 147.5), (810, 147.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 182.5), (810, 182.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 217.5), (810, 217.5), 4)

        #Draw Second Five Lines
        pygame.draw.line(self.window, [0, 0, 0], (80, 357.5), (810, 357.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 392.5), (810, 392.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 427.5), (810, 427.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 462.5), (810, 462.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 497.5), (810, 497.5), 4)

        #Draw Third Five Lines
        pygame.draw.line(self.window, [0, 0, 0], (80, 637.5), (810, 637.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 672.5), (810, 672.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 707.5), (810, 707.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 742.5), (810, 742.5), 4)
        pygame.draw.line(self.window, [0, 0, 0], (80, 777.5), (810, 777.5), 4)

        self.running = True

    def PreMain(self):
        global times
        global tab

        while True:
            #Instance of Tabs Panel
            for i in range(times):
                if i < times:
                    tab.append(TabsPygame(0, 44*i, 30, 38, "{0}".format(i)))

    def Main(self):
        #Main Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                for tabs in tab:
                    tabs.handle_event(event, self.window)

            #Put Image Onto Screen
            self.window.blit(self.white, (853, 816))

            for tabs in tab:
                tabs.draw(self.window)

            pygame.display.update()

class TabsPygame():
    def __init__(self, x, y, width, height, text):
        self.COLOR_INACTIVE = [255, 255, 255]
        self.COLOR_ACTIVE = [255, 0, 0]
        self.COLOR = [160, 160, 160]
        self.FONT = pygame.font.Font(None, 32)
        self.text_surface = self.FONT.render(text, True, self.COLOR)
        self.rect = pygame.Rect(x, y, width, height)
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
                PreMadeNotes(window)

    def draw(self, window):
        #Blit the rectangle
        pygame.draw.rect(window, self.COLOR, self.rect)
        #Blit the text
        window.blit(self.text_surface, (self.rect.x+8, self.rect.y+10))

if __name__ == '__main__':
    window_screen = SecondPygameWindow()
    t1 = threading.Thread(target=window_screen.PreMain)
    t1.start()
    t2 = threading.Thread(target=window_screen.Main())
    t2.start()
