import os

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pages = [
    ('item-1-2.html', 'Item 1.2'),
    ('item-1-3.html', 'Item 1.3'),
    ('item-2-1.html', 'Item 2.1'),
    ('item-2-2.html', 'Item 2.2'),
    ('item-3-1.html', 'Item 3.1'),
    ('item-3-2.html', 'Item 3.2'),
    ('item-3-3.html', 'Item 3.3')
]

for filename, title in pages:
    # 1. Remove active class from Item 1.1
    new_content = content.replace('href="index.html" class="active">Item 1.1</a>', 'href="index.html">Item 1.1</a>')
    
    # 2. Add active class to the correct item
    old_link = f'href="{filename}">{title}</a>'
    new_link = f'href="{filename}" class="active">{title}</a>'
    new_content = new_content.replace(old_link, new_link)
    
    # 3. Replace the main H1 title to make each page look distinct
    new_content = new_content.replace('<h1>Main Page Title (e.g., Installation Guide)</h1>', f'<h1>{title}</h1>')
    
    # Save the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Generated 7 template files successfully.")
