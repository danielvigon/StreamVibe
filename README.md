# StreamVibe - Cadastro de Filmes e Usuários

## Descrição
**StreamVibe** é um sistema simples de cadastro de filmes e usuários, desenvolvido com **Python** e **Django**, permitindo que os usuários possam adicionar filmes ao catálogo e registrar suas informações. O objetivo do projeto é proporcionar uma maneira intuitiva e rápida de organizar filmes e usuários para futuras interações.

<p align ="center">
<img src="./.github/preview.png" alt="captura de tela referente ao projeto StreamVibe"/>
</p>

## Funcionalidades

- **Cadastro de Filmes**: Adicione filmes com título, gênero, ano de lançamento, sinopse e outros detalhes relevantes.
- **Cadastro de Usuários**: Criação de contas de usuário com funcionalidades de login e gerenciamento de perfil.
- **Busca e Filtro de Filmes**: Encontre filmes por título, gênero ou ano de lançamento.
- **Interação com o Catálogo**: Permite aos usuários interagir com o catálogo de filmes, podendo marcar favoritos ou fazer recomendações.

## Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**
- **SQLite** (ou outro banco de dados configurável)
- **Bootstrap 4** (para estilização)
- **Django Rest Framework** (se for incluir APIs para front-end ou mobile)

## Como Rodar o Projeto Localmente

1. Clone o repositório:
    ```bash
    git clone https://github.com/SEU-USER/StreamVibe.git
    ```

2. Acesse o diretório do projeto:
    ```bash
    cd StreamVibe
    ```

3. Crie e ative um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

7. Acesse o projeto no navegador:
    ```
    http://127.0.0.1:8000/
    ```

## Como Contribuir

1. Faça um **fork** deste repositório.
2. Crie uma **branch** para a sua feature (ex: `feature/nova-funcionalidade`).
3. Realize as alterações necessárias.
4. Envie um **pull request** com uma descrição detalhada da alteração.

## Licença

Este projeto está licenciado sob a **MIT License** - consulte o arquivo [LICENSE](./LICENSE) para mais informações.

## Demonstração

Se você já tiver o projeto rodando, pode adicionar algumas imagens ou uma pequena demonstração de como o sistema se comporta:

- Página de cadastro de filmes
- Tela de login de usuários

## Roadmap

- [ ] Implementar funcionalidades de comentários e avaliações de filmes.
- [ ] Criar um sistema de recomendações baseado nos filmes assistidos.
- [ ] Adicionar suporte para múltiplos tipos de usuários (ex: administradores e usuários comuns).
- [ ] Implementar integração com APIs externas de filmes (como IMDb ou The Movie Database).
