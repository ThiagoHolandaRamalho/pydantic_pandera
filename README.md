# pydantic_pandera

# Visite minha documentação
![image](/pic/image.png)(https://thiagoholandaramalho.github.io/pydantic_pandera/)

# Poetry 

1.Instala as dependências do arquivo .toml: <pre><code>**poetry install --no-root**</code></pre>

# Comandos mkdocs

1.Inicia um novo projeto <pre><code> mkdoc new . </code></pre>
2.Instala o mkdocks mermaid <pre><code> poetry add 'mkdocs-mermaid2-plugin' . </code></pre>
2.Instala o mkdocks material <pre><code> poetry add 'mkdocs-material' . </code></pre>
4.Instala o mkdocks mkdocstrings <pre><code> poetry add 'mkdocstrings-python' . </code></pre>

5.Arquivo mkdocs.yml deve conter essa estrutura

<pre><code>

theme:
  name: material
  features:
    - content.code.copy

plugins:
  - search
  - mkdocstrings
  - mermaid2:
      version: 10.0.2

watch:
  - docs

</pre></code>

6.Deploy mkdocs <pre><code> mkdocs gh-deploy  </pre></code>
