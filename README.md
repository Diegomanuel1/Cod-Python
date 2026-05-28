# Cod Python
# Exercícios Básicos de Python

## 📌 Sobre o Repositório

Este repositório contém exercícios básicos desenvolvidos em Python com foco no aprendizado de lógica de programação e fundamentos da linguagem.

Os projetos foram criados durante os estudos da disciplina de programação, abordando conceitos essenciais para iniciantes.

---

# 🎯 Objetivo

O objetivo deste repositório é:

* Praticar lógica de programação;
* Aprender os fundamentos da linguagem Python;
* Desenvolver soluções simples utilizando programação;
* Melhorar a organização de projetos no GitHub;
* Criar uma base sólida para estudos mais avançados.

---

# 🛠 Tecnologias Utilizadas

* Python 3
* Visual Studio Code
* Git
* GitHub
---

# 🧠 Exercícios

## 🔹 Exercício 01 — Operações Matemáticas Básicas

Programa que solicita dois números ao usuário e realiza:

* Soma
* Subtração
* Multiplicação
* Divisão

### 📸 Screenshot

![Exercício 01]
<img width="793" height="296" alt="image" src="https://github.com/user-attachments/assets/653af61f-7e0b-4773-8b70-c1568a1522e2" />

---

## 🔹 Exercício 02 — Calculadora Comentada

Calculadora simples desenvolvida com comentários explicativos para auxiliar no aprendizado da linguagem Python.

O programa também possui tratamento para divisão por zero.

### 📸 Screenshot

![Exercício 02]
<img width="947" height="853" alt="image" src="https://github.com/user-attachments/assets/f8c3687d-657e-4a8e-9e03-0c116048fc46" />
<img width="453" height="82" alt="image" src="https://github.com/user-attachments/assets/b43f14eb-4484-41fa-b1b7-297a60be0295" />


---

## 🔹 Exercício 03 — Tabuada

Programa que solicita um número inteiro e exibe sua tabuada de 1 até 10 utilizando estrutura de repetição `for`.

### 📸 Screenshot

![Exercício 03]
<img width="704" height="293" alt="image" src="https://github.com/user-attachments/assets/caf9cb8e-40a0-4d76-9277-2403e637495e" />

---

## 🔹 Exercício 04 — Média Escolar

Programa que calcula a média de três notas e informa se o aluno foi aprovado ou reprovado.

### 📸 Screenshot

![Exercício 04]
<img width="645" height="377" alt="image" src="https://github.com/user-attachments/assets/d671863e-7d88-4cb4-b8d2-059cef2da966" />

---

## 🔹 Exercício 05 — Média Escolar Comentada

Versão comentada do programa de média escolar desenvolvida para facilitar o entendimento da lógica e da sintaxe da linguagem Python.

### 📸 Screenshot

![Exercício 05]
<img width="768" height="560" alt="image" src="https://github.com/user-attachments/assets/0df96ed3-1d8d-4ae3-b211-21cb0e14c56f" />

---

# 📌 Observações

* Exercícios desenvolvidos para fins educacionais;
* Projetos voltados para iniciantes em programação;
* Alguns códigos possuem comentários explicativos;
* O repositório será atualizado com novos exercícios futuramente.
# Exercícios Avançados de Python e Lógica Aplicada

📌 Sobre o Repositório
Este repositório contém uma coleção de exercícios práticos desenvolvidos em Python, focados na transição da lógica básica para conceitos de arquitetura de software avançada, boas práticas (Clean Code) e paradigmas de programação modernos.

🎯 Objetivo
O objetivo deste repositório é demonstrar o domínio de conceitos avançados da linguagem Python, incluindo:
* **Programação Orientada a Objetos (POO)**, encapsulamento e isolamento de propriedades;
* **Tratamento robusto de exceções** de forma defensiva (`try-except-else-finally`);
* **Tipagem estática aparente** (`Type Hinting`) para clareza em equipes de desenvolvimento;
* **Otimização algorítmica** e manipulação eficiente de dados em memória;
* **Validação de strings** avançada por meio de Expressões Regulares (Regex).

🛠 Tecnologias e Ferramentas
* **Python 3.10+** (Utilizando recursos modernos da linguagem)
* **Visual Studio Code** (Ambiente de desenvolvimento)
* **Git & GitHub** (Controle de versão e portfólio)

🧠 Documentação dos Exercícios Avançados (Upgrade de Lógica)

Abaixo estão as especificações técnicas detalhadas sobre a arquitetura e lógica aplicada nos novos scripts de 6 a 10:

---

### 🔹 Exercício 06 — Sistema de Gerenciamento de Inventário (POO)
O script de lista de compras procedural foi totalmente refatorado utilizando o paradigma de **Programação Orientada a Objetos**.
* **Conceitos Aplicados:** Encapsulamento estrito (atributos privados com prefixo `__`), impedindo a mutabilidade indevida externa dos dados do inventário.
* **Destaque Técnico:** Uso do método de segurança `.copy()` para retornar listagens, protegendo a integridade da lista original contra efeitos colaterais.

📸 **Screenshot**
![Execução do Exercício 6]
<img width="892" height="878" alt="image" src="https://github.com/user-attachments/assets/49aa3da4-7fb7-4d97-a8e8-c0cb6b805be8" />
<img width="1011" height="633" alt="image" src="https://github.com/user-attachments/assets/39153475-7ce4-4d6c-ba87-af564eae6cf0" />

---

### 🔹 Exercício 07 — Analisador Otimizado de Texto (Teoria dos Conjuntos)
Função de processamento textual com abordagem de alta performance matemática para contagem de caracteres específicos.
* **Conceitos Aplicados:** Uso de *Type Hinting* estrito para assinatura de funções e validação dinâmica de tipos em tempo de execução via `isinstance()`.
* **Destaque Técnico:** Troca de buscas lineares lentas em strings por buscas em conjuntos (`Set`), reduzindo a complexidade de tempo do algoritmo do operador `in` para $O(1)$.

📸 **Screenshot**
![Execução do Exercício 7]
<img width="890" height="802" alt="image" src="https://github.com/user-attachments/assets/a4961444-5836-43be-9ba7-46aea6ac3ad5" />

---

### 🔹 Exercício 08 — Agenda de Dados NoSQL em Memória (Regex)
Simulador de banco de dados baseado em documentos estruturados que substitui dicionários planos e simples.
* **Conceitos Aplicados:** Dicionários aninhados (*nested dicts*) com métodos de higienização de strings como `.strip().title()`.
* **Destaque Técnico:** Implementação da biblioteca nativa `re` (Regular Expressions) para validar se o e-mail inserido segue padrões de sintaxe web reais antes de gravá-lo em memória.

📸 **Screenshot**
![Execução do Exercício 8]
<img width="975" height="857" alt="image" src="https://github.com/user-attachments/assets/b933d712-6ed0-45ad-820e-ebd7ffcc3c49" />
<img width="882" height="724" alt="image" src="https://github.com/user-attachments/assets/37917ea8-244a-4818-893a-36c995ac9bb2" />

---

### 🔹 Exercício 09 — Cálculo de Fatorial Recursivo Defensivo
Resolução de problemas matemáticos clássicos através do paradigma de programação funcional e chamadas em pilha.
* **Conceitos Aplicados:** Controle exato de Casos Base para prevenção de laços infinitos e estouro de memória da máquina (*Stack Overflow*).
* **Destaque Técnico:** Tratamento defensivo de entradas que intercepta tipos errados e números negativos antes que eles cheguem à linha de execução recursiva principal.

📸 **Screenshot**
![Execução do Exercício 9]
<img width="933" height="675" alt="image" src="https://github.com/user-attachments/assets/80f00e5c-fac9-40fc-bb90-96b3171a686c" />

---

### 🔹 Exercício 10 — Motor Polimórfico de Conversão Térmica
Isolamento completo de fórmulas de engenharia climática em escopos estáticos e puros.
* **Conceitos Aplicados:** Métodos estáticos (`@staticmethod`) organizados em classes utilitárias, garantindo o princípio de responsabilidade única (SRP).
* **Destaque Técnico:** Tratamento completo de `ValueError` para prever cenários onde usuários digitam letras acidentalmente em campos numéricos de ponto flutuante (`float`).

📸 **Screenshot**
![Execução do Exercício 10]
<img width="878" height="853" alt="image" src="https://github.com/user-attachments/assets/0b91915c-f237-433c-bd83-91f5edaffc38" />
<img width="807" height="315" alt="image" src="https://github.com/user-attachments/assets/0fb87b9e-f1af-403f-942d-8c2722004d38" />


---

📌 Diretrizes de Engenharia Aplicadas
* **Padrão PEP 8:** Todos os códigos seguem as regras oficiais de estilo do ecossistema Python.
* **Código Defensivo:** Os programas foram desenhados para não quebrarem (*crash*) no terminal do usuário, mesmo quando dados inválidos ou absurdos são inseridos.
---

### 🔹 Exercício 11 — Gerenciador Avançado de Fluxos de Arquivos
Refatoração do script de manipulação de I/O em disco focado em tolerância a falhas.
* **Conceitos Aplicados:** Manipulação avançada do bloco `try-except` capturando de forma granular exceções do sistema operacional como `PermissionError` e `FileNotFoundError`.
* **Destaque Técnico:** Uso correto do gerenciador de contexto `with`, prevenindo o vazamento de recursos no sistema operacional e travamento de arquivos em memória.

📸 **Screenshot**
![Execução do Exercício 11]
<img width="859" height="469" alt="image" src="https://github.com/user-attachments/assets/3a18a96c-7cfa-4be3-9795-96aaab9ffd18" />


---

### 🔹 Exercício 12 — Motor de Criptografia de Senhas Seguras
A antiga lógica de geração pseudo-aleatória utilizando o módulo comum `random` foi descartada por motivos de conformidade de segurança.
* **Conceitos Aplicados:** Substituição completa do motor de sorteio pelo módulo `secrets`, que gera tokens adequados para criptografia de nível comercial e senhas imunes a ataques previsíveis.
* **Destaque Técnico:** List comprehension integrada e validação estrita de tipos para impedir o processamento de parâmetros inválidos de comprimento.

📸 **Screenshot**
![Execução do Exercício 12]
<img width="900" height="844" alt="image" src="https://github.com/user-attachments/assets/9d1244ad-7250-46b1-b491-2f02d2879a00" />


---

### 🔹 Exercício 13 — Engine de Telemetria e Ingestão de Logs
Script focado na implementação e rastreabilidade de eventos críticos de software de grande escala.
* **Conceitos Aplicados:** Uso de classes enumeradoras (`Enum`) para padronizar os tipos permitidos de severidade do Log (`INFO`, `WARNING`, `ERROR`), evitando strings mágicas soltas no código.
* **Destaque Técnico:** Formatação milimétrica de data utilizando máscaras em padrão ISO, incluindo frações de segundo para auditorias de alta precisão temporal.

📸 **Screenshot**
![Execução do Exercício 13]
<img width="820" height="820" alt="image" src="https://github.com/user-attachments/assets/ea0f0f79-db71-4f63-8128-3f670bb0e1f3" />

---

### 🔹 Exercício 14 — Validador Algorítmico Complexo de CPF
Refatoração da validação matemática dos dígitos verificadores aplicando padrões de Engenharia de Software.
* **Conceitos Aplicados:** Expressões Regulares (`re.findall`) aplicadas de forma otimizada para higienizar qualquer entrada poluída com hífens, espaços ou pontos de forma instantânea.
* **Destaque Técnico:** Uso de funções aninhadas em closures para centralizar a fórmula geométrica de validação de dígitos ponderados de acordo com os critérios do Ministério da Fazenda.

📸 **Screenshot**
![Execução do Exercício 14]
<img width="867" height="826" alt="image" src="https://github.com/user-attachments/assets/3554f2ec-cebc-4d68-8371-8a2f67d32717" />
---

### 🔹 Exercício 15 — Data Pipeline de Análise de Clientes (Pandas)
Migração de análises lógicas estáticas manuais para manipulação de pacotes científicos industriais de dados.
* **Conceitos Aplicados:** Integração total com a biblioteca **Pandas**, encapsulando leituras de planilhas CSV complexas diretamente em instâncias estruturadas na memória do computador.
* **Destaque Técnico:** Projeção e fatiamento de dados baseado em filtragem condicional booleana nativa de alta velocidade, além de tratamento robusto caso o arquivo físico mestre de entrada não seja localizado.

📸 **Screenshot**
![Execução do Exercício 15]
<img width="860" height="657" alt="image" src="https://github.com/user-attachments/assets/6a6a90c2-59cb-4ad8-bc35-25c889cac3be" />
---

## 🚀 Módulo Desafio Extremo (Engenharia de Software e Data Science)

Abaixo estão as análises de arquitetura dos scripts mais complexos desenvolvidos para encerramento do repositório:

### 🔹 Exercício 16 — Pipeline Analytics Avançado com Pandas
Evolução do tratamento de tabelas de clientes integrando camadas completas de tratamento estrito de tipos e manipulações agregadas.
* **Conceitos Aplicados:** Interceptação granular de `KeyError` (caso haja inconsistência estrutural nas colunas do CSV) e filtragens em memória vetorial de alta performance.
* **Destaque Técnico:** Uso do método estatístico `.idxmax()` sobre agrupamentos dinâmicos para extração instantânea do polo demográfico dominante.

📸 **Screenshot**
![Execução do Exercício 16]
<img width="860" height="887" alt="image" src="https://github.com/user-attachments/assets/1c390834-fdfc-4aab-ac39-455824cb56e6" />
<img width="907" height="271" alt="image" src="https://github.com/user-attachments/assets/01b34bd6-bb63-4868-a886-e0a7b5856aee" />

---

### 🔹 Exercício 17 — Arquitetura de Domínio Bancário Complexo (POO)
Modelagem de um ambiente bancário estruturado com múltiplos relacionamentos entre objetos dinâmicos em memória.
* **Conceitos Aplicados:** Conceito de *Aggregate Root* (Banco controlando Clientes, e Clientes agregando Contas). Proteção absoluta de mutabilidade via propriedades controladas (`@property`).
* **Destaque Técnico:** Lógica de negócios blindada com lançamentos de `PermissionError` para saques acima do saldo permitido, garantindo rastreabilidade contra fraudes em tempo de execução.

📸 **Screenshot**
![Execução do Exercício 17]
<img width="910" height="880" alt="image" src="https://github.com/user-attachments/assets/0b04c23b-88d4-40be-8651-d56e86d5a320" />
<img width="939" height="800" alt="image" src="https://github.com/user-attachments/assets/c12c0a3a-6ddb-4155-a327-88d915a7ec60" />
<img width="933" height="779" alt="image" src="https://github.com/user-attachments/assets/a129e645-9a15-4301-9971-f5c062b49548" />
<img width="878" height="809" alt="image" src="https://github.com/user-attachments/assets/2b382bfe-cacf-4fea-8111-e4bf249aca6f" />
<img width="840" height="776" alt="image" src="https://github.com/user-attachments/assets/afe791c5-6dab-438b-8679-e93cb795e32d" />
<img width="767" height="749" alt="image" src="https://github.com/user-attachments/assets/16b1acad-3935-4240-9a6d-b1fdba85784d" />

---

### 🔹 Exercício 18 — Subsistema de Renderização de Dashboards (Matplotlib)
Migração de rotinas simples de exibição gráfica para geração automatizada de relatórios visuais corporativos de alta definição.
* **Conceitos Aplicados:** Customização fina da biblioteca **Matplotlib**, alterando parâmetros de DPI, fontes acadêmicas e ordenação de gradeamento (`set_axisbelow`).
* **Destaque Técnico:** Algoritmo dinâmico de rótulos (`ax.annotate`) que calcula o posicionamento geométrico exato das informações em tempo real no topo de cada coluna.

📸 **Screenshot**
![Execução do Exercício 18]
<img width="829" height="877" alt="image" src="https://github.com/user-attachments/assets/f99012f4-e533-40d2-996d-ecc51d83f843" />
<img width="890" height="854" alt="image" src="https://github.com/user-attachments/assets/d818c7a0-42a4-4ce7-a188-d33e5227beed" />

---

### 🔹 Exercício 19 — Mecanismo de Web Scraping Defensivo (BBC News)
Script industrial focado em mineração de dados na web utilizando varredura assíncrona orientada a objetos.
* **Conceitos Aplicados:** Configuração de Headers simulando um navegador real (*User-Agent*) para passar de forma legítima por firewalls corporativos.
* **Destaque Técnico:** Implementação de `timeout` rígido no protocolo HTTP para impossibilitar o travamento e congelamento de threads de rede do sistema.

📸 **Screenshot**
![Execução do Exercício 19]
<img width="861" height="880" alt="image" src="https://github.com/user-attachments/assets/132168c9-e21a-4db8-a5e6-097acca3ebb5" />
<img width="902" height="277" alt="image" src="https://github.com/user-attachments/assets/86d55d53-c241-4a80-a990-aa8ce54fe287" />

---

### 🔹 Exercício 20 — Engine Completa do Jogo da Forca OO
Desenvolvimento de uma arquitetura modular de jogo de adivinhação, separando regras de interface (CLI), dados do jogador e estado da palavra secreta.
* **Conceitos Aplicados:** Uso de Teoria de Conjuntos (*Sets*) para histórico de palpites do competidor, eliminando penalidades injustas se o usuário digitar a mesma letra repetidas vezes.
* **Destaque Técnico:** Isolamento completo de dados sensíveis da string alvo através de propriedades estritamente privadas, protegendo o código contra manipulações externas indevidas.

📸 **Screenshot**
![Execução do Exercício 20]
<img width="886" height="883" alt="image" src="https://github.com/user-attachments/assets/23e71ede-3748-4afa-a35e-15a190c4e350" />
<img width="906" height="845" alt="image" src="https://github.com/user-attachments/assets/5dd5b62c-57b7-4730-bade-2a4534722679" />
<img width="891" height="806" alt="image" src="https://github.com/user-attachments/assets/7ca77c19-0b38-44eb-bc3b-295e8477b19d" />
<img width="475" height="119" alt="image" src="https://github.com/user-attachments/assets/9de1d253-b474-4199-b11e-130d1128e027" />

---

🏆 **Conclusão Geral das Refatorações:**
O repositório foi integralmente transformado, saindo de simples códigos puramente sequenciais feitos para estudo e passando a representar um **portfólio maduro e robusto**, apto a demonstrar habilidades práticas de arquitetura, otimização e boas práticas recomendadas pela indústria de desenvolvimento de software global.
---
# 👨‍💻 Autor

**Diego Manuel Santana Lima Barbosa**
Estudante de Ciência da Computação

---

