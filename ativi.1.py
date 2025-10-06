class Filme:
    def __init__(self, titulo, duracao, ingressos_disponiveis):
        self.titulo = titulo
        self.duracao = duracao  # em minutos
        self._ingressos_disponiveis = ingressos_disponiveis  # atributo protegido

    # Getter: permite acessar ingressos_disponiveis
    @property
    def ingressos_disponiveis(self):
        return self._ingressos_disponiveis

    # Setter: controla como alterar ingressos_disponiveis
    @ingressos_disponiveis.setter
    def ingressos_disponiveis(self, valor):
        if valor < 0:
            print(f"Não é possível definir ingressos negativos para {self.titulo}!")
        else:
            self._ingressos_disponiveis = valor
