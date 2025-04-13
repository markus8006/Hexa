# 📦 Hexa - Biblioteca de Conversão Hexadecimal

Uma biblioteca Python simples e educacional para conversão de números hexadecimais para decimal e vice-versa, além de manipulação de dados via uma classe personalizada.

---

## 🚀 Funcionalidades

- 📥 Converte números hexadecimais (como `'0xA'`, `'B'`, `'1F'`) para decimal.
- 📤 Converte números decimais para hexadecimal.
- 🧠 Classe `hexa` que recebe dados JSON-like com valores hexadecimais e converte para decimal automaticamente.
- ➕ Suporte à soma entre dois objetos da classe `hexa`.

---

## 📄 Estrutura do Projeto

```bash
.
├── Bibli.py     # Arquivo da biblioteca com as funções e a classe principal
├── main.py      # Script de exemplo usando a biblioteca
└── README.md    # (Este arquivo)
```


🧰 Como Usar
1. Importando a Biblioteca
python
Copiar código
import Bibli
2. Criando um dicionário com dados hexadecimais
python
Copiar código
```python
Hexas = {
    "num1": "A",
    "num2": "B",
    "num3": "C",
    "num4": "D"
}
```
4. Criando uma instância da classe hexa
python
Copiar código
```python
H = Bibli.hexa(Hexas)
```
6. Acessando os valores convertidos
python
Copiar código
```
print(H.num1)  # Saída: 10
print(H.num2)  # Saída: 11
```

8. Usando in_hexa() para converter decimal → hexadecimal
python
Copiar código
```python
print(Bibli.in_hexa(H.num1 + H.num3))  # Ex: 10 + 12 = 22 → "16"
print(Bibli.in_hexa(15))               # Saída: "F"
```
🔍 Funções e Classe
```python
convert(num)
```
Converte uma string hexadecimal para decimal.

Parâmetro: num (str, int ou com prefixo "0x")

Retorno: inteiro decimal
```python
in_hexa(num)
```
Converte um número decimal para hexadecimal.

Parâmetro: num (int, float ou str numérica)

Retorno: string hexadecimal (sem "0x")

class hexa
Classe que recebe um dicionário com valores hexadecimais e os converte para atributos decimais.

Parâmetros:
json_data — dicionário com chaves e valores hexadecimais.

debug — exibe mensagens de depuração (opcional).

Métodos:
__repr__() — representação do objeto.

__add__() — soma de dois objetos hexa.

📦 Exemplo de Saída
python
Copiar código
```bash
Class: hexa, Hexa: ({'num1': 'A', 'num2': 'B', 'num3': 'C', 'num4': 'D'})
16
F
```
⚠️ Nota
O módulo Bibli.py não é projetado para ser executado diretamente. Use-o via importação.

📚 Licença
Este projeto é apenas para fins educacionais. Use, modifique e aprenda!

✍️ Autor
Feito por Guilherme Rezende Markus
