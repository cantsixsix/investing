import yfinance as yf
import pandas as pd
import numpy as np
import time
import warnings
from datetime import datetime

# --- CONFIGURAÇÕES VISUAIS E DE SISTEMA ---
warnings.filterwarnings("ignore")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# ==============================================================================
# 1. LISTAS DE ATIVOS (MASSIVAS)
# ==============================================================================

# >> AÇÕES BRASIL (IBRA + Small Caps Líquidas - Aprox. 120 Tickers)
ACOES_BR = [
    'ABEV3.SA', 'ALOS3.SA', 'ALPA4.SA', 'ALUP11.SA', 'AMBP3.SA', 'ARZZ3.SA', 'ASAI3.SA', 'AZUL4.SA', 'AZZA3.SA',
    'B3SA3.SA', 'BBAS3.SA', 'BBDC3.SA', 'BBDC4.SA', 'BBSE3.SA', 'BEEF3.SA', 'BHIA3.SA', 'BPAC11.SA', 'BPAN4.SA',
    'BRAP4.SA', 'BRAV3.SA', 'BRFS3.SA', 'BRKM5.SA', 'BRSR6.SA', 'CAML3.SA', 'CASH3.SA', 'CCRO3.SA', 'CEAB3.SA',
    'CMIG3.SA', 'CMIG4.SA', 'CMIN3.SA', 'COGN3.SA', 'CPFE3.SA', 'CPLE6.SA', 'CRFB3.SA', 'CSAN3.SA', 'CSNA3.SA',
    'CURY3.SA', 'CVCB3.SA', 'CYRE3.SA', 'DIRR3.SA', 'DXCO3.SA', 'ECOR3.SA', 'EGIE3.SA', 'ELET3.SA', 'ELET6.SA',
    'EMBR3.SA', 'ENAT3.SA', 'ENEV3.SA', 'ENGI11.SA', 'EQTL3.SA', 'EZTC3.SA', 'FLRY3.SA', 'GGBR4.SA', 'GGPS3.SA',
    'GOAU4.SA', 'GOLL4.SA', 'HAPV3.SA', 'HYPE3.SA', 'IGTI11.SA', 'INTB3.SA', 'IRBR3.SA', 'ITSA4.SA', 'ITUB4.SA',
    'JBSS3.SA', 'JHSF3.SA', 'KEPL3.SA', 'KLBN11.SA', 'LREN3.SA', 'LWSA3.SA', 'MATD3.SA', 'MGLU3.SA', 'MRFG3.SA',
    'MRVE3.SA', 'MULT3.SA', 'NEOE3.SA', 'NTCO3.SA', 'ODPV3.SA', 'ONCO3.SA', 'PCAR3.SA', 'PETR3.SA', 'PETR4.SA',
    'PETZ3.SA', 'PLPL3.SA', 'POMO4.SA', 'POSI3.SA', 'PRIO3.SA', 'PSSA3.SA', 'RADL3.SA', 'RAIL3.SA', 'RAIZ4.SA',
    'RANI3.SA', 'RDOR3.SA', 'RECV3.SA', 'RENT3.SA', 'ROMI3.SA', 'SANB11.SA', 'SBFG3.SA', 'SBSP3.SA', 'SLCE3.SA',
    'SMTO3.SA', 'SOMA3.SA', 'STBP3.SA', 'SUZB3.SA', 'TAEE11.SA', 'TASA4.SA', 'TIMS3.SA', 'TOTS3.SA', 'TRPL4.SA',
    'UGPA3.SA', 'USIM5.SA', 'VALE3.SA', 'VAMO3.SA', 'VBBR3.SA', 'VIVA3.SA', 'VIVT3.SA', 'WEGE3.SA', 'YDUQ3.SA'
]

# >> FIIs (IFIX - Principais e Mais Líquidos - Aprox. 60 Tickers)
FIIS = [
    'ALZR11.SA', 'BTLG11.SA', 'BCFF11.SA', 'BRCO11.SA', 'BRCR11.SA', 'CPTS11.SA', 'DEVA11.SA', 'GGRC11.SA',
    'HCTR11.SA', 'HGLG11.SA', 'HGBS11.SA', 'HGRE11.SA', 'HGRU11.SA', 'HTMX11.SA', 'IRDM11.SA', 'JSRE11.SA',
    'KNCR11.SA', 'KNHY11.SA', 'KNIP11.SA', 'KNRI11.SA', 'KNSC11.SA', 'MALL11.SA', 'MXRF11.SA', 'PVBI11.SA',
    'RBRF11.SA', 'RBRP11.SA', 'RBRR11.SA', 'RBRY11.SA', 'RECR11.SA', 'RZTR11.SA', 'SARE11.SA', 'SPXS11.SA',
    'TGAR11.SA', 'TRXF11.SA', 'VCJR11.SA', 'VGHF11.SA', 'VGIP11.SA', 'VILG11.SA', 'VINO11.SA', 'VISC11.SA',
    'VRTA11.SA', 'XPIN11.SA', 'XPLG11.SA', 'XPML11.SA', 'RBED11.SA', 'LVBI11.SA', 'BRES11.SA', 'VLGQ11.SA'
]

# >> CRIPTOMOEDAS (Top Market Cap - Aprox. 40 Tickers)
CRIPTOS = [
    'BTC-USD', 'ETH-USD', 'BNB-USD', 'SOL-USD', 'XRP-USD', 'ADA-USD', 'DOGE-USD', 'AVAX-USD', 'TRX-USD',
    'DOT-USD', 'LINK-USD', 'MATIC-USD', 'TON-USD', 'SHIB-USD', 'LTC-USD', 'BCH-USD', 'ATOM-USD', 'XMR-USD',
    'ETC-USD', 'XLM-USD', 'FIL-USD', 'HBAR-USD', 'APT-USD', 'ARB-USD', 'NEAR-USD', 'VET-USD', 'QNT-USD',
    'MKR-USD', 'GRT-USD', 'AAVE-USD', 'ALGO-USD', 'STX-USD', 'IMX-USD', 'EOS-USD', 'SAND-USD', 'THETA-USD'
]

# >> COMBINAÇÃO DE TUDO
LISTA_COMPLETA = []
for t in ACOES_BR: LISTA_COMPLETA.append({'Ticker': t, 'Tipo': 'AÇÃO BR'})
for t in FIIS: LISTA_COMPLETA.append({'Ticker': t, 'Tipo': 'FII'})
for t in CRIPTOS: LISTA_COMPLETA.append({'Ticker': t, 'Tipo': 'CRIPTO'})

# ==============================================================================
# 2. FUNÇÕES DO MOTOR DE ANÁLISE
# ==============================================================================

def calcular_indicadores(df):
    if len(df) < 50: return None # Precisa de dados mínimos

    try:
        # Preço Atual
        preco = df['Close'].iloc[-1]

        # 1. RSI (14 períodos)
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs)).iloc[-1]

        # 2. Bandas de Bollinger (20 períodos, 2 desvios)
        sma20 = df['Close'].rolling(window=20).mean()
        std20 = df['Close'].rolling(window=20).std()
        upper = sma20 + (std20 * 2)
        lower = sma20 - (std20 * 2)

        # Distância relativa das bandas (para saber se "estourou")
        dist_lower = (preco / lower.iloc[-1]) - 1
        dist_upper = (preco / upper.iloc[-1]) - 1

        # 3. Tendência (Média Móvel 200)
        # Se o histórico for curto (ex: ativos novos), usa MM50
        if len(df) >= 200:
            mm_longa = df['Close'].rolling(window=200).mean().iloc[-1]
        else:
            mm_longa = df['Close'].rolling(window=50).mean().iloc[-1]

        tendencia = "ALTA" if preco > mm_longa else "BAIXA"

        return {
            'Preço': preco,
            'RSI': rsi,
            'Tendência': tendencia,
            'Lower': lower.iloc[-1],
            'Upper': upper.iloc[-1]
        }
    except:
        return None

def dar_nota(indicadores):
    score = 50 # Nota base neutra
    rsi = indicadores['RSI']
    preco = indicadores['Preço']

    # Critério RSI (Peso 40%)
    if rsi <= 25: score += 35      # Extremo desconto
    elif rsi <= 35: score += 20    # Desconto
    elif rsi >= 75: score -= 35    # Extremo sobrepreço
    elif rsi >= 65: score -= 20    # Sobrepreço

    # Critério Bollinger (Peso 30%)
    # Se furou a banda de baixo (está muito barato graficamente)
    if preco < indicadores['Lower']: score += 15
    # Se furou a banda de cima (está muito caro)
    if preco > indicadores['Upper']: score -= 15

    # Critério Tendência (Peso 30%)
    # Ajudar quem está em tendência de alta (Buy the dip)
    if indicadores['Tendência'] == "ALTA": score += 10
    else: score -= 10 # Penaliza quem está caindo no longo prazo (faca caindo)

    # Trava a nota entre 0 e 100
    return max(0, min(100, score))

# ==============================================================================
# 3. EXECUTAR O SCANNER (COM PROTEÇÃO)
# ==============================================================================

def rodar_analise():
    print(f"🚀 INICIANDO GIGA SCANNER - {len(LISTA_COMPLETA)} ATIVOS NA FILA")
    print("ℹ️  Modo de Segurança Ativado: Lotes pequenos com pausas para evitar bloqueio.")
    print("☕ Pegue um café, isso vai levar uns 3 a 5 minutos...\n")

    resultados = []

    # Configuração do Batch (Lote)
    tamanho_lote = 15
    total_lotes = len(LISTA_COMPLETA) // tamanho_lote + 1

    for i in range(0, len(LISTA_COMPLETA), tamanho_lote):
        lote_atual = LISTA_COMPLETA[i:i + tamanho_lote]
        num_lote = (i // tamanho_lote) + 1

        # Pega só os tickers para baixar
        tickers_lote = [item['Ticker'] for item in lote_atual]
        tickers_string = " ".join(tickers_lote)

        print(f"⏳ Processando Lote {num_lote}/{total_lotes} ({len(tickers_lote)} ativos)...")

        try:
            # Download em grupo é mais eficiente que um por um
            dados_lote = yf.download(tickers_string, period="1y", group_by='ticker', progress=False, threads=True)

            # Itera sobre cada ativo do lote baixado
            for item in lote_atual:
                ticker = item['Ticker']
                tipo = item['Tipo']

                try:
                    # Trata diferença se for apenas 1 ativo ou vários no dataframe
                    if len(tickers_lote) == 1:
                        df_ativo = dados_lote
                    else:
                        df_ativo = dados_lote[ticker]

                    df_ativo = df_ativo.dropna()

                    indicadores = calcular_indicadores(df_ativo)

                    if indicadores:
                        score = dar_nota(indicadores)

                        # Define Status Texto
                        if score >= 90: status = "💎 DIAMANTE (COMPRA)"
                        elif score >= 75: status = "🟢 OPORTUNIDADE"
                        elif score <= 10: status = "🔥 PERIGO (TOPO)"
                        elif score <= 30: status = "🔴 CUIDADO"
                        else: status = "⚪ NEUTRO"

                        resultados.append({
                            'TIPO': tipo,
                            'ATIVO': ticker.replace('.SA', '').replace('-USD', ''),
                            'PREÇO': round(indicadores['Preço'], 2),
                            'RSI': round(indicadores['RSI'], 1),
                            'TEND': indicadores['Tendência'],
                            'SCORE': int(score),
                            'STATUS': status
                        })

                except Exception as e:
                    # Silencioso para não poluir, apenas pula
                    continue

        except Exception as e:
            print(f"❌ Erro no lote {num_lote}: {e}")

        # PAUSA TÁTICA (ESSENCIAL PARA NÃO SER BLOQUEADO)
        time.sleep(2)

    # ==============================================================================
    # 4. EXIBIÇÃO FINAL
    # ==============================================================================

    if not resultados:
        print("\n❌ Nenhum dado coletado. Verifique sua internet ou tente mais tarde.")
        return

    df_final = pd.DataFrame(resultados)
    df_final = df_final.sort_values(by='SCORE', ascending=False)

    print("\n" + "="*80)
    print("✅ ANÁLISE FINALIZADA COM SUCESSO!")
    print("="*80)

    # Top 15 Oportunidades (Geral)
    print("\n🏆 TOP 15 MELHORES PONTUAÇÕES (GERAL):")
    print(df_final.head(15).to_string(index=False))

    # Top 15 Cripto
    print("\n🪙 TOP 5 CRIPTOS (DESCONTADAS):")
    print(df_final[df_final['TIPO'] == 'CRIPTO'].head(5).to_string(index=False))

    # Top 5 FIIs
    print("\n🏢 TOP 5 FIIs (BONS E BARATOS):")
    print(df_final[df_final['TIPO'] == 'FII'].head(5).to_string(index=False))

    # Top 5 Ações
    print("\n📈 TOP 5 AÇÕES BRASIL:")
    print(df_final[df_final['TIPO'] == 'AÇÃO BR'].head(5).to_string(index=False))

    # Salva Excel
    nome_arquivo = f"Relatorio_GigaScanner_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    df_final.to_excel(nome_arquivo, index=False)
    print(f"\n💾 Relatório Completo salvo em: {nome_arquivo}")

if __name__ == "__main__":
    rodar_analise()

