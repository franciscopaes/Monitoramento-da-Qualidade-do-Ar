# 🌎 Monitoramento da Qualidade do Ar com Python

> 🚀 Projeto em Python que utiliza Selenium para capturar automaticamente o índice de qualidade do ar (AQI) do site Weather.com e interpretar seu nível de poluição.

---

## 📖 Descrição do Projeto

Este projeto tem como objetivo **monitorar automaticamente a qualidade do ar (AQI - Air Quality Index)** de uma determinada região utilizando **Python e Selenium**.  
O código acessa o site [Weather.com](https://weather.com/), captura o valor atual do índice de qualidade do ar e interpreta o resultado com base na escala oficial de classificação ambiental.

Dessa forma, é possível automatizar a coleta de dados ambientais e disponibilizar informações atualizadas sobre a qualidade do ar.

---

## ⚙️ Tecnologias Utilizadas

- 🐍 **Python**
- 🌐 **Selenium WebDriver**
- 💻 **Google Chrome**
- ⏱️ **Biblioteca time**

---

## 🚀 Como Funciona

1. O script inicia o **navegador Chrome** em modo invisível (headless).  
2. Acessa automaticamente o link da previsão de qualidade do ar do **Weather.com**.  
3. Captura o valor atual do índice AQI exibido na página.  
4. Interpreta o número e classifica a qualidade do ar como:
   - **0–50:** Boa  
   - **51–100:** Moderada  
   - **101–150:** Ruim para grupos sensíveis  
   - **151–200:** Ruim  
   - **201–300:** Muito ruim  
   - **301–500:** Perigosa  
5. Exibe o resultado no terminal e encerra o navegador.

---

## 💡 Relevância Social do Projeto

A **qualidade do ar** é um dos principais fatores que influenciam a **saúde e o bem-estar das pessoas**, especialmente em áreas urbanas.  
A exposição prolongada a poluentes atmosféricos pode causar **problemas respiratórios, cardiovasculares** e agravar doenças crônicas, afetando principalmente **crianças, idosos e pessoas com condições pré-existentes**.

Este projeto é relevante para a sociedade pois:

- 🌱 **Promove a conscientização ambiental**, mostrando a importância de acompanhar os níveis de poluição do ar.  
- 💨 **Incentiva o uso da tecnologia** para automatizar a coleta de dados ambientais.  
- 📊 Pode ser **integrado a sistemas de monitoramento**, dashboards ou alertas que ajudem comunidades a se protegerem em dias de má qualidade do ar.  
- 🧠 Serve como **base educacional** para estudantes e desenvolvedores interessados em sustentabilidade e automação com Python.
