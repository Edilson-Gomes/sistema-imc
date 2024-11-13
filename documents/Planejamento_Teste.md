*Edilson Gomes*
---

# Planejamento de Teste: Sistema de Cálculo de IMC

## 1. Objetivo
Verificar se o sistema de cadastro de pessoas e cálculo de IMC está funcionando conforme os requisitos, emitindo alertas adequados quando o IMC está fora da faixa saudável.

## 2. Escopo
- **Testes a serem realizados**: Cadastro de pessoa, cálculo de IMC, alerta de IMC.
- **Funcionalidades não testadas**: Não há funcionalidades adicionais no momento.

## 3. Tipo de Teste
- **Testes Unitários**: Métodos de cálculo de IMC e verificação de alerta.
- **Testes Funcionais**: Processo de cadastro de pessoa.

## 4. Critérios de Aceitação
- O cadastro deve ser realizado com sucesso quando os campos obrigatórios forem preenchidos corretamente.
- O cálculo do IMC deve estar correto.
- O alerta deve ser gerado se o IMC estiver abaixo de 18.5 ou acima de 24.9.

## 5. Estratégia de Teste
- **Ferramentas**: Python `unittest` para testes automatizados.
- **Testes**: Automatizados para IMC, manuais para usabilidade do cadastro.

## 6. Ambiente de Teste
- Sistema Operacional: Windows 11
- Versão do Python: 3.12.0
- Banco de Dados: Memória (não persistente)

## 7. Plano de Testes
- **Teste 1**: Cadastro de pessoa com dados válidos.
  - **Entrada**: Nome: João, Idade: 30, Peso: 85, Altura: 1.80.
  - **Saída Esperada**: IMC = 26.23, alerta gerado.
  
- **Teste 2**: Cálculo do IMC para peso abaixo da faixa saudável.
  - **Entrada**: Nome: Maria, Idade: 28, Peso: 50, Altura: 1.60.
  - **Saída Esperada**: Cadastro bem-sucedido, sem alerta de IMC.

## 8. Plano de Execução de Testes
- Os testes serão realizados manualmente no ambiente de desenvolvimento.
- Falhas serão registradas e comunicadas à equipe de desenvolvimento.

## 9. Critérios de Encerramento
- Todos os testes executados.
- Nenhuma falha crítica.
  
