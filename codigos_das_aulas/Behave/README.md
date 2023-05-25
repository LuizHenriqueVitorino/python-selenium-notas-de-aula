# Aula Behave

Bem-vindo à pasta da aula Behave! Neste repositório, você encontrará recursos e informações sobre como usar o framework Behave para automação de testes.

## Instalação

Certifique-se de ter o Python instalado no seu sistema antes de prosseguir com a instalação do Behave.

1. Abra o terminal ou prompt de comando.
2. Atualise o sistema com:
```
sudo apt-get update
```
3. instale o pip:
```
sudo apt install python-pip
```
4. instale o behave:
```
pip install behave
```

## Estrutura de pastas e arquivos

A estrutura de pastas e arquivos nesta aula segue uma convenção comum usada em projetos Behave:

├── features/<br>
│ ├── steps/<br>
│ │ └── steps.py<br>
│ └── example.feature<br>
├── tests/<br>
│ └── test_example.py<br>
└── README.md<br>


- **features/**: Esta pasta contém os arquivos de feature do Behave, que descrevem o comportamento esperado do sistema em uma linguagem Gherkin.
  - **steps/**: Nesta pasta, você encontrará os arquivos Python que implementam os steps definidos nas features.
  - **example.feature**: Exemplo de arquivo de feature do Behave.

- **tests/**: Esta pasta contém os testes adicionais que você pode escrever para complementar os cenários definidos nas features.
  - **test_example.py**: Exemplo de arquivo de teste adicional.

- **README.md**: Este arquivo que você está lendo agora!

## Executando os testes

Para executar os testes usando o Behave, você pode usar o seguinte comando na raiz do projeto:

```
behave
```

## Recursos adicionais

Aqui estão alguns recursos adicionais que podem ajudá-lo a aprender mais sobre o Behave:

- Documentação oficial do Behave: [https://behave.readthedocs.io](https://behave.readthedocs.io)
- Exemplos de projetos Behave no GitHub: 
    - [behave](https://github.com/behave/behave)
    - [dunossauro](https://github.com/dunossauro/curso-python-selenium/tree/master/behave-exemplo)


Divirta-se aprendendo e automatizando testes com o Behave!