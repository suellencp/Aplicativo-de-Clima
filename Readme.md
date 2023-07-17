# Previsão do Tempo em Tkinter com API do OpenWeatherMap #
Este é um projeto simples de previsão do tempo usando a biblioteca Tkinter em Python e a API do OpenWeatherMap para obter as informações meteorológicas da cidade, exibindo a temperatura atual, descrição do clima e um ícone representativo.

# Funcionalidades #
O usuário pode inserir o nome da cidade desejada na caixa de entrada.
Ao clicar no botão "Search", o aplicativo faz uma requisição para a API do OpenWeatherMap para obter as informações de clima da cidade.
Se a cidade for encontrada, o aplicativo exibe o nome da cidade/país, o ícone do clima, a temperatura atual e a descrição do clima.
Se a cidade não for encontrada, uma caixa de diálogo de erro é exibida para informar o usuário.

# Dependências #
O projeto utiliza as seguintes bibliotecas:

tkinter: Biblioteca padrão para criar interfaces gráficas em Python.
requests: Biblioteca para realizar requisições HTTP.
PIL (Pillow): Biblioteca para manipulação de imagens.
ttkbootstrap: Biblioteca para estilizar os widgets do Tkinter.

# Configuração #
Antes de executar o código, é necessário obter uma chave de API do OpenWeatherMap. Acesse o site https://openweathermap.org/, crie uma conta gratuita e obtenha sua chave de API.

Certifique-se de ter instalado as bibliotecas necessárias.

# Utilização #
Importe as bibliotecas necessárias.
Defina a função get_weather(city) para obter as informações de clima da API do OpenWeatherMap.
Defina a função search() para pesquisar o clima para uma cidade especificada pelo usuário.
Crie a janela principal usando a classe ttkbootstrap.Window e defina o tema desejado.
Adicione os widgets na janela, incluindo uma caixa de entrada para a cidade, um botão de pesquisa, rótulos para exibir as informações de clima e um rótulo para exibir o ícone do clima.
Defina a função mainloop() para iniciar o loop principal da interface gráfica.

# Observações #
Certifique-se de substituir a variável API_key pela sua própria chave de API do OpenWeatherMap.
Os ícones de clima são obtidos a partir da API do OpenWeatherMap. Caso deseje usar ícones personalizados, você pode salvá-los localmente e atualizar o código para carregar os ícones personalizados a partir de uma pasta específica.
Este projeto é um exemplo básico de como criar um aplicativo de previsão do tempo utilizando a biblioteca Tkinter. Você pode personalizá-lo e adicionar mais funcionalidades conforme suas necessidades.