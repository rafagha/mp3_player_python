"""
Me desafiei a criar um mp3 player e saiu quase perfeito.
O volume e os botoes de acelerar não funcionam. Mas,
de resto, tudo ok.
Para funcionar de forma correta vc vai precisar instalar o pygame
e tbm alterar o caminho de onde a musica esta, da teus pulo.
"""

from tkinter import *
from tkinter import filedialog
import pygame


class MusicPlayer:
    """Classe da aplicação"""

    def __init__(self):
        self.music_player = Tk()

        # lista de musicas
        self.play_list = []

        # variaveis
        self.volume = DoubleVar()

        # pygame
        pygame.mixer.init()
        self.pausado = False
        self.comecou = False

        # imagens dos botoes
        #self.img_acelerar = PhotoImage(file="imgs/acelerar.png")
        self.img_anterior = PhotoImage(file="imgs/anterior.png")
        self.img_limpar_lista = PhotoImage(file="imgs/clear_list.png")
        self.img_estop = PhotoImage(file='imgs/estop.png')
        self.img_exit = PhotoImage(file="imgs/exit.png")
        self.img_mplayer = PhotoImage(file="imgs/mplayer.png")
        self.img_next = PhotoImage(file='imgs/next.png')
        self.img_open_folder = PhotoImage(file="imgs/open_folder.png")
        self.img_play_pause = PhotoImage(file='imgs/play_pause.png')
        self.img_remove_music = PhotoImage(file="imgs/remove_music.png")
        #self.img_retardar = PhotoImage(file="imgs/retardar.png")
        self.img_volume = PhotoImage(file='imgs/volume.png')

        self.wid_listbox()
        self.wid_btns()
        self.wid_vol()
        self.janela_principal()

    def janela_principal(self):
        """Janela principal do App"""

        # da linha 54 ate a 68 é uma gambiarra para centralizar a tela
        window_height = 400
        window_width = 600

        screen_width = self.music_player.winfo_screenwidth()
        screen_height = self.music_player.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2)) - 40

        lab_img_mplayer = Label(self.music_player, image=self.img_mplayer)
        lab_img_mplayer.place(relx=0.05, rely=0.06)

        Label(self.music_player, text="Mp3 Player", font=('verdana', 43, 'bold')).place(relx=.2, rely=0.05)

        self.music_player.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.music_player.title('Mp3 Player')
        self.music_player.mainloop()

    def wid_listbox(self):
        """função widget lista que exibe as musicas"""
        self.list_box = Listbox(self.music_player, width=64, selectbackground='gray',
                                selectforeground='black', bg='black', fg='green')
        self.list_box.place(relx=0.18, rely=0.35)

    def wid_btns(self):
        """botoes da aplicação"""
        self.btn_abrir_pasta = Button(self.music_player, bd=3, image=self.img_open_folder,
                                      command=self.func_carregar_musicas)
        self.btn_abrir_pasta.place(relx=0.05, rely=.35, width=50, height=50)

        self.btn_player_pause = Button(self.music_player, bd=3, image=self.img_play_pause, command=self.func_play_pause)
        self.btn_player_pause.place(relx=0.05, rely=0.50, width=50, height=50)

        self.btn_stop = Button(self.music_player, bd=3, image=self.img_estop, command=self.func_stop)
        self.btn_stop.place(relx=0.05, rely=0.65, width=50, height=50)

        self.btn_retroceder = Button(self.music_player, bd=3, image=self.img_anterior, command=self.func_previous)
        self.btn_retroceder.place(relx=0.25, rely=.81, width=50, height=50)

        #self.btn_retardar = Button(self.music_player, bd=3, image=self.img_retardar)
        #self.btn_retardar.place(relx=.39, rely=.81, width=50, height=50)

        #self.btn_acelerar = Button(self.music_player, bd=3, image=self.img_acelerar)
        #self.btn_acelerar.place(relx=.53, rely=.81, width=50, height=50)

        self.btn_next = Button(self.music_player, bd=3, image=self.img_next, command=self.func_next)
        self.btn_next.place(relx=.67, rely=.81, width=50, height=50)

        self.btn_remover = Button(self.music_player, bd=3, image=self.img_remove_music, command=self.func_remove_item)
        self.btn_remover.place(relx=.87, rely=0.50, width=50, height=50)

        self.btn_limpar_lista = Button(self.music_player, bd=3, image=self.img_limpar_lista, command=self.func_clear_listbox)
        self.btn_limpar_lista.place(relx=.87, rely=0.65, width=50, height=50)

        self.btn_sair = Button(self.music_player, bd=3, image=self.img_exit,
                               command=lambda: self.music_player.destroy())
        self.btn_sair.place(relx=0.87, rely=0.35, width=50, height=50)


    def func_set_vol(self, event):
        """função que imprime o volume"""
        print(type(event.widget.get()))

    def wid_vol(self):
        """widget volume"""
        self.lab_volume = Label(self.music_player, image=self.img_volume)
        self.lab_volume.place(relx=.20, rely=0.26)

        self.escala = Scale(self.music_player, variable=self.volume, orient=HORIZONTAL, bd=3, length=300)
        self.escala.bind("<ButtonRelease>", self.func_set_vol)
        self.escala.place(relx=.27, rely=0.22)

    def func_carregar_musicas(self):
        """função que carrega as musicas"""
        musicas = filedialog.askopenfilename(multiple=True,
                                             initialdir="C:/Users/regar/PycharmProjects/mp3_player/musicas", title="Selecione as musicas",
                                             filetypes=(("mp3", "*.mp3*"), ("all files", "*.*")))

        # da linha 134 ate 147 é uma gambiarra
        # o mais correto é usar regex, mas não sei regex
        s = ''
        for i in musicas:
            self.play_list.append(i)
            i = i.replace('C:/Users/regar/PycharmProjects/mp3_player/musicas/', '')
            i = i[::-1]

            for x in i:
                if x == '/':
                    break
                else:
                    s += x
            s = s[::-1]
            self.list_box.insert('end', s)
            s = ''

    def func_stop(self):
        """função stop"""
        pygame.mixer.music.stop()
        self.list_box.select_clear(ACTIVE)
        self.comecou = False

    def func_play_pause(self):
        """função play-pause"""
        tocando = pygame.mixer.music.get_busy()
        print(type(tocando))
        print(tocando)

        if not self.comecou:
            if len(self.play_list) == 0:
                pass

            else:
                music = self.list_box.curselection()
                if len(music) > 0:
                    print('foi selecionado')
                    music = self.play_list[music[0]]

                else:
                    print('nao foi')
                    music = self.play_list[0]

                print(music)
                pygame.mixer.music.load(music)
                pygame.mixer.music.play(loops=0)
                self.comecou = True
                #print(pygame.mixer.music.get_volume())
                #pygame.mixer.music.set_volume(1)

        elif self.comecou and self.pausado == False:
            pygame.mixer.music.pause()
            self.pausado = True

        elif self.pausado:
            pygame.mixer.music.unpause()
            self.pausado = False

    def func_next(self):
        """função passar musica"""
        atual = self.list_box.curselection()

        if atual == () and self.list_box.size() > 0:
            pygame.mixer.music.load(self.play_list[0])
            pygame.mixer.music.play(loops=0)
            self.list_box.select_clear(0, END)
            self.list_box.activate(0)
            self.list_box.select_set(0, last=None)

        if len(list(atual)) == 1:
            if atual[0] < len(self.play_list)-1:
                next = atual[0] + 1
                m = self.play_list[next]
                pygame.mixer.music.load(m)
                pygame.mixer.music.play(loops=0)
                self.list_box.select_clear(0, END)
                self.list_box.activate(next)
                self.list_box.select_set(next, last=None)

            else:
                pygame.mixer.music.load(self.play_list[0])
                pygame.mixer.music.play(loops=0)
                self.list_box.select_clear(0, END)
                self.list_box.activate(0)
                self.list_box.select_set(0, last=None)

    def func_previous(self):
        """função musica anterior"""
        atual = self.list_box.curselection()
        print(len(self.play_list))
        if len(list(atual)) == 1:
            print(atual)
            pre = atual[0] - 1
            if pre >= 0:
                m = self.play_list[pre]
                pygame.mixer.music.load(m)
                pygame.mixer.music.play(loops=0)
                self.list_box.select_clear(0, END)
                self.list_box.activate(pre)
                self.list_box.select_set(pre, last=None)

    def func_remove_item(self):
        """função remover musica"""
        item = self.list_box.curselection()
        try:
            self.list_box.delete(item)
        except:
            pass
        else:
            del(self.play_list[item[0]])

    def func_clear_listbox(self):
        """função limpar lista"""
        self.func_stop()
        self.list_box.delete(0, END)
        self.play_list = []

player = MusicPlayer()
