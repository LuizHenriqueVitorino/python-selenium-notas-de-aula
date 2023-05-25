Funcionalidade: Login no sistema

    Cenário: Logar no sistema com sucesso
        Dado que eu esteja na tela de login do sistema
        Quando o usuário digita seu username
            | input     | entrada       |
            | username  | standard_user |
        E digita sua senha
        E clica em submit
        Então o usuário deve estar logado