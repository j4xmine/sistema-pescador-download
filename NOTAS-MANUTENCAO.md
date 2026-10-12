# Marlin 1.1.2 — versão estável

**[Baixar instalador Windows](https://github.com/j4xmine/sistema-pescador-download/releases/download/v1.1.2/SistemaPescador-Setup-1.1.2.exe)**

- Resumo de manutenção por pescador e ano, com exportação Excel e JSON.
- Totais baseados na produção histórica vinculada à guia atual; preços e percentuais por espécie.
- Perfis compartilhados por entidade, com permissões e histórico de alterações.
- Último perfil escolhido aplicado automaticamente nos próximos pescadores, preservando os totais individuais.
- Seleção rápida com busca e acesso direto ao gerenciamento de perfis.
- Recuperação da configuração individual salva quando necessário.
- Produção Pesqueira e GPS com o fluxo Rápido · perfis.

## Como usar

Abra Produção Pesqueira e GPS, selecione pescador e ano e acesse Manutenção · PesqBrasil. Em Selecionar perfil, escolha o modelo. Ele ficará lembrado por conta e entidade neste computador, inclusive após reiniciar o aplicativo. Os modelos continuam compartilhados com a equipe; a escolha de cada operador é independente.

Ao abrir outro pescador, o aplicativo consulta a versão atual do último perfil e aplica somente aos meses com origem válida. A configuração anteriormente salva não é sobrescrita automaticamente: use Usar configuração salva para recuperá-la ou Salvar configuração para guardar o novo resumo. Sem conexão ou perfil disponível, um aviso pede conferência.

## Instalação

Conclua as emissões e sincronizações e feche o programa. Execute o instalador sem desinstalar a versão anterior. O mesmo pacote serve para instalação limpa e atualização, incluindo GuiaBridge 0.5.58 e ScannerBridge 2.0.2. Dados e configurações são preservados pelo instalador.

O backend exigido é **1.1.2-rc.3-manutencao**, já instalado e validado no EC2 pelo responsável. Quem já o instalou **não precisa atualizar o servidor novamente**. Os arquivos do backend anexados são os mesmos pacotes verificados da rc.3; não foram recompilados. Consulte MANUTENCAO-SERVIDOR.md se estiver preparando outro ambiente.

## Verificação

Pacotes publicados somente após análise do código, testes automatizados de manutenção e regressão, testes do atualizador no Windows e verificação do instalador em máquina descartável (instalação limpa, atualização da rc.3 e versões anteriores, preservação de dados e reparo de componentes). SHA256SUMS.txt e unified-manifest.json identificam o conteúdo e o commit do aplicativo.

Esta versão prepara os resumos; o preenchimento e envio automático ao PesqBrasil serão desenvolvidos na próxima etapa. Nenhum envio ao PesqBrasil é realizado por esta atualização.
