# Como atualizar o site

Sempre que mudar algo (texto, projeto novo, imagem, etc.), siga essa ordem no terminal:

## 1. Salvar as mudanças no GitHub (código-fonte)

git add .
git commit -m "descrição da mudança"
git push

## 2. Publicar a versão visual atualizada (o site de verdade)

quarto publish gh-pages

---

Pronto! Espera 1-2 minutos e confere em:
https://iuryxavierr.github.io/

Se pedir confirmação (Y/n), aperta Y e Enter.