from manim import *

config.background_color="#1E1E1E"
Text.set_default(font = "Manrope")

class AulaCompleta(MovingCameraScene):
    def construct(self):
          InicioParte2.construct(self)
          Rotatoria.construct(self)
          LogodaUTF.construct(self)
          CenaFinal.construct(self)
          
class InicioParte2(MovingCameraScene):
    def construct(self):
        # ----- Objetos ------
        # Antes
        textExemplo = Text("Exemplo")
        # Ai a câmera se move para cima desse objeto
        textPresenca = Text("Marcamos presença nas plataformas",
                            color="#1E1E1E",
                            t2c={"presença":"#AA77C7","plataformas":"#58C4DD"}).move_to((20,1,0))
        
        # Agora aqui vai ser definido um monte de svg (amooooo)
        svgDiscord = SVGMobject("./assets/discord.svg").move_to((15.5,-6,0)).scale(0.7)
        svgInstagram = SVGMobject("./assets/instagram.svg").move_to((18.5,-6,0)).scale(0.7)
        svgLinkedin = SVGMobject("./assets/linkedin.svg").move_to((21.5,-6,0)).scale(0.7)
        svgYoutube = SVGMobject("./assets/youtube.svg").move_to((24.5,-6,0)).scale(0.7)

        # ----- Animações -----
        self.camera.frame.save_state()
        # Antes
        self.add(textExemplo)
        self.wait()
        # troca o fundo de cor
        self.camera.background_color = "#ece6e2"
        self.wait()
        
        # A câmera se move
        self.play(self.camera.frame.animate.move_to(textPresenca))
        self.remove(textExemplo)
        self.wait()

        # Presenca
        self.play(Write(textPresenca))

        # Logos
        self.play(textPresenca.animate.shift(UP),
                  svgDiscord.animate.move_to((15.5,0,0)),
                  svgInstagram.animate.move_to((18.5,0,0)),
                  svgLinkedin.animate.move_to((21.5,0,0)),
                  svgYoutube.animate.move_to((24.5,0,0)))
        self.wait()

        # Destroi tudo
        self.play(self.camera.frame.animate.shift(DOWN*10))
        #self.remove(textExemplo)
        self.remove(textPresenca)
        self.remove(svgDiscord)
        self.remove(svgInstagram)
        self.remove(svgLinkedin)
        self.remove(svgYoutube)
        
        self.play(Restore(self.camera.frame))
        
class Rotatoria(MovingCameraScene):
    def construct(self):
        # ----- Objetos ------

        # Equipe unida
        textEquipe1 = Text("Apresentamos resultados,",color="#1E1E1E",t2c={"resultados":"#AA77C7"}).move_to((0,0.5,0))
        textEquipe2 = Text("graças a uma equipe unida e dedicada:", color="#1E1E1E",t2c={"unida":"#58C4DD","dedicada":"#236B8E"}).move_to((0,-0.5,0))


        # Circulo (mais grosso) sendo criado
        circleBonito = Circle(stroke_width=20, color="#1E1E1E")
        
        # Diretoria
        textDiretoria = Text("Diretoria",color="#AA77C7").move_to((0,2.5,0)).scale(0.6)
        pathDiretoria = VMobject(color="#1E1E1E")
        dotDiretoria = Dot(color="#1E1E1E").move_to([0,1,0])

        pathDiretoria.set_points_as_corners([dotDiretoria.get_center(), dotDiretoria.get_center()])

        def update_path(path):
                previous_path = path.copy()
                previous_path.add_points_as_corners([dotDiretoria.get_center()])
                path.become(previous_path)
        pathDiretoria.add_updater(update_path)



        # Tesouraria
        textTesouraria = Text("Tesouraria",color="#58C4DD").move_to((3.2,1.2,0)).scale(0.6)
        pathTesouraria = VMobject(color="#1E1E1E")
        dotTesouraria = Dot(color="#1E1E1E").move_to([0.7,0.7,0])

        pathTesouraria.set_points_as_corners([dotTesouraria.get_center(), dotTesouraria.get_center()])

        def update_path(path):
                previous_path = path.copy()
                previous_path.add_points_as_corners([dotTesouraria.get_center()])
                path.become(previous_path)
        pathTesouraria.add_updater(update_path)


        # Desenvolvimento
        textDesenvolvimento = Text("Desenvolvimento",color="#236B8E").move_to((4,-1.2,0)).scale(0.6)
        pathDesenvolvimento = VMobject(color="#1E1E1E")
        dotDesenvolvimento = Dot(color="#1E1E1E").move_to([0.7,-0.7,0])

        pathDesenvolvimento.set_points_as_corners([dotDesenvolvimento.get_center(), dotDesenvolvimento.get_center()])

        def update_path(path):
                previous_path = path.copy()
                previous_path.add_points_as_corners([dotDesenvolvimento.get_center()])
                path.become(previous_path)
        pathDesenvolvimento.add_updater(update_path)

        # Conteudo
        textConteudo = Text("Conteúdo",color="#AA77C7").move_to((0,-2.5,0)).scale(0.6)
        pathConteudo = VMobject(color="#1E1E1E")
        dotConteudo = Dot(color="#1E1E1E").move_to([0,-1,0])

        pathConteudo.set_points_as_corners([dotConteudo.get_center(), dotConteudo.get_center()])

        def update_path(path):
                previous_path = path.copy()
                previous_path.add_points_as_corners([dotConteudo.get_center()])
                path.become(previous_path)
        pathConteudo.add_updater(update_path)

        # Produtos
        textProdutos = Text("Produtos",color="#236B8E").move_to((-3.2,-1.2,0)).scale(0.6)
        pathProdutos = VMobject(color="#1E1E1E")
        dotProdutos = Dot(color="#1E1E1E").move_to([-0.7,-0.7,0])

        pathProdutos.set_points_as_corners([dotProdutos.get_center(), dotProdutos.get_center()])

        def update_path(path):
                previous_path = path.copy()
                previous_path.add_points_as_corners([dotProdutos.get_center()])
                path.become(previous_path)
        pathProdutos.add_updater(update_path)

        # Eem
        textEem1 = Text("Estratégia e",color="#58C4DD").move_to((-3.3,1.4,0)).scale(0.6)
        textEem2 = Text("Marketing",color="#58C4DD").move_to((-3.3,0.9,0)).scale(0.6)

        pathEem = VMobject(color="#1E1E1E")
        dotEem = Dot(color="#1E1E1E").move_to([-0.7,0.7,0])

        pathEem.set_points_as_corners([dotEem.get_center(), dotEem.get_center()])

        def update_path(path):
                previous_path = path.copy()
                previous_path.add_points_as_corners([dotEem.get_center()])
                path.become(previous_path)
        pathEem.add_updater(update_path)



        
        


        # ----- Animações -----
        self.camera.background_color = "#ece6e2"
        self.camera.frame.save_state()

        self.play(Write(textEquipe1))
        self.wait()
        self.play(Write(textEquipe2))
        self.wait()
        self.play(textEquipe1.animate.move_to((-20,0.5,0)),textEquipe2.animate.move_to((-20,-0.5,0)))

        self.play(Create(circleBonito))

        # Flecha diretoria
        self.add(pathDiretoria, dotDiretoria)
        self.play(dotDiretoria.animate.shift(UP),run_time=0.5)
        self.play(Write(textDiretoria),run_time=0.5)

        # Flecha tesouraria
        self.add(pathTesouraria, dotTesouraria)
        self.play(dotTesouraria.animate.shift((UP+RIGHT)*0.5),run_time=0.5)
        self.play(dotTesouraria.animate.shift((RIGHT)*0.8),run_time=0.5)
        self.play(Write(textTesouraria),run_time=0.5)

        # Flecha Desenvolvimento
        self.add(pathDesenvolvimento, dotDesenvolvimento)
        self.play(dotDesenvolvimento.animate.shift((DOWN+RIGHT)*0.5),run_time=0.5)
        self.play(dotDesenvolvimento.animate.shift((RIGHT)*0.8),run_time=0.5)
        self.play(Write(textDesenvolvimento,run_time=0.5))

        # Flecha Conteudo
        self.add(pathConteudo, dotConteudo)
        self.play(dotConteudo.animate.shift(DOWN),run_time=0.5)
        self.play(Write(textConteudo),run_time=0.5)


        # Flecha Produtos
        self.add(pathProdutos, dotProdutos)
        self.play(dotProdutos.animate.shift((DOWN+LEFT)*0.5),run_time=0.5)
        self.play(dotProdutos.animate.shift((LEFT)*0.8),run_time=0.5)
        self.play(Write(textProdutos),run_time=0.5)

        # Flecha Eem
        self.add(pathEem, dotEem)
        self.play(dotEem.animate.shift((UP+LEFT)*0.5),run_time=0.5)
        self.play(dotEem.animate.shift((LEFT)*0.8),run_time=0.5)
        self.play(Write(textEem1),run_time=0.5)
        self.play(Write(textEem2),run_time=0.5)

        
        self.wait()
        self.wait()

        self.play(self.camera.frame.animate.shift(DOWN*10))

        # Destroi turu e toros
        self.remove(textEquipe1, textEquipe2,
                    circleBonito,
                
                # Diretoria
                textDiretoria, pathDiretoria, dotDiretoria,
                
                # Tesouraria
                textTesouraria, pathTesouraria, dotTesouraria,
                
                # Desenvolvimento
                textDesenvolvimento, pathDesenvolvimento, dotDesenvolvimento,
                
                # Conteudo
                textConteudo, pathConteudo, dotConteudo,
                
                # Produtos
                textProdutos, pathProdutos, dotProdutos,
                
                # Eem
                textEem1, textEem2, pathEem, dotEem
                )
        
        self.play(Restore(self.camera.frame))
        
class LogodaUTF(MovingCameraScene):
    def construct(self):
        # ----- Objetos ------
        textComputacao = Text("Um projeto de computação",color="#1E1E1E",t2c={"computação":"#AA77C7"}).move_to((-1.4,1,0))
        textUTF = Text("da UTFPR",color="#1E1E1E",t2c={"UTFPR":"#ABAB3F"}).move_to((4.4,1.1,0))

        imageUTF = ImageMobject("./assets/utfpr.png").move_to((0,-1,0))
        


        # ----- Animações ------
        self.camera.background_color = "#ece6e2"
        self.camera.frame.save_state()

        # Abracadabra
        self.play(Write(textComputacao))
        self.wait()
        self.play(Write(textUTF))
        self.wait()
        self.play(FadeIn(imageUTF))
        self.wait()

        # Câmera desce para ver a cena final
        self.play(self.camera.frame.animate.shift(DOWN*10))
        self.remove(textComputacao,textUTF,imageUTF)
        self.play(Restore(self.camera.frame))

class CenaFinal(Scene):
    def construct(self):
        # ----- Objetos ------
        textComando = Text("Você é que está no comando!",color="#1E1E1E",t2c={"Você":"#236B8E","comando":"#AA77C7"}).move_to((1,0,0)).scale(0.8)
        
        svgComando = SVGMobject("./assets/comando.svg")

        # ----- Animações ------
        self.camera.background_color = "#ece6e2"

        self.play(SpinInFromNothing(svgComando))
        self.play(svgComando.animate.move_to((-4,0,0)))
        self.play(Write(textComando))
        self.wait()
        self.wait()

        self.play(Unwrite(textComando),ShrinkToCenter(svgComando),run_time=1.5)

        self.wait()