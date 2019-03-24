# ElliotBot </h1>
[![Github-Release][git-release]][release-link]
[![License][license]][license-link]
![Repository-Size][repo-size]

>Telegram Bot destinado para gerenciamento de Mensagens e uso administrativo do grupo no Telegram, [Guia Anônima][link-telegram].

## Requisitos
Caso deseje utilizar este Telegram Bot, ou executá-lo, precisará dos seguintes pacotes, presentes no ```requeriments.txt```:

* ```certifi==2019.3.9```
* ```chardet==3.0.4```
* ```idna==2.8```
* ```pyTelegramBotAPI==3.6.6```
* ```python-dotenv==0.10.1```
* ```requests==2.21.0```
* ```six==1.12.0```
* ```urllib3==1.24.1```

Para instalar todos, de uma única vez, utilize o comando abaixo:

```pip install pyTelegramBotAPI python-dotenv```

Ou utilizando o arquivo ```requeriments.txt```:

```pip install -r requeriments.txt```

## Instalação
O processo de intalção é simples. Basta fazer um ```git clone``` do repositório.

```git clone https://github.com/TheMrKeven/ElliotBot.git```

Entretanto, mesmo após instalado, necessita de alguns ajustes.

## Configuração
O processo de configuração também é simples, mas exige certa atenção, para que tudo funcione corretamente. 
Uma configuração errada, acarretará em certos problemas na execução do código. É aconselhável a utilização de um ambiente virtual, entretanto, se deseja utilizá-lo sem um, 
tenha certeza de que o python utilizado, é <b>Python >= 3.6</b>. 

Para ver a versão do Python, utilize seguinte comando no terminal:
```python --version```

No arquivo ```.env```, ```settings.py``` e ```messages.py```, presentes 
no diretório ```ElliotBot/src/config```, possuem algumas configurações a serem feitas.

* ```messages.py```: Ficam localizadas as mensagens do bot. Caso deseje alterar 
alguma mensagem, pode ser feito neste arquivo.

* ```.env```: Devem estar presentes nesse arquivo, o Token e o Link do Bot.
O link, é utilizado no Inline Keyboard, para direciona-lo ao chat Privado, ao apertar em <b>Regras</b>. 
O Token, deve ser obtido com o <b>BotFather</b>.

* ```settings.py```: Todas as modificações, devem ser passadas a constantes deste arquivo,
por ele ser importado pelo ```core.py```.

# Executando

Após ter configurado e instalado os requisitos, utilize o comando ```python bot.py```.

# Exemplos de Comandos

Aqui estarão listados alguns comandos já presentes no Bot, caso deseje adicionar um comando ao projeto, leia a seção [Como Contribuir][como-contribuir].

* ```/start```: _Mostra as regras do grupo._ (__Privado somente__)
* ```/rules```: _Mostra as regras do grupo. (__Privado, e no Grupo__) (__Grupo, Somente Admins__)_
* ```/ban```: _Aplica banimento em membro do grupo (__Somente por Reply__) (__Somente Admins__)_
* ```/canal```: _Mostra Link do Canal do Youtube __Guia Anônima___ (__Privado, e no Grupo__) (__Todos__)
* ```/curso```: _Mostra Cursos do Instrutor @AdSEBR (__Privado, e no Grupo__) (__Todos__)_
* ```/ctf```: _Mostra mensagem do CTF (__Privado, e no Grupo__) (__Todos__)_

# Como Contribuir
 1. Faça o fork do projeto (https://github.com/TheMrKeven/ElliotBot/fork)
 2. Crie uma branch para sua modificação (git checkout -b feature/fooBar)
 3. Faça o commit (git commit -am 'Add some fooBar')
 4. Push (git push origin feature/fooBar)
 5. Crie um novo Pull Request



[git-release]: https://img.shields.io/github/release/TheMrKeven/ElliotBot.svg
[license]: https://img.shields.io/github/license/TheMrKeven/ElliotBot.svg
[repo-size]: https://img.shields.io/github/repo-size/TheMrKeven/ElliotBot.svg
[release-link]: https://github.com/TheMrKeven/ElliotBot/releases
[license-link]: https://github.com/TheMrKeven/ElliotBot/blob/master/LICENSE
[como-contribuir]: https://github.com/TheMrKeven/ElliotBot#como-contribuir
[link-telegram]: https://t.me/joinchat/Hfn_WEnF4BMzxPJn13Bxaw
