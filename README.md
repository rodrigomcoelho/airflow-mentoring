# Airflow

Nosso primeiro exemplo utilizando Apache Airflow.

## Criando Ambiente Local de Desenvolvimento

Criar o ambiente virtual.

```bash
python3 -m venv .venv
```

> :warning: Esse comando pode variar entre python e python3 depende do que está instalado no seu sistema operacional.

Ativar o ambiente virtual

```bash
source .venv/bin/active
```

### Correções

- [X] O Hook só devolve 30 registros, precisamos paginar.
- [X] A URL está fixa. Precisamos para uma conexão.
- [X] O endpoint está fixo. Precisamos receber como argumento.
- [x] Operador apenas logando as linhas. Precisando descarregar em algum local.
- [ ] Caminho está sendo salvo com um digito para o mês e dia.
- [ ] Estamos reescrevendo do dia de hoje quando reexecutamos tasks referentes a dias no passado.
