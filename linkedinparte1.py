from manim import *
from manim import UpdateFromFunc
MarkupText.set_default(font = "Trade Gothic")
PATH_COLOR = "#aa77c7"
BG_COLOR = "#0D0D1A"

class LinkedinParte1(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        logo_svg = SVGMobject("assets/logoComando.svg").scale(1.5).move_to(ORIGIN)
        
        self.play(Write(logo_svg))
        self.play(logo_svg.animate.shift(UP*0.7))        
        comando = MarkupText('<b>comando.c</b>', font="Major Mono Display").next_to(logo_svg, DOWN, buff=0.1).scale(0.6)

        path = [
            np.array([0.000,  -2.000, 0.0]),# inicio do ponto q aparece na tela
            np.array([0.000, -8.000, 0.0]), 
            np.array([0.907, -8.707, 0.0]),# pausa aqui i=1
            np.array([0.907, -14.707, 0.0]),
            np.array([0.000, -15.414, 0.0]),# pausa aqui i=3
            np.array([0.000, -21.414, 0.0]),
            np.array([0.907, -22.121, 0.0])# pausa aqui i=5
        ] # path que será percorrido

        guia = VGroup(*[
            Line(path[i], path[i + 1])
            .set_color(PATH_COLOR)
            .set_stroke(width=1.5, opacity=0.15)
            for i in range(len(path) - 1)
        ])
        self.add(guia)

        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5
        ).move_to(comando[0]).scale(0.3)

        self.play(TypeWithCursor(comando, cursor))
        self.play(Blink(cursor, blinks=1))
        self.remove(cursor)
        self.wait(0.6)

        ponto = Dot(color=PATH_COLOR, radius=0.13)
        brilho = ponto.copy().scale(2).set_opacity(0.18)
        traveller = VGroup(brilho, ponto)
        traveller.move_to(path[0])
        self.add(traveller)

        # ------------------------animações em cada parada-----------------------
        primeira = MarkupText('<span><b>Qualidade</b> de ensino</span>', font_size=70).scale(0.7).next_to(path[2], RIGHT, buff=0.6)
        capelo = ImageMobject("assets/image.png").scale(0.6).next_to(primeira, UP, buff=0.1)
        a1 = Group(primeira, capelo)

        segunda = MarkupText('<span><b>Democratização</b>\ndo Conhecimento</span>', font_size=70).scale(0.7).next_to(path[4], LEFT, buff=0.6)
        pessoas = ImageMobject("assets/grupopessoas.png").scale(0.6).next_to(segunda, UP, buff=0.1)
        a2=Group(segunda, pessoas)

        terceira = MarkupText('<span><b>Fidelidade</b> ao\nconhecimento técnico</span>', font_size=70).scale(0.7).next_to(path[6], RIGHT, buff=0.6)
        livro = ImageMobject("assets/livro2.png").scale(0.6).next_to(terceira, UP, buff=0.4)
        a3 = Group(terceira, livro)
        #-------------------------------------------------------------------------

        offset = 0 # ajusta câmera em relação ao traveller

        def follow_camera(m):
            m.move_to(traveller.get_center() + offset)

        self.play(
            self.camera.frame.animate.move_to(traveller.get_center() + offset),
            run_time=0.6,
            rate_func=linear
        )
        for i in range(len(path) - 1):
            inicio = path[i]
            fim = path[i+1]

            dist = np.linalg.norm(fim - inicio)
            tempo = dist * 0.3 # percorre 1 unidade de distância do path em 0.3s

            seg = Line(inicio, fim).set_color(PATH_COLOR).set_stroke(width=4)

            self.play(
                MoveAlongPath(traveller, Line(inicio, fim)),
                UpdateFromFunc(self.camera.frame, follow_camera),
                Create(seg),
                run_time=tempo,
                rate_func=linear
            )

            if i in [1, 3, 5]:
                self.wait(0.5)

                if i == 1:
                    self.play(
                        FadeIn(primeira),
                        SpinInFromNothing(capelo),
                        self.camera.frame.animate.move_to(a1),
                        run_time=1
                    )
                    self.play(Circumscribe(primeira, color="#5CE1E6", buff=0.1))
                    self.wait(0.5)
                    
                    #calcula o novo offset
                    offset = self.camera.frame.get_center() - traveller.get_center()
                elif i == 3:
                    self.play(
                        FadeIn(segunda),
                        SpinInFromNothing(pessoas),
                        self.camera.frame.animate.move_to(a2),
                        run_time=1
                    )
                    self.play(Circumscribe(segunda, color="#5CE1E6", buff=0.1))
                    self.wait(0.5)

                    #calcula o novo offset
                    offset = self.camera.frame.get_center() - traveller.get_center()
                elif i == 5:
                    self.play(
                        FadeIn(terceira),
                        SpinInFromNothing(livro),
                        self.camera.frame.animate.move_to(a3),
                        run_time=1
                    )
                    self.play(Circumscribe(terceira, color="#5CE1E6", buff=0.1))
                    self.wait(0.5)

                    #calcula o novo offset
                    offset = self.camera.frame.get_center() - traveller.get_center()