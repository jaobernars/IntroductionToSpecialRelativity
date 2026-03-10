import glob

html_files = glob.glob('item-*.html')

sidebar_addition = '''<div class="sidebar-group">
                    <h3>Visão Geral</h3>
                    <ul>
                        <li><a href="index.html">Cabeçalho do Modelo</a></li>
                        <li><a href="index.html#resumo">Resumo do Documento</a></li>
                        <li><a href="index.html#toc">Índice Completo</a></li>
                    </ul>
                </div>
                <div class="sidebar-group">'''

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'Visão Geral' in content:
        continue
        
    content = content.replace('<li><a href="index.html">Item 1.1</a></li>', '<li><a href="item-1-2.html">Item 1.1</a></li>')
    content = content.replace('<li><a href="index.html" class="active">Item 1.1</a></li>', '<li><a href="item-1-2.html" class="active">Item 1.1</a></li>')

    content = content.replace('<div class="sidebar-group">', sidebar_addition, 1)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f'Updated {len(html_files)} files')
