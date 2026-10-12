# Marlin 1.1.2-rc.3 — perfis da entidade

Pré-release para conferência. O catálogo estável continua na Marlin 1.1.1.

- Perfis de manutenção compartilhados por entidade, com espécies, preços/kg, meses e percentuais.
- Administradores gerenciam; funcionários consultam e aplicam. Importação dos perfis locais com confirmação, preservando os originais.
- Autoria, data e últimas 200 alterações; proteção contra edições simultâneas.
- Cópia offline somente para consulta. Totais continuam próprios de cada pescador, a partir da produção vinculada à guia atual do histórico.
- Resumo mensal e anual, exportação Excel XLSX e JSON. Alterar um perfil não modifica configurações já aplicadas nem envia dados ao PesqBrasil.

## 1. Atualizar o servidor EC2

Conclua emissões e sincronizações e execute no terminal do EC2 usado nas atualizações anteriores:

```bash
bash <<'MANUTENCAO'
set -euo pipefail
pasta_manutencao=$(mktemp -d "$HOME/pescador-manutencao-XXXXXXXX")
cd "$pasta_manutencao"
base_manutencao='https://github.com/j4xmine/sistema-pescador-download/releases/download/v1.1.2-rc.3'
for arquivo in SHA256SUMS-backend.txt MANUTENCAO-SERVIDOR.md backend-manifest.json instalar-manutencao.py sistema-pescador-backend-manutencao.jar; do
  curl --fail --location --retry 3 "$base_manutencao/$arquivo" --output "$arquivo"
done
echo 'fd5f027b31f548347955a73f7a3a6067fa09e1c8d8a322df64087f82d0121fa1  SHA256SUMS-backend.txt' | sha256sum --check -
sha256sum --check SHA256SUMS-backend.txt
sudo python3 ./instalar-manutencao.py "$PWD/sistema-pescador-backend-manutencao.jar"
MANUTENCAO
```

Espere **MANUTENCAO_BACKEND_INSTALADO=True**. O script confere a versão atual, faz backup do JAR e serviço e tenta retornar ao anterior se a API não iniciar. Aceita o backend Advocacia 1.1.0-rc.1 já utilizado pela Marlin. Não force a instalação se houver divergência. Não altera configurações de duas etapas nem migra cadastros/guia. A publicação desta release não instala automaticamente o EC2.

## 2. Instalar o aplicativo

[Baixar instalador Windows](https://github.com/j4xmine/sistema-pescador-download/releases/download/v1.1.2-rc.3/SistemaPescador-Setup-1.1.2-rc.3.exe)

Feche o programa e execute o instalador sem desinstalar a versão anterior. O arquivo Atualizacao é idêntico ao Setup; baixe apenas um. Confira SHA256SUMS.txt. Inclui GuiaBridge 0.5.58 e ScannerBridge 2.0.2; mantém esquema local 12.

Abra **Produção Pesqueira e GPS → pescador e ano → Manutenção · PesqBrasil → Perfis**. Como administrador, crie ou importe um modelo; entre em outro computador/conta da mesma entidade e confira a lista. Depois aplique a um pescador, revise e salve sua configuração.

## Validação

Backend: 340 testes Java/Mongo/HTTP e 4 do instalador. Desktop: 786 testes na suíte completa (27 específicos da manutenção), análise de código e validação de cálculo/exportação, sincronização, permissões, cache, importação, interface e instalação/atualização Windows com dados sintéticos. Os assets publicados são os mesmos binários verificados, sem recompilação. A validação operacional no EC2 e no computador do usuário ainda precisa ser confirmada antes de promover a versão estável.
