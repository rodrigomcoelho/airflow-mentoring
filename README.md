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
- [ ] O Hook só devolve 30 registros, precisamos paginar.
- [ ] A URL está fixa. Precisamos para uma conexão.
- [ ] O endpoint está fixo. Precisamos receber como argumento.
