# Desafio-Nivel-1-PDV-com-Descontos-Python-
Atividade do Programa Trilhas - Inova

## O que o código faz:
Faz um registo de compras, aplica desconto de 20% se a idade for >= 65 anos, caso o valor do desconto for > R$100 recebe um valor extra de 10%, não recebe valor negativo, armazena os dados em uma lista e ao digitar o 0 (zero) o codigo é encerrado e mostra uma lista com  resumo do dia. 

## Como ele faz:
Funciona como um caixa de supermecado: primeiro recebe o valor da compra e a idade do cliente, depois, verifica se tem direito ao desconto de 20% por idade e em seguida, se o valor da compra com o desconto passar de R$100 será aplicado +10%, feito isso será salvo em um histórico ou lista, depois disso voltará novamente pedindo outro valor da compra ( seria um loop), esse loop só terminará quando o clinte digitar 0 e logo em seguida aparecerá o resumo do dia: quantidade de comprar registrada, total bruto (soma dos valores originais), total do desconto concedidos e total final(soma dos valores com descontos).

## Como rodar:
O comando pra executar o programa ( python pdv.py)

## Tabela de exemplos:
| Caso | Valor(R$) | Idade | Desconto Idade | Desconto por Valor | Valor Final Esperado | 
|---|---|---|---|---|---|
|    1   |  R$50.00    |   30 |  0%  | 0%  | R$50.00 |
|    2   |  R$100.00    |   30 |  0%  | 0%  | R$100.00 |
|    3   |  R$80.00    |   65 |  20%  | 0%  | R$64.00 |
|    4   |  R$100.00    |   70 |  20%  | 0%  | R$80.00 |
|    5   |  R$250.00    |   70 |  20%  | 0%  | R$100.00 |
|    6   |  R$200.00    |   30 |  0%  | 10%  | R$180.00 |
|    7   |  R$101.00    |   30 |  0%  | 10%  | R$90.90|
|    8   |  R$200.00    |   650 |  20%  | 10%  | R$144.00 |
|    9   |  R$1000.00    |   80 |  20%  | 10%  | R$720.00 |
|    10   |  R$200.00    |   64 |  0%  | 10%  | R$180.00 |

