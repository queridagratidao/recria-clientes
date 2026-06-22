# Clientes RECRIA

Repositório privado com dados de diagnóstico, estratégia, copy e criativos de cada cliente da agência RECRIA.

Estrutura por cliente: `[slug-do-cliente]/`
- `questionario-onboarding*.md` — respostas do questionário de diagnóstico
- `diagnostico-estrategico.{md,docx,pdf}` — diagnóstico e plano de ação (gerado pela skill `estrategista-cliente`)
- `copies/` — copies de social media e tráfego pago (gerado pela skill `copywriter-cliente`)
- `social-media/` — criativos pra postar no perfil do cliente (gerado pela skill `design-social-media-cliente`)
- `trafego-pago/` — criativos e briefing pro gestor de tráfego (gerado pela skill `design-trafego-cliente`)

Pipeline completo: `questionario-cliente` → `estrategista-cliente` → `copywriter-cliente` → `design-social-media-cliente` / `design-trafego-cliente`.
