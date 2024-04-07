## Configuração do Ambiente
Primeiro, crie um ambiente virtual para isolar as dependências do projeto:

```shell
python -m venv envs
```

Ative o ambiente virtual:

* No Windows:
```shell
envs\Scripts\activate.bat
```

* No Unix ou macOS:
```shell
source envs/bin/activate
```

Importe os pacotes necessarios para o projeto

```shell
pip install aiohttp 
```