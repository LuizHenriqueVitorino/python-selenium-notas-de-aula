# DESAFIOS E EXERCÍCIOS
## DESAFIOS
### 1. **Testlink** - *Desafio proposto pela GREat-UFC*

Implemente um caso de testes automatizado com **SELENIUM** ou **Robot Framework** para o seguinte cenário:

1. Acesse a página do [Testlink](https://testlink.org/)
```md
https://testlink.org/
```
2. Faça alguns assertions na página do Testlink;
3. Click no link para o GitHub do Testlink;
4. Faça alguns assertions na página para confirmar que é o github do Testlink;
5. (Opcional) Realizar uma pesquisa no GitHub e verificar resultado.

## EXERCÍCIOS
### 1. **ESCREVER EM INPUTs** - *Exercício dos formulários*

Implement um caso de teste automatizado com **Selenium** de forma que a automação siga os seguintes passos:

1. Acesse a página do [test](https://selenium.dunossauro.live/exercicio_06.html)
```md
https://selenium.dunossauro.live/exercicio_06.html
```
2. Preencha o primeiro formulário com um *nome* e uma *senha* e clique no botão *enviar*;
![imagem do formulario](imagens/documentacao/formulario1.png)

3. Verifique a resposta no canto inferior esquerdo da tela;
![resposta](imagens/documentacao/resposta.png)

4. Repita este procedimento para todos os formulários.

### 2. **ESPERAS IMPLÍCITAS E EXPLÍCITAS** - *Exercício da barra de espera*

Crie dois arquivos e implemente dois casos de testes automatizado com **SELENIUM**, em um arquivo você deve implementar utilizando o **Implicit Wait** e, no outro, o **Explicit Wait**, para o seguinte cenário:

1. Acesse a página do [test](https://selenium.dunossauro.live/aula_09_a.html);
```md
https://selenium.dunossauro.live/aula_09_a.html
``` 
2. Espere o carregamento do botão **barrinha top**;
![carregamento do botão barrinha top](imagens/documentacao/carrega_botao.png)

3. Clique no botão **barrinha top**;
![botão barrinha top](/imagens/documentacao/botao_barrinha_top.png)

4. Espere a barra de load desaparecer;
![barrinha de load](/imagens/documentacao/barra_de_load.png)

5. Verifique a mensagem de carregamento concluído utilizando *assert*
![mensagem de sucesso](imagens/documentacao/carregamento_concluido.png)

### 2. **Alerts e Prompts** - *Exercício do site omayo*
#### 2.1 **ALERTs**
Implemente um caso de testes automatizado com **SELENIUM** para o seguinte cenário:

1. Acesse a página do [test](https://omayo.blogspot.com/);
```md
https://omayo.blogspot.com/
```
2. Preencha o login simples no final da página;
![login simples](imagens/documentacao/login_simples.png)

3. Dê um **assert** na mensagem no Alert e clique em **OK**;
![Alert](imagens/documentacao/alert.png)

#### 2.2 **PROMPTs**
Implemente um caso de testes automatizado com **SELENIUM** para o seguinte cenário:

1. Acesse a página do [test](https://omayo.blogspot.com/);
```md
https://omayo.blogspot.com/
```
2. Clique no botão **get prompt** localizado no lado direito da tela;
![botão get prompt](imagens/documentacao/botao_prompt.png)

3. Escreva algo no **prompt** e aperte no botão **OK**
![Prompt](imagens/documentacao/prompt.png)

### 2. **ABAS E JANELAS** - *Exercício da função que pecorre os Ids das páginas abertas*

Implemente uma automação com **SELENIUM** de acordo com o que se pede:

1. Você deve fazer a automação abrir 5 abas ou janelas de sua escolha;
2. No seu arquivo deve possuir uma função com as seguintes características:

| AÇÃO        | DESCRIÇÃO      |
|:----------  |:----------------|
| input       | Uma string     |
| output      | A url da aba que contém a String passada por parâmetro
