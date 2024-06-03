criar executável: pyinstaller --onefile --windowed app.py

2. Adicionar Função get_resource_path

Primeiro, crie um utilitário para lidar com o caminho dos recursos. Isso pode ser colocado em um módulo separado, por exemplo, utils.py, ou diretamente no seu app.py se for simples.

3. Ajustar main_interface.py

Modifique o arquivo main_interface.py para usar a função get_resource_path ao carregar recursos. Vou assumir que você está carregando a imagem do logo no main_interface.py.

4. Atualizar app.py

Certifique-se de importar a função correta no app.py.

5. Gerar o Executável com PyInstaller

Finalmente, use o comando PyInstaller para gerar o executável, incluindo a pasta assets:

pyinstaller --onefile --windowed --add-data "assets:assets" app.py
