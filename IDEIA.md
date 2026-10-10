# 💡 Ideia: Investing

> Este repositório é uma **ideia em validação**. Mapa completo de todas as ideias: [IDEIAS.md no repo `dev`](https://github.com/cantsixsix/dev/blob/claude/serene-bardeen-1tjfw2/IDEIAS.md).
>
> Estágios: 💡 ideia · 🧪 protótipo · 🚀 no ar · ✅ validada · 🗄️ arquivada.
> Regra: antes de escrever mais código, rodar o **teste** de uma variação. Sem reação em 2 semanas → 🗄️.

## F2 · Investing — `investing` 🧪

Python + yfinance: calcula indicadores e dá uma nota para cada ativo.
- **F2.a Ações BR** — `agora.py`. *Teste:* relatório semanal num canal e ver se alguém pede o próximo.
- **F2.b Ações internacionais** — `internacional.py` (hoje vazio).
- **F2.c Alerta de nota** — avisa quando um ativo muda de nota.
- **F2.d Newsletter de análise** — o relatório vira conteúdo.

<!-- validacao:inicio -->

## 🧪 Como validar

Teste de 7 dias. Resultados vão na [Bancada de Ideias](https://claude.ai/artifact/Y4H9MCxyvwwLDmhL812znj).

### F2 · Investing — scanner de ativos

**Em uma frase:** Analisa ~200 ações, FIIs e criptos e mostra quais estão com melhor nota esta semana.

- **Problema:** Investidor iniciante não tem tempo de olhar indicador por indicador de centenas de ativos.
- **Para quem:** Pessoa física que investe por conta própria na B3 e em cripto.
- **Como funciona:** Um script baixa os preços do Yahoo Finance, analisa só o gráfico (sem olhar balanço nem dividendos) e dá uma nota de 0 a 100. O resultado vira um relatório semanal.
- **Como ganha dinheiro:** Newsletter grátis com top 5; R$ 19,90/mês para o ranking completo e alertas. (Não é recomendação de investimento.)

| Teste | |
|---|---|
| Tipo | Post de conteúdo com link |
| Página | https://validar-ideias.netlify.app/f2/ |
| Onde divulgar | Grupos de investimento no Telegram, Twitter/X fintwit |
| Preço testado | R$ 19,90/mês (ranking completo) |
| Meta em 7 dias | **50 inscrições em 14 dias** |

<!-- validacao:fim -->
