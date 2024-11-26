# traslator-google-English-Portuguese-Indian
 Segue um código Python para criar um **Tradutor de Arquivos de Texto com Interface Gráfica** no Windows 10. Este tradutor permite:

1. Escolher a **pasta de entrada** e a **pasta de saída**.
2. Selecionar a **primeira língua** (origem) e a **segunda língua** (destino) a partir de uma lista de opções: *Inglês, Português Europeu, Indiano*.
3. Traduzir os arquivos `.txt` da pasta de entrada para a língua de destino e salvar na pasta de saída.

### Passo a Passo

1. **Importação de Módulos**:
   - `os`: Para manipulação de arquivos e pastas.
   - `tkinter` e `ttk`: Para a interface gráfica.
   - `googletrans`: Para tradução dos textos.
   - `Combobox`: Para seleção das línguas.

2. **Funções de Interface**:
   - `escolher_pasta_entrada` e `escolher_pasta_saida`: Usam `filedialog` para selecionar pastas.
   - `traduzir_arquivos`: Gerencia a tradução e atualiza a barra de progresso.

3. **Dicionário de Idiomas**:
   - Define os idiomas suportados pelo código ISO.

4. **Interface Gráfica**:
   - Campos para selecionar pastas.
   - Combobox para selecionar as línguas de origem e destino.
   - Barra de progresso para acompanhar o progresso da tradução.

5. **Execução**:
   - Os arquivos traduzidos são salvos com o sufixo `_traduzido` na pasta de saída.

---

### Dependências

Instale o módulo `googletrans` antes de executar o código:

```bash
pip install googletrans==4.0.0-rc1
```

Com este programa, você pode traduzir arquivos `.txt` entre as línguas disponíveis (Português Europeu, Inglês e Indiano).
