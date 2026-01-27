Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.

Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.

Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.

Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().

Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.

Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?

Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.