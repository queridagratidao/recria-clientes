import pathlib
from playwright.sync_api import sync_playwright
P=pathlib.Path('/home/user/recria-clientes/agencia-recria/cursos/recria-ads/paginas')
F=(pathlib.Path(__file__).parent/'c1/fonts_embedded.css').read_text()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    for name in ['pagina-de-vendas','pagina-de-obrigado']:
        for w,tag in [(390,'celular'),(1280,'computador')]:
            pg=b.new_page(viewport={'width':w,'height':900},device_scale_factor=2 if w<500 else 1)
            pg.route('**/fonts.googleapis.com/**',lambda r:r.fulfill(body='',content_type='text/css'))
            pg.goto((P/f'{name}.html').as_uri()); pg.add_style_tag(content=F); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
            pg.screenshot(path=str(P/f'preview-{name}-{tag}.png'),full_page=True); pg.close()
    b.close()
