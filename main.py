import customtkinter as ctk
import os
import sys
import math

def caminho_recurso(nome):
    if getattr(sys, "frozen", False):
        pasta = sys._MEIPASS
    else:
        pasta = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(pasta, nome)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# 1 Classe
class Aplicativo(ctk.CTk):
    # 1.1 Função que fica repetindo as funções para o programa ficar aberto
    def __init__(self):
        #1.1.1
        super().__init__()
        self.title("Missão Aurora - Simulador de pouso")
        self.geometry("850x700")

        # 1.1.3 Configuração da grade
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # 1.1.4 Criação dos frames
            # 1.1.4.1 Criação da aba esquerda 
        self.aba_left = ctk.CTkFrame(self, width=200)
        self.aba_left.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.aba_left.grid_columnconfigure(0, weight=1)
        self.aba_left.grid_columnconfigure(1, weight=1)

            # 1.1.4.2 Criação da aba direita
        self.aba_right = ctk.CTkFrame(self, width=400)
        self.aba_right.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)
                                    
        self.construir_aba_left()
        self.construir_aba_right()

        self.landing_id = None
        self.simulation_id = None
        self.cronometro_id = None
        self.tempo_total = 0

    # 1.2 Função que cria aba esquerda do programa
    def construir_aba_left(self):
        # 1.2.1 Grade e título
        self.title_aba_left = ctk.CTkLabel(self.aba_left, text="Configuração", font=("Arial", 20,"bold"))
        self.title_aba_left.grid(row=0, columnspan=2, sticky="we",padx=10, pady=10)

        # Prioridade de pouso

        self.frame_priority = ctk.CTkFrame(self.aba_left)

            # Título
        self.caption_priority = ctk.CTkLabel(self.frame_priority, text="Prioridade de pouso", font=("Arial", 16, "bold"))
        self.caption_priority.pack()

        
            # Habitação
        self.box_habitat = ctk.CTkFrame(
            self.frame_priority,
            height=35,
            corner_radius=8,
            border_width=0
        )
        self.box_habitat.pack_propagate(False)

        self.text_box_habitat = ctk.CTkLabel(
            self.box_habitat,
            text="Habitação",
            font=("Arial", 12),
            fg_color="transparent",
            corner_radius=0
        )
        self.text_box_habitat.pack(
            side="left",
            fill="both",
            expand=True
        )
            # Energia
        self.box_energy = ctk.CTkFrame(
            self.frame_priority,
            height=35,
            corner_radius=8,
            border_width=0
        )
        self.box_energy.pack_propagate(False)

        self.text_box_energy = ctk.CTkLabel(
            self.box_energy,
            text="Energia",
            font=("Arial", 12),
            fg_color="transparent",
            corner_radius=0
        )
        self.text_box_energy.pack(fill="both", expand=True)
            # Labotatório científico
        self.box_lc = ctk.CTkFrame(
            self.frame_priority,
            height=35,
            corner_radius=8,
            border_width=0
        )
        self.box_lc.pack_propagate(False)

        self.text_box_lc = ctk.CTkLabel(
            self.box_lc,
            text="Laboratório científico",
            font=("Arial", 12),
            fg_color="transparent",
            corner_radius=0
        )
        self.text_box_lc.pack(
            side="left",
            fill="both",
            expand=True
        )
            # Logistica
        self.box_logistic = ctk.CTkFrame(
            self.frame_priority,
            height=35,
            corner_radius=8,
            border_width=0
        )
        self.box_logistic.pack_propagate(False)

        self.text_box_logistic = ctk.CTkLabel(
            self.box_logistic,
            text="Logística",
            font=("Arial", 12),
            fg_color="transparent",
            corner_radius=0
        )
        self.text_box_logistic.pack(
            side="left",
            fill="both",
            expand=True
        )
            # Suporte médico
        self.box_sm = ctk.CTkFrame(
            self.frame_priority,
            height=35,
            corner_radius=8,
            border_width=0
        )
        self.box_sm.pack_propagate(False)

        self.text_box_sm = ctk.CTkLabel(
            self.box_sm,
            text="Suporte médico",
            font=("Arial", 12),
            fg_color="transparent",
            corner_radius=0
        )
        self.text_box_sm.pack(
            side="left",
            fill="both",
            expand=True
        )
            # Estação
        self.box_es = ctk.CTkFrame(
            self.frame_priority,
            height=35,
            corner_radius=8,
            border_width=0
        )
        self.box_es.pack_propagate(False)

        self.text_box_es = ctk.CTkLabel(
            self.box_es,
            text="Estação",
            font=("Arial", 12),
            fg_color="transparent",
            corner_radius=0
        )
        self.text_box_es.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Lista dos seis módulos, na ordem inicial
        self.frames_priority = [
            self.box_habitat,
            self.box_energy,
            self.box_lc,
            self.box_logistic,
            self.box_sm,
            self.box_es
        ]
        # Associa cada módulo ao seu rótulo de nome
        self.fuel_habitat = 0
        self.mass_habitat = 0
        self.cc_habitat = 0

        self.variveis_test  = [self.text_box_habitat, self.fuel_habitat, self.mass_habitat, self.cc_habitat]

        self.labels_modulos = {
            self.box_habitat: self.text_box_habitat,
            self.box_energy: self.text_box_energy,
            self.box_lc: self.text_box_lc,
            self.box_logistic: self.text_box_logistic,
            self.box_sm: self.text_box_sm,
            self.box_es: self.text_box_es,
}

        # Cria os números de prioridade
        self.labels_prioridade = {}

        for modulo in self.frames_priority:
            # Número da prioridade
            label = ctk.CTkLabel(
                modulo,
                text="",
                width=30,
                font=("Arial", 12, "bold"),
                anchor="center"
            )
            label.pack(side="left", padx=(10, 0), fill="y")

            self.labels_prioridade[modulo] = label

            # Nome do módulo ao lado do número
            nome = self.labels_modulos[modulo]
            nome.pack_forget()
            nome.pack(side="left", fill="both", expand=True)

            self.frame_selecionado = None


            def selecionar_modulo(frame):
                self.frame_selecionado = frame

                for modulo in self.frames_priority:
                    modulo.configure(
                        fg_color=("gray90", "gray17"),
                        border_width=0
                    )

                frame.configure(
                    fg_color=("gray75", "gray30"),
                    border_width=2,
                    border_color="#00BFFF"
                )



        def atualizar_posicoes():
            for modulo in self.frames_priority:
                modulo.pack_forget()

            for indice, modulo in enumerate(self.frames_priority, start=1):
                self.labels_prioridade[modulo].configure(
                    text=f"{indice}."
                )
                modulo.pack(fill="x", padx=5, pady=5)

            self.botoes_prioridade.pack_forget()
            self.botoes_prioridade.pack(pady=10)


        def subir_modulo():
            if self.frame_selecionado is None:
                return

            indice = self.frames_priority.index(self.frame_selecionado)

            if indice > 0:
                self.frames_priority[indice], self.frames_priority[indice - 1] = (
                    self.frames_priority[indice - 1],
                    self.frames_priority[indice]
                )

                atualizar_posicoes()


        def descer_modulo():
            if self.frame_selecionado is None:
                return

            indice = self.frames_priority.index(self.frame_selecionado)

            if indice < len(self.frames_priority) - 1:
                self.frames_priority[indice], self.frames_priority[indice + 1] = (
                    self.frames_priority[indice + 1],
                    self.frames_priority[indice]
                )

                atualizar_posicoes()


        # Permite selecionar um módulo clicando nele ou no seu conteúdo
        for modulo in self.frames_priority:
            modulo.bind(
                "<Button-1>",
                lambda evento, m=modulo: selecionar_modulo(m)
            )

            for filho in modulo.winfo_children():
                filho.bind(
                    "<Button-1>",
                    lambda evento, m=modulo: selecionar_modulo(m)
                )


        # Botões compartilhados
        self.botoes_prioridade = ctk.CTkFrame(self.frame_priority)

        self.button_up_module = ctk.CTkButton(
            self.botoes_prioridade,
            text="↑",
            width=45,
            command=subir_modulo
        )
        self.button_up_module.pack(side="left", padx=5, pady=5)

        self.button_down_module = ctk.CTkButton(
            self.botoes_prioridade,
            text="↓",
            width=45,
            command=descer_modulo
        )
        self.button_down_module.pack(side="left", padx=5, pady=5)

        # Mostra os módulos na ordem inicial
        atualizar_posicoes()

        # Os botões ficam abaixo dos módulos
        self.botoes_prioridade.pack(pady=10)

        # Função que verifica se é um número a informação inserida pelo usuário
        def validacao(valor):
            if valor in ("", "."):
                return True

            if valor.startswith("-"):
                valor = valor[1:]

            if valor.count(".") > 1:
                return False

            return valor.replace(".", "", 1).isdigit() or valor.endswith(".")


        # 1.2.2 Habitação---------------------------------

            # 1.2.2.1 Frame
        self.frame_habitat = ctk.CTkFrame(self.aba_left)

            # 1.2.2.2 Subtítulo
        self.caption_habitat = ctk.CTkLabel(self.frame_habitat, text="Habitação", font=("Arial", 16, "bold"),)
        self.caption_habitat.grid(row=0, columnspan=2, sticky="we", padx=10, pady=10)
            # 1.2.2.4 Nível de combustível
        self.text_nivel_fuel_habitat = ctk.CTkLabel(self.frame_habitat, text="Nível de combustível: ", font=("Arial", 12))
        self.text_nivel_fuel_habitat.grid(row=2, column=0, padx=(5,0))
        self.text_nivel_fuel_habitat_entry = ctk.CTkEntry(self.frame_habitat, font=("Arial", 12), validate="key", validatecommand=(
        self.register(validacao), "%P"))
        self.text_nivel_fuel_habitat_entry.grid(row=2, column=1, padx=(0,5), pady=(0,5))
            # 1.2.2.5 Massa
        self.text_mass_habitat = ctk.CTkLabel(self.frame_habitat, text="Massa: ", font=("Arial", 12))
        self.text_mass_habitat.grid(row=3, column=0, padx=(5,0))
        self.text_mass_habitat_entry = ctk.CTkEntry(self.frame_habitat, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_mass_habitat_entry.grid(row=3, column=1, padx=(0,5), pady=(0,5))
            # 1.2.2.6 Criticidade da carga
        self.text_cc_habitat = ctk.CTkLabel(self.frame_habitat, text="Criticidade da carga: ", font=("Arial", 12))
        self.text_cc_habitat.grid(row=4, column=0, padx=(5,0))
        self.text_cc_habitat_entry = ctk.CTkOptionMenu(self.frame_habitat, values=["Baixa", "Média", "Alta"], font=("Arial", 12))
        self.text_cc_habitat_entry.grid(row=4, column=1, padx=(0,5), pady=(0,5))

        # 1.2.3 Energia---------------------------------
            # 1.2.3.1 Frame
        self.frame_energy = ctk.CTkFrame(self.aba_left)

            # 1.2.3.2 Subtítulo
        self.caption_energy = ctk.CTkLabel(self.frame_energy, text="Energia", font=("Arial", 16, "bold"))
        self.caption_energy.grid(row=0, columnspan=2, sticky="we", padx=10, pady=10)
            # 1.2.3.4 Nível de combustível
        self.text_fuel_energy = ctk.CTkLabel(self.frame_energy, text="Nível de combustível: ", font=("Arial", 12))
        self.text_fuel_energy.grid(row=2, column=0, padx=(5,0))
        self.text_fuel_energy_entry = ctk.CTkEntry(self.frame_energy, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_fuel_energy_entry.grid(row=2, column=1, padx=(0,5), pady=(0,5))
            # 1.2.3.5 Massa
        self.text_mass_energy = ctk.CTkLabel(self.frame_energy, text="Massa: ", font=("Arial", 12))
        self.text_mass_energy.grid(row=3, column=0, padx=(5,0))
        self.text_mass_energy_entry = ctk.CTkEntry(self.frame_energy, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_mass_energy_entry.grid(row=3, column=1, padx=(0,5), pady=(0,5))
            # 1.2.3.5 Criticidade da carga
        self.text_cc_energy = ctk.CTkLabel(self.frame_energy, text="Criticidade da carga: ", font=("Arial", 12))
        self.text_cc_energy.grid(row=4, column=0, padx=(5,0))
        self.text_cc_energy_entry = ctk.CTkOptionMenu(self.frame_energy, values=["Baixa", "Média", "Alta"], font=("Arial", 12))
        self.text_cc_energy_entry.grid(row=4, column=1, padx=(0,5), pady=(0,5))

        # 1.2.4 Laboratório científico---------------------------------
            # 1.2.4.1 Frame
        self.frame_lc = ctk.CTkFrame(self.aba_left)

            # 1.2.4.2 Título
        self.caption_lc = ctk.CTkLabel(self.frame_lc, text="Laboratório Científico", font=("Arial", 16, "bold"))
        self.caption_lc.grid(row=0, columnspan=2)
            # 1.2.4.4 Nível de combustível
        self.text_fuel_lc = ctk.CTkLabel(self.frame_lc, text="Nível de combustível: ", font=("Arial", 12))
        self.text_fuel_lc.grid(row=2, column=0, padx=(5,0))
        self.text_fuel_lc_entry = ctk.CTkEntry(self.frame_lc, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_fuel_lc_entry.grid(row=2, column=1, padx=(0,5), pady=(0,5))
            # 1.2.4.5 Massa
        self.text_mass_lc = ctk.CTkLabel(self.frame_lc, text="Massa: ", font=("Arial", 12))
        self.text_mass_lc.grid(row=3, column=0, padx=(5,0))
        self.text_mass_lc_entry = ctk.CTkEntry(self.frame_lc, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_mass_lc_entry.grid(row=3, column=1, padx=(0,5), pady=(0,5))
            # 1.2.4.6 Criticidade da carga
        self.text_cc_lc = ctk.CTkLabel(self.frame_lc, text="Criticidade da carga: ", font=("Arial", 12))
        self.text_cc_lc.grid(row=4, column=0, padx=(5,0))
        self.text_cc_lc_entry = ctk.CTkOptionMenu(self.frame_lc, values=["Baixa", "Média", "Alta"], font=("Arial", 12))
        self.text_cc_lc_entry.grid(row=4, column=1, padx=(0,5), pady=(0,5))
        
        # 1.2.5 Logística---------------------------------
            # 1.2.5.1 Frame
        self.frame_logistic = ctk.CTkFrame(self.aba_left)
            # 1.2.5.2 Subtítulo
        self.caption_logistic = ctk.CTkLabel(self.frame_logistic, text="Logística", font=("Arial", 16, "bold"))
        self.caption_logistic.grid(row=0, columnspan = 2)
            # 1.2.5.4 Nível de combustível
        self.text_fuel_logistic = ctk.CTkLabel(self.frame_logistic, text="Nível de combustível: ", font=("Arial", 12))
        self.text_fuel_logistic.grid(row=2, column=0, padx=(5,0))
        self.text_fuel_logistic_entry = ctk.CTkEntry(self.frame_logistic, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_fuel_logistic_entry.grid(row=2, column=1, padx=(0,5), pady=(0,5))
            # 1.2.5.5 Massa
        self.text_mass_logistic = ctk.CTkLabel(self.frame_logistic, text="Massa: ", font=("Arial", 12))
        self.text_mass_logistic.grid(row=3, column=0, padx=(5,0))
        self.text_mass_logistic_entry = ctk.CTkEntry(self.frame_logistic, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_mass_logistic_entry.grid(row=3, column=1, padx=(0,5), pady=(0,5))
            # 1.2.5.6 Criticidade da carga
        self.text_cc_logistic = ctk.CTkLabel(self.frame_logistic, text="Criticidade da carga: ", font=("Arial", 12))
        self.text_cc_logistic.grid(row=4, column=0, padx=(5,0))
        self.text_cc_logistic_entry = ctk.CTkOptionMenu(self.frame_logistic, values=["Baixa", "Média", "Alta"], font=("Arial", 12))
        self.text_cc_logistic_entry.grid(row=4, column=1, padx=(0,5), pady=(0,5))

        # 1.2.6 Suporte Médico---------------------------------
            # 1.2.6.1 Frame
        self.frame_sm = ctk.CTkFrame(self.aba_left)

            # 1.2.6.2 Subtítulo
        self.caption_sm = ctk.CTkLabel(self.frame_sm, text="Suporte Médico", font=("Arial", 16, "bold"))
        self.caption_sm.grid(row=0, columnspan = 2)
            # 1.2.6.4 Nível de combustível
        self.text_fuel_sm = ctk.CTkLabel(self.frame_sm, text="Nível de combustível: ", font=("Arial", 12))
        self.text_fuel_sm.grid(row=2, column =0, padx=(5,0))
        self.text_fuel_sm_entry = ctk.CTkEntry(self.frame_sm, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_fuel_sm_entry.grid(row=2, column=1, padx=(0,5), pady=(0,5))
            # 1.2.6.5 Massa
        self.text_mass_sm = ctk.CTkLabel(self.frame_sm, text="Massa: ", font=("Arial", 12))
        self.text_mass_sm.grid(row=3, column =0, padx=(5,0))
        self.text_mass_sm_entry = ctk.CTkEntry(self.frame_sm, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_mass_sm_entry.grid(row=3, column=1, padx=(0,5), pady=(0,5))
            # 1.2.6.6 Criticidade da carga
        self.text_cc_sm = ctk.CTkLabel(self.frame_sm, text="Criticidade da carga: ", font=("Arial", 12))
        self.text_cc_sm.grid(row=4, column =0, padx=(5,0))
        self.text_cc_sm_entry = ctk.CTkOptionMenu(self.frame_sm, values=["Baixa", "Média", "Alta"], font=("Arial", 12))
        self.text_cc_sm_entry.grid(row=4, column=1, padx=(0,5), pady=(0,5))

        # 1.2.7 Estação---------------------------------
            # 1.2.7.1 Frame
        self.frame_es = ctk.CTkFrame(self.aba_left)

            # 1.2.7.2 Subtítulo
        self.caption_es = ctk.CTkLabel(self.frame_es, text="Estação", font=("Arial", 16, "bold"))
        self.caption_es.grid(row=0, columnspan=2)
            # 1.2.7.4 Nível de combustível
        self.text_fuel_es = ctk.CTkLabel(self.frame_es, text="Nível de combustível: ", font=("Arial", 12))
        self.text_fuel_es.grid(row=2, column=0,  padx=(5,0))
        self.text_fuel_es_entry = ctk.CTkEntry(self.frame_es, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_fuel_es_entry.grid(row=2, column=1, padx=(0,5), pady=(0,5))
            # 1.2.7.5 Massa
        self.text_mass_es = ctk.CTkLabel(self.frame_es, text="Massa: ", font=("Arial", 12))
        self.text_mass_es.grid(row=3, column=0,  padx=(5,0))
        self.text_mass_es_entry = ctk.CTkEntry(self.frame_es, validate="key", validatecommand=(
        self.register(validacao), "%P"), font=("Arial", 12))
        self.text_mass_es_entry.grid(row=3, column=1, padx=(0,5), pady=(0,5))
            # 1.2.7.6 Criticidade da carga
        self.text_cc_es = ctk.CTkLabel(self.frame_es, text="Criticidade da carga: ", font=("Arial", 12))
        self.text_cc_es.grid(row=4, column=0,  padx=(5,0))
        self.text_cc_es_entry = ctk.CTkOptionMenu(self.frame_es, values=["Baixa", "Média", "Alta"], font=("Arial", 12))
        self.text_cc_es_entry.grid(row=4, column=1, padx=(0,5), pady=(0,5))

        # 1.2.8 Visualização dos módulos em andamento
        self.frame_running = ctk.CTkFrame(self.aba_left)
        self.caption_running = ctk.CTkLabel(self.frame_running, text=f"Módulo:", font=("Arial", 16, "bold"))
                # Habitat
        self.text_nivel_fuel_running = ctk.CTkLabel(self.frame_running, text="Nível de combustível", font=("Arial", 12))
        self.button_fuel_actual = ctk.CTkButton(self.frame_running, text="N/d", fg_color="blue", hover_color="blue")
        self.text_paraquedas_running = ctk.CTkLabel(self.frame_running, text="Paraquedas", font=("Arial", 12))
        self.button_paraquedas_actual = ctk.CTkButton(self.frame_running, text="N/d", fg_color="blue", hover_color="blue")
        self.retrofoguete_habitat = "Funcionando"
        self.text_retrofoguete_running = ctk.CTkLabel(self.frame_running, text="Retrofoguete", font=("Arial", 12))
        self.button_retrofoguete_actual = ctk.CTkButton(self.frame_running, text="N/d", fg_color="blue", hover_color="blue")
        self.text_cc_running = ctk.CTkLabel(self.frame_running, text="Criticidade da carga", font=("Arial", 12))
        self.text_outside_temperature = ctk.CTkLabel(self.frame_running, text="Temperatura externa", font=("Arial", 12))
        self.button_outside_temperature_actual = ctk.CTkButton(self.frame_running, text="N/d")
        self.text_estimated_time_running = ctk.CTkLabel(self.frame_running, text="Tempo estimado de chegada", font=("Arial", 12))
        self.button_estimated_time_actual= ctk.CTkButton(self.frame_running, text="N/d", fg_color="blue", hover_color="blue")
        self.outside_temperature = None
        self.button_cc_actual = ctk.CTkButton(self.frame_running, text="N/d", fg_color="blue", hover_color="blue")

        self.text_nivel_fuel_running.grid(row=2, columnspan=2)
        self.button_fuel_actual.grid(row=3, columnspan=2)
        self.text_paraquedas_running.grid(row=4, columnspan=2)
        self.button_paraquedas_actual.grid(row=5, columnspan=2)
        self.text_retrofoguete_running.grid(row=6, columnspan=2)
        self.button_retrofoguete_actual.grid(row=7, columnspan=2)
        self.text_cc_running.grid(row=8, columnspan=2)
        self.button_cc_actual.grid(row=9, columnspan=2, pady=(0,5))
        self.text_outside_temperature.grid(row=10, columnspan=2)
        self.button_outside_temperature_actual.grid(row=11, columnspan=2)
        self.text_estimated_time_running.grid(row=12, columnspan=2)
        self.button_estimated_time_actual.grid(row=13, columnspan=2, pady=(0,10))



            # Segundo frame
        self.frame_informacoes_pouso = ctk.CTkFrame(self.aba_left, fg_color="transparent")
        self.pouso_habitat = None
        self.pouso_energy = None
        self.pouso_lc = None
        self.pouso_logistic = None
        self.pouso_sm = None
        self.pouso_es = None
        self.modulo_habitat = ctk.CTkLabel(self.frame_informacoes_pouso, text=f"Pouso do módulo de habitat: {self.pouso_habitat}", font=("Arial", 12))
        self.modulo_energy = ctk.CTkLabel(self.frame_informacoes_pouso, text=f"Pouso do módulo de energia: {self.pouso_energy}", font=("Arial", 12))
        self.modulo_lc = ctk.CTkLabel(self.frame_informacoes_pouso, text=f"Pouso do módulo de laboratório científico: {self.pouso_lc}", font=("Arial", 12))
        self.modulo_logistic = ctk.CTkLabel(self.frame_informacoes_pouso, text=f"Pouso do módulo logística: {self.pouso_logistic}", font=("Arial", 12))
        self.modulo_sm = ctk.CTkLabel(self.frame_informacoes_pouso, text=f"Pouso do módulo de suporte médico: {self.pouso_sm}", font=("Arial", 12))
        self.modulo_es = ctk.CTkLabel(self.frame_informacoes_pouso, text=f"Pouso do módulo de estação: {self.pouso_es}", font=("Arial", 12))


                # Energia
        self.fuel_energy = 0
        self.mass_energy = 0
        self.cc_energy = 0
        self.retrofoguete_energy = "Funcionando"
                # Laboratório científico
        self.fuel_lc = 0
        self.mass_lc = 0
        self.cc_lc = 0
        self.retrofoguete_lc = "Funcionando"
                # Logística
        self.fuel_logistic = 0
        self.mass_logistic = 0
        self.cc_logistic = 0
        self.retrofoguete_logistic = "Funcionando"
                # Suporte Médico
        self.fuel_sm = 0
        self.mass_sm = 0
        self.cc_sm = 0
        self.retrofoguete_sm = "Funcionando"
                # Estação
        self.fuel_es = 0
        self.mass_es = 0
        self.cc_es = 0
        self.retrofoguete_es = "Funcionando"

        # Páginas da aba esquerda
        self.pags = [self.frame_priority, self.frame_habitat, self.frame_energy, self.frame_lc, self.frame_logistic, self.frame_sm, self.frame_es, self.frame_running]

        self.pag_actualy = 0
        
        def construir_menu():
            self.pag = self.pags[self.pag_actualy]

            self.pag.grid(row=1, columnspan= 2, padx=(5,5), pady=(5,5), sticky="snwe")
            self.pag.grid_columnconfigure(0, weight=1)
            self.pag.grid_columnconfigure(1, weight=1)
            if self.pag_actualy == 7:
                self.frame_informacoes_pouso.grid(row=6, columnspan=2, sticky="snwe")
            else:
                self.frame_informacoes_pouso.grid_forget()            

        def reset():
            self.indice_modulo = 0
            self.speed = 5500
            self.altitude = 125000
            self.impulso = 0
            self.aceleracao = 0
            self.paraquedas_aberto = False
            self.empuxo_maximo = 100000
            self.pouso_habitat = None
            self.pouso_energy = None
            self.pouso_lc = None
            self.pouso_logistic = None
            self.pouso_sm = None
            self.pouso_es = None
            self.modulo_habitat.pack_forget()
            self.modulo_energy.pack_forget()
            self.modulo_lc.pack_forget()
            self.modulo_logistic.pack_forget()
            self.modulo_sm.pack_forget()
            self.modulo_es.pack_forget()
            self.points = 0
            self.modulos_sucesso = 0
            self.atualizar_retrofoguete(False)
                
        def next_pag():
            try:
                # 1.2.8.1 Habitação
                if self.pag_actualy == 1:
                    self.fuel_habitat = float(self.text_nivel_fuel_habitat_entry.get())
                    self.mass_habitat = float(self.text_mass_habitat_entry.get())
                    self.cc_habitat = self.text_cc_habitat_entry.get()

                    if self.fuel_habitat > 1500:
                        self.box_text_information.configure(text="A quantidade de combustível do módulo não pode ultrapassar 1500 quilogramas")
                        return
                    if self.mass_habitat > 3000 or self.mass_habitat < 100:
                        self.box_text_information.configure(text="A quantidade recomendada de massa do módulo deve estar entre 100 e 3000 quilogramas, sendo fortemente recomendado não passar de 2500 quilogramas para um pouso seguro", wraplength=400)
                        return
                        
                elif self.pag_actualy == 2:
                    # 1.2.8.2 Energia
                    self.fuel_energy = float(self.text_fuel_energy_entry.get())
                    self.mass_energy = float(self.text_mass_energy_entry.get())
                    self.cc_energy = self.text_cc_energy_entry.get()

                    if self.fuel_energy > 1500:
                        self.box_text_information.configure(text="A quantidade de combustível do módulo não pode ultrapassar 1500 quilogramas")
                        return
                    if self.mass_energy > 3000 or self.mass_energy < 100:
                        self.box_text_information.configure(text="A quantidade recomendada de massa do módulo deve estar entre 100 e 3000 quilogramas, sendo fortemente recomendado não passar de 2500 quilogramas para um pouso seguro", wraplength=400)
                        return

                elif self.pag_actualy == 3:
                    # 1.2.8.4 Laboratório científico
                    self.fuel_lc = float(self.text_fuel_lc_entry.get())
                    self.mass_lc = float(self.text_mass_lc_entry.get())
                    self.cc_lc = self.text_cc_lc_entry.get()

                    if self.fuel_lc > 1500:
                        self.box_text_information.configure(text="A quantidade de combustível do módulo não pode ultrapassar 1500 quilogramas")
                        return
                    if self.mass_lc > 3000 or self.mass_lc < 100:
                        self.box_text_information.configure(text="A quantidade recomendada de massa do módulo deve estar entre 100 e 3000 quilogramas, sendo fortemente recomendado não passar de 2500 quilogramas para um pouso seguro", wraplength=400)
                        return
                
                elif self.pag_actualy == 4:
                    # 1.2.8.3 Logística
                    self.fuel_logistic = float(self.text_fuel_logistic_entry.get())
                    self.mass_logistic = float(self.text_mass_logistic_entry.get())
                    self.cc_logistic = self.text_cc_logistic_entry.get()

                    if self.fuel_logistic > 1500:
                        self.box_text_information.configure(text="A quantidade de combustível do módulo não pode ultrapassar 1500 quilogramas")
                        return
                    if self.mass_logistic > 3000 or self.mass_logistic < 100:
                        self.box_text_information.configure(text="A quantidade recomendada de massa do módulo deve estar entre 100 e 3000 quilogramas, sendo fortemente recomendado não passar de 2500 quilogramas para um pouso seguro", wraplength=400)
                        return
                
                elif self.pag_actualy == 5:
                    # 1.2.8.5 Suporte Médico
                    self.fuel_sm = float(self.text_fuel_sm_entry.get())
                    self.mass_sm = float(self.text_mass_sm_entry.get())
                    self.cc_sm = self.text_cc_sm_entry.get()

                    if self.fuel_sm > 1500:
                        self.box_text_information.configure(text="A quantidade de combustível do módulo não pode ultrapassar 1500 quilogramas")
                        return
                    if self.mass_sm > 3000 or self.mass_sm < 100:
                        self.box_text_information.configure(text="A quantidade recomendada de massa do módulo deve estar entre 100 e 3000 quilogramas, sendo fortemente recomendado não passar de 2500 quilogramas para um pouso seguro", wraplength=400)
                        return
                elif self.pag_actualy == 6:
                    # 1.2.8.6 Estação
                    self.fuel_es = float(self.text_fuel_es_entry.get())
                    self.mass_es = float(self.text_mass_es_entry.get())
                    self.cc_es = self.text_cc_es_entry.get()

                    if self.fuel_es > 1500:
                        self.box_text_information.configure(text="A quantidade de combustível do módulo não pode ultrapassar 1500 quilogramas")
                        return
                    if self.mass_es > 3000 or self.mass_es < 100:
                        self.box_text_information.configure(text="A quantidade recomendada de massa do módulo deve estar entre 100 e 3000 quilogramas, sendo fortemente recomendado não passar de 2500 quilogramas para um pouso seguro", wraplength=400)
                        return
            except:
                self.box_text_information.configure(text="Preencha os campos com algum valor")
                return
            if self.pag_actualy < 6:
                self.pag.grid_forget()
                self.box_text_information.configure(text="")
                self.button_previous_pag.configure(state="")
                self.pag_actualy += 1
                self.button_next_pag.configure(state="enabled")
                construir_menu()

            if self.pag_actualy == 6:
                self.button_next_pag.configure(state="disabled")
                self.button_start.configure(state="enabled")



        def previous_pag():
            if self.pag_actualy > 0:
                self.pag.grid_forget()
                self.pag_actualy -= 1
                self.button_next_pag.configure(state="enabled")
                self.button_start.configure(state="disabled")
                construir_menu()
            if self.pag_actualy == 0:
                self.button_previous_pag.configure(state="disabled")

        # Botões de Próxima página
        self.button_next_pag = ctk.CTkButton(self.aba_left, text="Próxima página", command=next_pag)
        self.button_next_pag.grid(row=4, column=1,padx=(5,10), sticky="w")
        self.button_previous_pag = ctk.CTkButton(self.aba_left, text="Voltar página", command=previous_pag, state="disabled")
        self.button_previous_pag.grid(row=4, column=0,padx=(10,5), sticky="e")

        construir_menu()

        

        self.circle = 0
        self.modules_name = [self.text_box_habitat, self.text_box_energy, self.text_box_lc, self.text_box_logistic, self.text_box_sm, self.text_box_es]

        self.speed = 5500
        self.altitude = 125000
        self.impulso = 0
        self.aceleracao = 0
        self.paraquedas_aberto = False
        self.empuxo_maximo = 100000
        self.modulos_pouso = f"{self.frames_priority[0]}"
        self.points = 0
        self.modulos_sucesso = 0


        def calcular_consumo(empuxo, tempo, impulso_especifico):
            if empuxo <= 0 or tempo <= 0 or impulso_especifico <= 0:
                return 0.0

            gravidade_padrao = 3.71  # m/s²

            consumo = (
                empuxo * tempo
                / (impulso_especifico * gravidade_padrao)
            )

            return consumo

        def calcular_frenagem(altitude, velocidade, massa, empuxo):
            gravidade = 3.71

            if massa <= 0 or empuxo <= 0:
                return False

            # Desaceleração disponível com o motor ligado
            desaceleracao = empuxo / massa - gravidade

            # O motor precisa conseguir vencer a gravidade
            if desaceleracao <= 0:
                return False

            # Distância teórica necessária para parar
            distancia_frenagem = velocidade**2 / (2 * desaceleracao)

            # Margem de segurança de 20%
            distancia_segura = distancia_frenagem * 1.5

            return altitude <= distancia_segura

        def calcular_densidade(altitude):
            densidade_superficie = 0.020  # kg/m³
            escala_altura = 11100         # metros

            return densidade_superficie * math.exp(
                -max(0, altitude) / escala_altura
            )

        def calcular_aceleracao(massa, velocidade, impulso, densidade, paraquedas_aberto):
            gravidade = 3.71
            area = 10.0
            coeficiente_arrasto = 1.0

            if paraquedas_aberto:
                area = 100.0
                coeficiente_arrasto = 1.5

            arrasto = (
                0.5
                * densidade
                * velocidade**2
                * coeficiente_arrasto
                * area
            )

            aceleracao = gravidade - (arrasto + impulso) / massa

            return aceleracao

        def estimar_tempo_pouso(altitude, velocidade, massa, combustivel, empuxo_maximo, paraquedas_aberto):
            gravidade = 3.71
            dt = 0.1
            tempo = 0.0

            # Cópias dos valores para não alterar a simulação real
            h = altitude
            v = velocidade
            fuel = combustivel
            paraquedas = paraquedas_aberto

            # Evita uma simulação infinita
            tempo_maximo = 3600

            while h > 0 and tempo < tempo_maximo:
                densidade = calcular_densidade(h)

                impulso = 0

                # Estima quando o retrofoguete precisa começar a frear
                if fuel > 0 and calcular_frenagem(
                    h, v, massa, empuxo_maximo
                ):
                    impulso = empuxo_maximo

                # Calcula o consumo de combustível
                consumo = calcular_consumo(impulso, dt, 300)
                fuel = max(0, fuel - consumo)

                if fuel <= 0:
                    impulso = 0

                # Calcula a aceleração
                aceleracao = calcular_aceleracao(
                    massa,
                    v,
                    impulso,
                    densidade,
                    paraquedas
                )

                velocidade_anterior = v

                # Atualiza velocidade e altitude
                v = max(0, v + aceleracao * dt)

                velocidade_media = (velocidade_anterior + v) / 2
                h = max(0, h - velocidade_media * dt)

                # Abre o paraquedas na altitude definida
                if h <= 12000:
                    paraquedas = True

                tempo += dt

            if h > 0:
                return None

            return tempo

        def calcular_temperatura_externa(altitude):
            temperatura_superficie = -63  # °C
            variacao_por_km = -1.0         # °C por km

            altitude_km = altitude / 1000

            temperatura = temperatura_superficie + (variacao_por_km * altitude_km)

            return temperatura
        

        def simulation():
                self.ordem_pouso = self.frames_priority.copy()
                self.cronometro()
                landing()
                self.circle += 1
                
        def landing():
            modulo = self.ordem_pouso[self.indice_modulo]
            nome = self.labels_modulos[modulo].cget("text")

            self.caption_running.configure(text=f"Módulo: {nome}")
            self.caption_running.grid(row=0, columnspan=2)

            if nome == "Habitação":
                if self.fuel_habitat < 100:
                    self.button_fuel_actual.configure(text=self.fuel_habitat, fg_color="red", hover_color="red")
                elif self.fuel_habitat < 500 and self.fuel_habitat >= 100:
                    self.button_fuel_actual.configure(text=self.fuel_habitat, fg_color="darkorange", hover_color="darkorange")
                else:
                    self.button_fuel_actual.configure(text=self.fuel_habitat, fg_color="green", hover_color="green")
                self.button_retrofoguete_actual.configure(text=self.retrofoguete_habitat)
                self.button_cc_actual.configure(text=self.cc_habitat)

                if self.paraquedas_aberto == True:
                    self.button_paraquedas_actual.configure(text="Aberto", fg_color="green", hover_color="green")
                else:
                    self.button_paraquedas_actual.configure(text="Fechado", fg_color="blue", hover_color="blue")

                dt = 0.1
                gravidade = 3.71

                densidade = calcular_densidade(self.altitude)
                dt = 0.1  # intervalo de simulação em segundos

                consumo = calcular_consumo(
                    self.impulso,
                    dt,
                    300
                )
                self.fuel_habitat = max(
                    0.0,
                    self.fuel_habitat - consumo
                )
                self.button_fuel_actual.configure(
                    text=f"{self.fuel_habitat:.2f} kg"
                )
                # Calcula a frenagem necessária antes de calcular a aceleração.
                # O motor só consegue frear se o empuxo superar o peso.
                self.impulso = 0

                if calcular_frenagem(
                    self.altitude,
                    self.speed,
                    self.mass_habitat,
                    self.empuxo_maximo
                ):
                    self.impulso = self.empuxo_maximo

                
                if self.fuel_habitat > 0:
                    self.impulso = min(
                        self.impulso,
                        self.empuxo_maximo
                    )
                    if self.impulso == 0:
                        self.retrofoguete_habitat = "Desligado"
                        self.button_retrofoguete_actual.configure(fg_color="blue", hover_color="blue")
                    else:
                        self.retrofoguete_habitat = "Funcionando"
                        self.button_retrofoguete_actual.configure(fg_color="green", hover_color="green")
                else:
                    self.impulso = 0
                    self.retrofoguete_habitat = "Sem combustível"
                    self.button_retrofoguete_actual.configure(fg_color="darkred", hover_color="darkred")

                # Calcula a aceleração considerando o motor e o arrasto.
                self.aceleracao = calcular_aceleracao(
                    self.mass_habitat,
                    self.speed,
                    self.impulso,
                    densidade,
                    self.paraquedas_aberto
                )

                velocidade_anterior = self.speed

                # Atualiza a velocidade.
                self.speed = max(
                    0.0,
                    self.speed + self.aceleracao * dt
                )

                # Atualiza a altitude usando a velocidade média.
                velocidade_media = (
                    velocidade_anterior + self.speed
                ) / 2

                self.altitude = max(
                    0.0,
                    self.altitude - velocidade_media * dt
                )

                self.atualizar_nave()

                # Abre o paraquedas abaixo de 12 km.
                if self.altitude <= 12000:
                    self.paraquedas_aberto = True

                self.atualizar_paraquedas()

                tempo = estimar_tempo_pouso(
                    self.altitude,
                    self.speed,
                    self.mass_habitat,
                    self.fuel_habitat,
                    self.empuxo_maximo,
                    self.paraquedas_aberto
                )

                if tempo is None:
                    texto_tempo = "indeterminado"
                else:
                    minutos = int(tempo // 60)
                    segundos = int(tempo % 60)

                    texto_tempo = (
                        f"{minutos}:{segundos}"
                    )

                self.button_estimated_time_actual.configure(text=texto_tempo)

                self.outside_temperature = calcular_temperatura_externa(self.altitude)
                self.button_outside_temperature_actual.configure(text=f"{self.outside_temperature:.2f} ℃")

                self.speed_visualizador.configure(text=f"Velocidade: {self.speed:.2f} m/s")
                self.aceleracao_visulizador.configure(text=f"Aceleração: {self.aceleracao:.2f} m/s²")
                self.altitude_visulizador.configure(text=f"Altitude: {self.altitude:.2f} metros")
                self.empuxo_visualizador.configure(text=f"Empuxo: {self.impulso:.2f} N")
                self.atualizar_retrofoguete(self.impulso > 0)
                
            elif nome == "Energia":
                if self.fuel_energy < 100:
                    self.button_fuel_actual.configure(text=self.fuel_energy, fg_color="red", hover_color="red")
                elif self.fuel_energy < 500 and self.fuel_energy >= 100:
                    self.button_fuel_actual.configure(text=self.fuel_energy, fg_color="darkorange", hover_color="darkorange")
                else:
                    self.button_fuel_actual.configure(text=self.fuel_energy, fg_color="green", hover_color="green")
                self.button_retrofoguete_actual.configure(text=self.retrofoguete_energy)
                self.button_cc_actual.configure(text=self.cc_energy)

                if self.paraquedas_aberto == True:
                    self.button_paraquedas_actual.configure(text="Aberto", fg_color="green", hover_color="green")
                else:
                    self.button_paraquedas_actual.configure(text="Fechado", fg_color="blue", hover_color="blue")

                dt = 0.1
                gravidade = 3.71

                densidade = calcular_densidade(self.altitude)
                dt = 0.1  # intervalo de simulação em segundos

                consumo = calcular_consumo(
                    self.impulso,
                    dt,
                    300
                )
                self.fuel_energy = max(
                    0.0,
                    self.fuel_energy - consumo
                )
                self.button_fuel_actual.configure(
                    text=f"{self.fuel_energy:.2f} kg"
                )
                # Calcula a frenagem necessária antes de calcular a aceleração.
                # O motor só consegue frear se o empuxo superar o peso.
                self.impulso = 0

                if calcular_frenagem(
                    self.altitude,
                    self.speed,
                    self.mass_energy,
                    self.empuxo_maximo
                ):
                    self.impulso = self.empuxo_maximo

                if self.fuel_energy > 0:
                    self.impulso = min(
                        self.impulso,
                        self.empuxo_maximo
                    )
                    if self.impulso == 0:
                        self.retrofoguete_energy = "Desligado"
                        self.button_retrofoguete_actual.configure(fg_color="blue", hover_color="blue")
                    else:
                        self.retrofoguete_energy = "Funcionando"
                        self.button_retrofoguete_actual.configure(fg_color="green", hover_color="green")
                else:
                    self.impulso = 0
                    self.retrofoguete_energy = "Sem combustível"
                    self.button_retrofoguete_actual.configure(fg_color="darkred", hover_color="darkred")

                # Calcula a aceleração considerando o motor e o arrasto.
                self.aceleracao = calcular_aceleracao(
                    self.mass_energy,
                    self.speed,
                    self.impulso,
                    densidade,
                    self.paraquedas_aberto
                )

                velocidade_anterior = self.speed

                # Atualiza a velocidade.
                self.speed = max(
                    0.0,
                    self.speed + self.aceleracao * dt
                )

                # Atualiza a altitude usando a velocidade média.
                velocidade_media = (
                    velocidade_anterior + self.speed
                ) / 2

                self.altitude = max(
                    0.0,
                    self.altitude - velocidade_media * dt
                )

                self.atualizar_nave()

                # Abre o paraquedas abaixo de 12 km.
                if self.altitude <= 12000:
                    self.paraquedas_aberto = True

                self.atualizar_paraquedas()

                tempo = estimar_tempo_pouso(
                    self.altitude,
                    self.speed,
                    self.mass_energy,
                    self.fuel_energy,
                    self.empuxo_maximo,
                    self.paraquedas_aberto
                )

                if tempo is None:
                    texto_tempo = "indeterminado"
                else:
                    minutos = int(tempo // 60)
                    segundos = int(tempo % 60)

                    texto_tempo = (
                        f"{minutos}:{segundos}"
                    )

                self.button_estimated_time_actual.configure(text=texto_tempo)

                self.outside_temperature = calcular_temperatura_externa(self.altitude)
                self.button_outside_temperature_actual.configure(text=f"{self.outside_temperature:.2f} ℃")

                self.speed_visualizador.configure(text=f"Velocidade: {self.speed:.2f} m/s")
                self.aceleracao_visulizador.configure(text=f"Aceleração: {self.aceleracao:.2f} m/s²")
                self.altitude_visulizador.configure(text=f"Altitude: {self.altitude:.2f} metros")
                self.empuxo_visualizador.configure(text=f"Empuxo: {self.impulso:.2f} N")

            elif nome == "Laboratório científico":
                if self.fuel_lc < 100:
                    self.button_fuel_actual.configure(text=self.fuel_lc, fg_color="red", hover_color="red")
                elif self.fuel_lc < 500 and self.fuel_lc >= 100:
                    self.button_fuel_actual.configure(text=self.fuel_lc, fg_color="darkorange", hover_color="darkorange")
                else:
                    self.button_fuel_actual.configure(text=self.fuel_lc, fg_color="green", hover_color="green")
                self.button_retrofoguete_actual.configure(text=self.retrofoguete_lc)
                self.button_cc_actual.configure(text=self.cc_lc)

                if self.paraquedas_aberto == True:
                    self.button_paraquedas_actual.configure(text="Aberto", fg_color="green", hover_color="green")
                else:
                    self.button_paraquedas_actual.configure(text="Fechado", fg_color="blue", hover_color="blue")

                dt = 0.1
                gravidade = 3.71

                densidade = calcular_densidade(self.altitude)
                dt = 0.1  # intervalo de simulação em segundos

                consumo = calcular_consumo(
                    self.impulso,
                    dt,
                    300
                )
                self.fuel_lc = max(
                    0.0,
                    self.fuel_lc - consumo
                )
                self.button_fuel_actual.configure(
                    text=f"{self.fuel_lc:.2f} kg"
                )
                # Calcula a frenagem necessária antes de calcular a aceleração.
                # O motor só consegue frear se o empuxo superar o peso.
                self.impulso = 0

                if calcular_frenagem(
                    self.altitude,
                    self.speed,
                    self.mass_lc,
                    self.empuxo_maximo
                ):
                    self.impulso = self.empuxo_maximo

                if self.fuel_lc > 0:
                    self.impulso = min(
                        self.impulso,
                        self.empuxo_maximo
                    )
                    if self.impulso == 0:
                        self.retrofoguete_lc = "Desligado"
                        self.button_retrofoguete_actual.configure(fg_color="blue", hover_color="blue")
                    else:
                        self.retrofoguete_lc = "Funcionando"
                        self.button_retrofoguete_actual.configure(fg_color="green", hover_color="green")
                else:
                    self.impulso = 0
                    self.retrofoguete_lc = "Sem combustível"
                    self.button_retrofoguete_actual.configure(fg_color="darkred", hover_color="darkred")

                # Calcula a aceleração considerando o motor e o arrasto.
                self.aceleracao = calcular_aceleracao(
                    self.mass_lc,
                    self.speed,
                    self.impulso,
                    densidade,
                    self.paraquedas_aberto
                )

                velocidade_anterior = self.speed

                # Atualiza a velocidade.
                self.speed = max(
                    0.0,
                    self.speed + self.aceleracao * dt
                )

                # Atualiza a altitude usando a velocidade média.
                velocidade_media = (
                    velocidade_anterior + self.speed
                ) / 2

                self.altitude = max(
                    0.0,
                    self.altitude - velocidade_media * dt
                )

                self.atualizar_nave()

                # Abre o paraquedas abaixo de 12 km.
                if self.altitude <= 12000:
                    self.paraquedas_aberto = True

                self.atualizar_paraquedas()

                tempo = estimar_tempo_pouso(
                    self.altitude,
                    self.speed,
                    self.mass_lc,
                    self.fuel_lc,
                    self.empuxo_maximo,
                    self.paraquedas_aberto
                )

                if tempo is None:
                    texto_tempo = "indeterminado"
                else:
                    minutos = int(tempo // 60)
                    segundos = int(tempo % 60)

                    texto_tempo = (
                        f"{minutos}:{segundos}"
                    )

                self.button_estimated_time_actual.configure(text=texto_tempo)

                self.outside_temperature = calcular_temperatura_externa(self.altitude)
                self.button_outside_temperature_actual.configure(text=f"{self.outside_temperature:.2f} ℃")
                
                self.speed_visualizador.configure(text=f"Velocidade: {self.speed:.2f} m/s")
                self.aceleracao_visulizador.configure(text=f"Aceleração: {self.aceleracao:.2f} m/s²")
                self.altitude_visulizador.configure(text=f"Altitude: {self.altitude:.2f} metros")
                self.empuxo_visualizador.configure(text=f"Empuxo: {self.impulso:.2f} N")

            elif nome == "Logística":
                if self.fuel_logistic < 100:
                    self.button_fuel_actual.configure(text=self.fuel_logistic, fg_color="red", hover_color="red")
                elif self.fuel_logistic < 500 and self.fuel_logistic >= 100:
                    self.button_fuel_actual.configure(text=self.fuel_logistic, fg_color="darkorange", hover_color="darkorange")
                else:
                    self.button_fuel_actual.configure(text=self.fuel_logistic, fg_color="green", hover_color="green")
                self.button_retrofoguete_actual.configure(text=self.retrofoguete_logistic)
                self.button_cc_actual.configure(text=self.cc_logistic)

                if self.paraquedas_aberto == True:
                    self.button_paraquedas_actual.configure(text="Aberto", fg_color="green", hover_color="green")
                else:
                    self.button_paraquedas_actual.configure(text="Fechado", fg_color="blue", hover_color="blue")

                dt = 0.1
                gravidade = 3.71

                densidade = calcular_densidade(self.altitude)
                dt = 0.1  # intervalo de simulação em segundos

                consumo = calcular_consumo(
                    self.impulso,
                    dt,
                    300
                )
                self.fuel_logistic = max(
                    0.0,
                    self.fuel_logistic - consumo
                )
                self.button_fuel_actual.configure(
                    text=f"{self.fuel_logistic:.2f} kg"
                )
                # Calcula a frenagem necessária antes de calcular a aceleração.
                # O motor só consegue frear se o empuxo superar o peso.
                self.impulso = 0

                if calcular_frenagem(
                    self.altitude,
                    self.speed,
                    self.mass_logistic,
                    self.empuxo_maximo
                ):
                    self.impulso = self.empuxo_maximo

                if self.fuel_logistic > 0:
                    self.impulso = min(
                        self.impulso,
                        self.empuxo_maximo
                    )
                    if self.impulso == 0:
                        self.retrofoguete_logistic = "Desligado"
                        self.button_retrofoguete_actual.configure(fg_color="blue", hover_color="blue")
                    else:
                        self.retrofoguete_logistic = "Funcionando"
                        self.button_retrofoguete_actual.configure(fg_color="green", hover_color="green")
                else:
                    self.impulso = 0
                    self.retrofoguete_logistic = "Sem combustível"
                    self.button_retrofoguete_actual.configure(fg_color="darkred", hover_color="darkred")

                # Calcula a aceleração considerando o motor e o arrasto.
                self.aceleracao = calcular_aceleracao(
                    self.mass_logistic,
                    self.speed,
                    self.impulso,
                    densidade,
                    self.paraquedas_aberto
                )

                velocidade_anterior = self.speed

                # Atualiza a velocidade.
                self.speed = max(
                    0.0,
                    self.speed + self.aceleracao * dt
                )

                # Atualiza a altitude usando a velocidade média.
                velocidade_media = (
                    velocidade_anterior + self.speed
                ) / 2

                self.altitude = max(
                    0.0,
                    self.altitude - velocidade_media * dt
                )

                self.atualizar_nave()

                # Abre o paraquedas abaixo de 12 km.
                if self.altitude <= 12000:
                    self.paraquedas_aberto = True

                self.atualizar_paraquedas()

                tempo = estimar_tempo_pouso(
                    self.altitude,
                    self.speed,
                    self.mass_logistic,
                    self.fuel_logistic,
                    self.empuxo_maximo,
                    self.paraquedas_aberto
                )

                if tempo is None:
                    texto_tempo = "indeterminado"
                else:
                    minutos = int(tempo // 60)
                    segundos = int(tempo % 60)

                    texto_tempo = (
                        f"{minutos}:{segundos}"
                    )

                self.button_estimated_time_actual.configure(text=texto_tempo)

                self.outside_temperature = calcular_temperatura_externa(self.altitude)
                self.button_outside_temperature_actual.configure(text=f"{self.outside_temperature:.2f} ℃")

                self.speed_visualizador.configure(text=f"Velocidade: {self.speed:.2f} m/s")
                self.aceleracao_visulizador.configure(text=f"Aceleração: {self.aceleracao:.2f} m/s²")
                self.altitude_visulizador.configure(text=f"Altitude: {self.altitude:.2f} metros")
                self.empuxo_visualizador.configure(text=f"Empuxo: {self.impulso:.2f} N")

            elif nome == "Suporte médico":
                if self.fuel_sm < 100:
                    self.button_fuel_actual.configure(text=self.fuel_sm, fg_color="red", hover_color="red")
                elif self.fuel_sm < 500 and self.fuel_sm >= 100:
                    self.button_fuel_actual.configure(text=self.fuel_sm, fg_color="darkorange", hover_color="darkorange")
                else:
                    self.button_fuel_actual.configure(text=self.fuel_sm, fg_color="green", hover_color="green")
                self.button_retrofoguete_actual.configure(text=self.retrofoguete_sm)
                self.button_cc_actual.configure(text=self.cc_sm)

                if self.paraquedas_aberto == True:
                    self.button_paraquedas_actual.configure(text="Aberto", fg_color="green", hover_color="green")
                else:
                    self.button_paraquedas_actual.configure(text="Fechado", fg_color="blue", hover_color="blue")

                dt = 0.1
                gravidade = 3.71

                densidade = calcular_densidade(self.altitude)
                dt = 0.1  # intervalo de simulação em segundos

                consumo = calcular_consumo(
                    self.impulso,
                    dt,
                    300
                )
                self.fuel_sm = max(
                    0.0,
                    self.fuel_sm - consumo
                )
                self.button_fuel_actual.configure(
                    text=f"{self.fuel_logistic:.2f} kg"
                )
                # Calcula a frenagem necessária antes de calcular a aceleração.
                # O motor só consegue frear se o empuxo superar o peso.
                self.impulso = 0

                if calcular_frenagem(
                    self.altitude,
                    self.speed,
                    self.mass_sm,
                    self.empuxo_maximo
                ):
                    self.impulso = self.empuxo_maximo

                if self.fuel_sm > 0:
                    self.impulso = min(
                        self.impulso,
                        self.empuxo_maximo
                    )
                    if self.impulso == 0:
                        self.retrofoguete_sm = "Desligado"
                        self.button_retrofoguete_actual.configure(fg_color="blue", hover_color="blue")
                    else:
                        self.retrofoguete_sm = "Funcionando"
                        self.button_retrofoguete_actual.configure(fg_color="green", hover_color="green")
                else:
                    self.impulso = 0
                    self.retrofoguete_sm = "Sem combustível"
                    self.button_retrofoguete_actual.configure(fg_color="darkred", hover_color="darkred")

                # Calcula a aceleração considerando o motor e o arrasto.
                self.aceleracao = calcular_aceleracao(
                    self.mass_sm,
                    self.speed,
                    self.impulso,
                    densidade,
                    self.paraquedas_aberto
                )

                velocidade_anterior = self.speed

                # Atualiza a velocidade.
                self.speed = max(
                    0.0,
                    self.speed + self.aceleracao * dt
                )

                # Atualiza a altitude usando a velocidade média.
                velocidade_media = (
                    velocidade_anterior + self.speed
                ) / 2

                self.altitude = max(
                    0.0,
                    self.altitude - velocidade_media * dt
                )

                self.atualizar_nave()

                # Abre o paraquedas abaixo de 12 km.
                if self.altitude <= 12000:
                    self.paraquedas_aberto = True

                self.atualizar_paraquedas()

                tempo = estimar_tempo_pouso(
                    self.altitude,
                    self.speed,
                    self.mass_sm,
                    self.fuel_sm,
                    self.empuxo_maximo,
                    self.paraquedas_aberto
                )

                if tempo is None:
                    texto_tempo = "indeterminado"
                else:
                    minutos = int(tempo // 60)
                    segundos = int(tempo % 60)

                    texto_tempo = (
                        f"{minutos}:{segundos}"
                    )

                self.button_estimated_time_actual.configure(text=texto_tempo)

                self.outside_temperature = calcular_temperatura_externa(self.altitude)
                self.button_outside_temperature_actual.configure(text=f"{self.outside_temperature:.2f} ℃")

                self.speed_visualizador.configure(text=f"Velocidade: {self.speed:.2f} m/s")
                self.aceleracao_visulizador.configure(text=f"Aceleração: {self.aceleracao:.2f} m/s²")
                self.altitude_visulizador.configure(text=f"Altitude: {self.altitude:.2f} metros")
                self.empuxo_visualizador.configure(text=f"Empuxo: {self.impulso:.2f} N")

            elif nome == "Estação":
                if self.fuel_es < 100:
                    self.button_fuel_actual.configure(text=self.fuel_es, fg_color="red", hover_color="red")
                elif self.fuel_sm < 500 and self.fuel_sm >= 100:
                    self.button_fuel_actual.configure(text=self.fuel_es, fg_color="darkorange", hover_color="darkorange")
                else:
                    self.button_fuel_actual.configure(text=self.fuel_es, fg_color="green", hover_color="green")
                self.button_retrofoguete_actual.configure(text=self.retrofoguete_es)
                self.button_cc_actual.configure(text=self.cc_es)

                if self.paraquedas_aberto == True:
                    self.button_paraquedas_actual.configure(text="Aberto", fg_color="green", hover_color="green")
                else:
                    self.button_paraquedas_actual.configure(text="Fechado", fg_color="blue", hover_color="blue")

                dt = 0.1
                gravidade = 3.71

                densidade = calcular_densidade(self.altitude)
                dt = 0.1  # intervalo de simulação em segundos

                consumo = calcular_consumo(
                    self.impulso,
                    dt,
                    300
                )
                self.fuel_es = max(
                    0.0,
                    self.fuel_es - consumo
                )
                self.button_fuel_actual.configure(
                    text=f"{self.fuel_es:.2f} kg"
                )
                # Calcula a frenagem necessária antes de calcular a aceleração.
                # O motor só consegue frear se o empuxo superar o peso.
                self.impulso = 0

                if calcular_frenagem(
                    self.altitude,
                    self.speed,
                    self.mass_es,
                    self.empuxo_maximo
                ):
                    self.impulso = self.empuxo_maximo

                if self.fuel_es > 0:
                    self.impulso = min(
                        self.impulso,
                        self.empuxo_maximo
                    )
                    if self.impulso == 0:
                        self.retrofoguete_es = "Desligado"
                        self.button_retrofoguete_actual.configure(fg_color="blue", hover_color="blue")
                    else:
                        self.retrofoguete_es = "Funcionando"
                        self.button_retrofoguete_actual.configure(fg_color="green", hover_color="green")
                else:
                    self.impulso = 0
                    self.retrofoguete_es = "Sem combustível"
                    self.button_retrofoguete_actual.configure(fg_color="darkred", hover_color="darkred")

                # Calcula a aceleração considerando o motor e o arrasto.
                self.aceleracao = calcular_aceleracao(
                    self.mass_es,
                    self.speed,
                    self.impulso,
                    densidade,
                    self.paraquedas_aberto
                )

                velocidade_anterior = self.speed

                # Atualiza a velocidade.
                self.speed = max(
                    0.0,
                    self.speed + self.aceleracao * dt
                )

                # Atualiza a altitude usando a velocidade média.
                velocidade_media = (
                    velocidade_anterior + self.speed
                ) / 2

                self.altitude = max(
                    0.0,
                    self.altitude - velocidade_media * dt
                )

                self.atualizar_nave()

                # Abre o paraquedas abaixo de 12 km.
                if self.altitude <= 12000:
                    self.paraquedas_aberto = True

                self.atualizar_paraquedas()

                tempo = estimar_tempo_pouso(
                    self.altitude,
                    self.speed,
                    self.mass_es,
                    self.fuel_es,
                    self.empuxo_maximo,
                    self.paraquedas_aberto
                )

                if tempo is None:
                    texto_tempo = "indeterminado"
                else:
                    minutos = int(tempo // 60)
                    segundos = int(tempo % 60)

                    texto_tempo = (
                        f"{minutos}:{segundos}"
                    )

                self.button_estimated_time_actual.configure(text=texto_tempo)

                self.outside_temperature = calcular_temperatura_externa(self.altitude)
                self.button_outside_temperature_actual.configure(text=f"{self.outside_temperature:.2f} ℃")

                self.speed_visualizador.configure(text=f"Velocidade: {self.speed:.2f} m/s")
                self.aceleracao_visulizador.configure(text=f"Aceleração: {self.aceleracao:.2f} m/s²")
                self.altitude_visulizador.configure(text=f"Altitude: {self.altitude:.2f} metros")
                self.empuxo_visualizador.configure(text=f"Empuxo: {self.impulso:.2f} N")

            if self.altitude <= 0:
                self.altitude = 0
                self.caption_running.grid_forget()

                if self.speed <= 1.0:
                    if nome == "Habitação":
                        self.pouso_habitat = "pouso seguro"
                        self.modulo_habitat.configure(text=f"Pouso do módulo de habitat: {self.pouso_habitat}")
                        self.modulo_habitat.pack(padx=(5,5))
                    elif nome == "Energia":
                        self.pouso_energy = "pouso seguro"
                        self.modulo_energy.configure(text=f"Pouso do módulo de energia: {self.pouso_energy}")
                        self.modulo_energy.pack(padx=(5,5))
                    elif nome == "Laboratório científico":
                        self.pouso_lc = "pouso seguro"
                        self.modulo_lc.configure(text=f"Pouso do módulo de laboratório científico: {self.pouso_lc}")
                        self.modulo_lc.pack(padx=(5,5))
                    elif nome == "Logística":
                        self.pouso_logistic = "pouso seguro"
                        self.modulo_logistic.configure(text=f"Pouso do módulo logística: {self.pouso_logistic}")
                        self.modulo_logistic.pack(padx=(5,5))
                    elif nome == "Suporte médico":
                        self.pouso_sm = "pouso seguro"
                        self.modulo_sm.configure(text=f"Pouso do módulo de suporte médico: {self.pouso_sm}")
                        self.modulo_sm.pack(padx=(5,5))
                    elif nome == "Estação":
                        self.pouso_es = "pouso seguro"
                        self.modulo_es.configure(text=f"Pouso do módulo de estação: {self.pouso_es}")
                        self.modulo_es.pack(padx=(5,5))

                elif self.speed <= 3.0 and self.speed > 1.0:
                    if nome == "Habitação":
                        self.pouso_habitat = f"Impacto com velocidade de {self.speed:.2f} m/s"
                        self.modulo_habitat.configure(text=f"Pouso do módulo de habitat: {self.pouso_habitat}")
                        self.modulo_habitat.pack(padx=(5,5))
                    elif nome == "Energia":
                        self.pouso_energy = f"Impacto com velocidade de {self.speed:.2f} m/s"
                        self.modulo_energy.configure(text=f"Pouso do módulo de energia: {self.pouso_energy}")
                        self.modulo_energy.pack(padx=(5,5))
                    elif nome == "Laboratório científico":
                        self.pouso_lc = f"Impacto com velocidade de {self.speed:.2f} m/s"
                        self.modulo_lc.configure(text=f"Pouso do módulo de laboratório científico: {self.pouso_lc}")
                        self.modulo_lc.pack(padx=(5,5))
                    elif nome == "Logística":
                        self.pouso_logistic = f"Impacto com velocidade de {self.speed:.2f} m/s"
                        self.modulo_logistic.configure(text=f"Pouso do módulo logística: {self.pouso_logistic}")
                        self.modulo_logistic.pack(padx=(5,5))
                    elif nome == "Suporte médico":
                        self.pouso_sm = f"Impacto com velocidade de {self.speed:.2f} m/s"
                        self.modulo_sm.configure(text=f"Pouso do módulo de suporte médico: {self.pouso_sm}")
                        self.modulo_sm.pack(padx=(5,5))
                    elif nome == "Estação":
                        self.pouso_es = f"Impacto com velocidade de {self.speed:.2f} m/s"
                        self.modulo_es.configure(text=f"Pouso do módulo de estação: {self.pouso_es}")
                        self.modulo_es.pack(padx=(5,5))

                else:
                    if nome == "Habitação":
                        self.pouso_habitat = "carga danificada"
                        self.modulo_habitat.configure(text=f"Pouso do módulo de habitat: {self.pouso_habitat}")
                        self.modulo_habitat.pack(padx=(5,5))
                    elif nome == "Energia":
                        self.pouso_energy = "carga danificada"
                        self.modulo_energy.configure(text=f"Pouso do módulo de energia: {self.pouso_energy}")
                        self.modulo_energy.pack(padx=(5,5))
                    elif nome == "Laboratório científico":
                        self.pouso_lc = "carga danificada"
                        self.modulo_lc.configure(text=f"Pouso do módulo de laboratório científico: {self.pouso_lc}")
                        self.modulo_lc.pack(padx=(5,5))
                    elif nome == "Logística":
                        self.pouso_logistic = "Carga danificada"
                        self.modulo_logistic.configure(text=f"Pouso do módulo logística: {self.pouso_logistic}")
                        self.modulo_logistic.pack(padx=(5,5))
                    elif nome == "Suporte médico":
                        self.pouso_sm = "carga danificada"
                        self.modulo_sm.configure(text=f"Pouso do módulo de suporte médico: {self.pouso_sm}")
                        self.modulo_sm.pack(padx=(5,5))
                    elif nome == "Estação":
                        self.pouso_es = "carga danificada"
                        self.modulo_es.configure(text=f"Pouso do módulo de estação: {self.pouso_es}")
                        self.modulo_es.pack(padx=(5,5))

                self.indice_modulo += 1

                if self.indice_modulo < len(self.ordem_pouso):
                    # Reinicia a descida para o próximo módulo
                    self.speed = 5500
                    self.altitude = 125000
                    self.paraquedas_aberto = False
                    self.reposicionar_nave()
                    self.after(100, landing)


                else:
                    # Baixa
                    if self.cc_habitat == "Baixa" and self.pouso_habitat == "pouso seguro":
                        self.points += 1
                        self.modulos_sucesso += 1

                    if self.cc_energy == "Baixa" and self.pouso_energy == "pouso seguro":
                        self.points += 1
                        self.modulos_sucesso += 1

                    if self.cc_lc == "Baixa" and self.pouso_lc == "pouso seguro":
                        self.points += 1
                        self.modulos_sucesso += 1

                    if self.cc_logistic == "Baixa" and self.pouso_logistic == "pouso seguro":
                        self.points += 1
                        self.modulos_sucesso += 1

                    if self.cc_sm == "Baixa" and self.pouso_sm == "pouso seguro":
                        self.points += 1
                        self.modulos_sucesso += 1

                    if self.cc_es == "Baixa" and self.pouso_es == "pouso seguro":
                        self.points += 1
                        self.modulos_sucesso += 1

                    # Média
                    if self.cc_habitat == "Média" and self.pouso_habitat == "pouso seguro":
                        self.points += 2
                        self.modulos_sucesso += 1

                    if self.cc_energy == "Média" and self.pouso_energy == "pouso seguro":
                        self.points += 2
                        self.modulos_sucesso += 1

                    if self.cc_lc == "Média" and self.pouso_lc == "pouso seguro":
                        self.points += 2
                        self.modulos_sucesso += 1

                    if self.cc_logistic == "Média" and self.pouso_logistic == "pouso seguro":
                        self.points += 2
                        self.modulos_sucesso += 1

                    if self.cc_sm == "Média" and self.pouso_sm == "pouso seguro":
                        self.points += 2
                        self.modulos_sucesso += 1

                    if self.cc_es == "Média" and self.pouso_es == "pouso seguro":
                        self.points += 2
                        self.modulos_sucesso += 1

                    # Alta
                    if self.cc_habitat == "Alta" and self.pouso_habitat == "pouso seguro":
                        self.points += 3
                        self.modulos_sucesso += 1

                    if self.cc_energy == "Alta" and self.pouso_energy == "pouso seguro":
                        self.points += 3
                        self.modulos_sucesso += 1

                    if self.cc_lc == "Alta" and self.pouso_lc == "pouso seguro":
                        self.points += 3
                        self.modulos_sucesso += 1

                    if self.cc_logistic == "Alta" and self.pouso_logistic == "pouso seguro":
                        self.points += 3
                        self.modulos_sucesso += 1

                    if self.cc_sm == "Alta" and self.pouso_sm == "pouso seguro":
                        self.points += 3
                        self.modulos_sucesso += 1

                    if self.cc_es == "Alta" and self.pouso_es == "pouso seguro":
                        self.points += 3
                        self.modulos_sucesso += 1


                    self.box_text_information.configure(text=f"Todos os módulos pousaram! Pela suas configurações de criticidade das cargas e dos resultados dos pousos dos módulos você conseguiu {self.points} pontos, tendo conseguido pousar com sucesso {self.modulos_sucesso} módulos.", wraplength=400)
                    self.after_cancel(self.cronometro_id)
                    self.cronometro_id = None
                    self.landing_id = None
            else:       
                self.landing_id = self.after(100, landing)
                


        # 1.2.10 Função Simulação
        def start():
            try:
                self.fuel_es = float(self.text_fuel_es_entry.get())
                self.mass_es = float(self.text_mass_es_entry.get())
                self.cc_es = self.text_cc_es_entry.get()

            except:
                self.box_text_information.configure(text="Preencha os campos com algum valor")
                return
            # Modificação dos botões de páginas
            reset()
            self.button_stop.configure(state="enabled")
            self.button_start.configure(state="disabled")
            self.button_next_pag.grid_forget()
            self.button_previous_pag.grid_forget()
            # Modficação das pag
            self.pag.grid_forget()
            self.box_text_information.configure(text="")
            self.pag_actualy += 1
            construir_menu()

            simulation()

            
        # 1.2.11 Função para parar a simulação
        def back():
            self.button_stop.configure(state="disabled")
            self.button_start.configure(state="enabled")
            self.button_next_pag.grid(row=4, column=1, padx=(5,10), sticky="w")
            self.button_previous_pag.grid(row=4, column=0,padx=(10,5), sticky="e")
            if self.landing_id is not None:
                self.after_cancel(self.landing_id)
                self.landing_id = None

            self.pag.grid_forget()
            self.box_text_information.configure(text="")
            self.pag_actualy -= 1
            construir_menu()

        # 1.2.12 Botões de iniciar e parar a simulação
            # 1.2.12,1 Botão de iniciar
        self.button_start = ctk.CTkButton(self.aba_left, text="Iniciar", command=start, state="disabled")
        self.button_start.grid(row=3, column=1, padx=(5,10), pady=(10,10), sticky="w")
            # 1.2.12.2 Botão de parar
        self.button_stop = ctk.CTkButton(self.aba_left, text="Parar", command=back, state="disabled")
        self.button_stop.grid(row=3, column=0, padx=(10,5), pady=(10,10), sticky="e")

        # Caixa de texto
        
        self.box_text_information = ctk.CTkLabel(self.aba_left, text="")
        self.box_text_information.grid(row=5, columnspan=2, pady=(5,5))


    def atualizar_nave(self):
        altitude_inicial = 125000
        topo_solo = 340
        altura_nave = 105

        proporcao = 1 - min(
            max(self.altitude, 0) / altitude_inicial, 1
        )

        y_inicial = 10
        y_final = topo_solo - altura_nave
        y = y_inicial + proporcao * (y_final - y_inicial)

        caixa = self.canvas.bbox("nave")

        if caixa:
            deslocamento_y = y - caixa[1]

            self.canvas.move("nave", 0, deslocamento_y)
            self.canvas.move("paraquedas", 0, deslocamento_y)
            self.canvas.move("retro", 0, deslocamento_y)

    def reposicionar_nave(self):
        caixa = self.canvas.bbox("nave")

        if caixa:
            self.canvas.move("nave", 0, 10 - caixa[1])

        caixa_paraquedas = self.canvas.bbox("paraquedas")

        if caixa_paraquedas:
            self.canvas.move("paraquedas", 0, -65 - caixa_paraquedas[1])

        caixa_retro = self.canvas.bbox("retro")

        if caixa_retro:
            self.canvas.move("retro", 0, 10 - caixa_retro[1])

        self.atualizar_paraquedas()
        self.atualizar_retrofoguete(False)

    def atualizar_paraquedas(self):
        if self.paraquedas_aberto:
            self.canvas.itemconfigure("paraquedas", state="normal")
        else:
            self.canvas.itemconfigure("paraquedas", state="hidden")

    def atualizar_retrofoguete(self, ligado):
        estado = "normal" if ligado else "hidden"
        self.canvas.itemconfigure("retro", state=estado)

    def cronometro(self):
        self.tempo_total += 1
        self.minutos = self.tempo_total // 60
        self.segundos = self.tempo_total % 60
        self.time_total_visualizador.configure(text=f"Tempo: {self.minutos:02d}:{self.segundos:02d}")

        self.cronometro_id = self.after(1000, self.cronometro)
    
    # 1.3 Função que cria aba direita do programa
    def construir_aba_right(self):
        self.title_aba_right = ctk.CTkLabel(self.aba_right, text="Visualizador", font=("Arial", 20,"bold"))
        self.title_aba_right.grid(row=0, columnspan=2, sticky="we",padx=10, pady=10)
        self.aba_right.grid_columnconfigure(0, weight=1)

        # Frame - Visualizador
        self.frame_visualizador = ctk.CTkFrame(self.aba_right)
        self.frame_visualizador.grid(row=1, columnspan=2, pady=(5,5), sticky="we")
        # Área de desenho
        self.canvas = ctk.CTkCanvas(
            self.frame_visualizador,
            width=380,
            height=400,
            bg="#1b1b2f",
            highlightthickness=0
        )
        self.canvas.pack(padx=5, pady=5)

        # Solo de Marte
        self.canvas.create_rectangle(
            0, 340, 380, 400,
            fill="#8C3F2B",
            outline=""
        )

        # Pedras no solo
        for x, y, tamanho in [
            (25, 365, 5), (70, 385, 4),
            (290, 370, 6), (345, 390, 5)
        ]:
            self.canvas.create_oval(
                x, y, x + tamanho * 2, y + tamanho,
                fill="#603025",
                outline=""
            )

        # Chamas dos retrofoguetes (atrás das pernas)
        self.canvas.create_polygon(
            125, 85, 140, 85, 132, 112,
            fill="#FF9F43",
            outline="#FFD166",
            tags="retro"
        )

        self.canvas.create_polygon(
            180, 85, 195, 85, 187, 112,
            fill="#FF9F43",
            outline="#FFD166",
            tags="retro"
        )

        # Pernas do módulo
        self.canvas.create_line(
            125, 65, 105, 100, 85, 105,
            fill="#AAB7C4", width=5,
            tags="nave"
        )

        self.canvas.create_line(
            195, 65, 215, 100, 235, 105,
            fill="#AAB7C4", width=5,
            tags="nave"
        )

        # Pés de pouso
        self.canvas.create_line(
            75, 105, 95, 105,
            fill="#E0E6ED", width=5,
            tags="nave"
        )

        self.canvas.create_line(
            225, 105, 245, 105,
            fill="#E0E6ED", width=5,
            tags="nave"
        )

        # Corpo principal
        self.canvas.create_rectangle(
            115, 35, 205, 85,
            fill="#596675",
            outline="#D8E1EA",
            width=2,
            tags="nave"
        )

        # Painel frontal
        self.canvas.create_rectangle(
            125, 43, 195, 77,
            fill="#354454",
            outline="#8193A5",
            width=1,
            tags="nave"
        )

        # Parte superior
        self.canvas.create_polygon(
            115, 35,
            130, 15,
            190, 15,
            205, 35,
            fill="#8795A5",
            outline="#E0E6ED",
            width=2,
            tags="nave"
        )

        # Janela central
        self.canvas.create_oval(
            148, 43, 172, 67,
            fill="#36C5F0",
            outline="#B8F2FF",
            width=2,
            tags="nave"
        )

        # Reflexo da janela
        self.canvas.create_oval(
            153, 46, 160, 53,
            fill="#D7FAFF",
            outline="",
            tags="nave"
        )

        # Luzes de status
        self.canvas.create_oval(
            130, 48, 137, 55,
            fill="#55E6A5",
            outline="",
            tags="nave"
        )

        self.canvas.create_oval(
            183, 48, 190, 55,
            fill="#FFB454",
            outline="",
            tags="nave"
        )

        # Antena
        self.canvas.create_line(
            160, 15, 160, 5,
            fill="#D8E1EA",
            width=2,
            tags="nave"
        )

        self.canvas.create_oval(
            156, 1, 164, 9,
            fill="#36C5F0",
            outline="",
            tags="nave"
        )

        # Detalhes laterais
        self.canvas.create_line(
            132, 72, 143, 72,
            fill="#36C5F0",
            width=2,
            tags="nave"
        )

        self.canvas.create_line(
            177, 72, 188, 72,
            fill="#36C5F0",
            width=2,
            tags="nave"
        )

        # Cúpula do paraquedas
        self.canvas.create_arc(
            105, -65, 215, 45,
            start=0,
            extent=180,
            style="pieslice",
            fill="#E74C3C",
            outline="#FFD6D2",
            width=2,
            tags=("paraquedas",)
        )

        # Divisões da cúpula
        self.canvas.create_line(
            160, -65, 160, 0,
            fill="#FFD6D2",
            width=2,
            tags=("paraquedas",)
        )

        self.canvas.create_line(
            125, -50, 145, 0,
            fill="#FFD6D2",
            width=2,
            tags=("paraquedas",)
        )

        self.canvas.create_line(
            195, -50, 175, 0,
            fill="#FFD6D2",
            width=2,
            tags=("paraquedas",)
        )

        # Cordas do paraquedas
        self.canvas.create_line(
            115, 0, 130, 35,
            fill="#D8E1EA",
            width=2,
            tags=("paraquedas",)
        )

        self.canvas.create_line(
            205, 0, 190, 35,
            fill="#D8E1EA",
            width=2,
            tags=("paraquedas",)
        )

        self.canvas.create_line(
            160, 0, 160, 35,
            fill="#D8E1EA",
            width=2,
            tags=("paraquedas",)
        )

        # Começa fechado
        self.canvas.itemconfigure("paraquedas", state="hidden")

        # Resto
        self.time_total_visualizador = ctk.CTkLabel(self.aba_right, text=f"Tempo: 00:00")
        self.time_total_visualizador.grid(row=2, columnspan=2)
        # Configura o espaço das duas colunas
        self.aba_right.grid_columnconfigure((0, 1), weight=1, uniform="colunas")

        self.speed_visualizador = ctk.CTkLabel(
            self.aba_right,
            text=f"Velocidade: {self.speed:.2f} m/s",
            anchor="w"
        )
        self.speed_visualizador.grid(
            row=3, column=0, padx=20, pady=5, sticky="ew"
        )

        self.aceleracao_visulizador = ctk.CTkLabel(
            self.aba_right,
            text=f"Aceleração: {self.aceleracao:.2f} m/s²",
            anchor="w"
        )
        self.aceleracao_visulizador.grid(
            row=3, column=1, padx=10, pady=5, sticky="ew"
        )

        self.altitude_visulizador = ctk.CTkLabel(
            self.aba_right,
            text=f"Altitude: {self.altitude:.2f} metros",
            anchor="w"
        )
        self.altitude_visulizador.grid(
            row=4, column=0, padx=20, pady=5, sticky="ew"
        )

        self.empuxo_visualizador = ctk.CTkLabel(
            self.aba_right,
            text=f"Empuxo: {self.impulso:.2f} N",
            anchor="w"
        )
        self.empuxo_visualizador.grid(
            row=4, column=1, padx=10, pady=5, sticky="ew"
        )


        
window = Aplicativo()
window.mainloop()
