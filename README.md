# Investing

Scanner de ativos em Python: baixa dados do Yahoo Finance (`yfinance`) para ações brasileiras, FIIs e criptos (cerca de 200 ativos), calcula indicadores, dá uma nota para cada ativo e mostra os melhores por categoria.

## Rodar

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python agora.py      # leva de 3 a 5 minutos (baixa em lotes com pausas)
```

`internacional.py` está vazio — reservado para a variação F2.b (só ativos internacionais).

Ideias e variações: [IDEIA.md](IDEIA.md).
