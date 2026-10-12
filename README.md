# Sistema Pescador — Downloads

## Versão estável: v1.1.2 — Marlin

[Baixar instalador completo para Windows](https://github.com/j4xmine/sistema-pescador-download/releases/download/v1.1.2/SistemaPescador-Setup-1.1.2.exe)

O mesmo pacote serve para **computadores novos e atualizações**. Não é necessário instalar versões intermediárias. Inclui GuiaBridge 0.5.58, ScannerBridge 2.0.2 e runtime Microsoft. Setup e Atualizacao têm conteúdo idêntico.

Conclua sincronizações e emissões, salve o trabalho, feche o programa e execute o instalador **sem desinstalar a versão atual**. Também é possível usar **Verificar atualizações** no aplicativo ou baixar pela [área de usuários](https://sistemapescador.com.br/area).

## Novidades da 1.1.2

- Resumo de manutenção por pescador e ano, com Excel e JSON.
- Totais da produção histórica vinculada à guia atual; preços e percentuais por espécie.
- Perfis compartilhados por entidade, com permissões e histórico de alterações.
- Último perfil escolhido aplicado automaticamente nos próximos pescadores, sempre com os totais individuais.
- Seletor rápido com busca e opção de recuperar a configuração individual salva.

A escolha do último perfil é lembrada por conta e entidade neste computador. Os modelos são compartilhados com a equipe; cada operador mantém sua escolha independente. A aplicação automática não sobrescreve configurações salvas: use **Salvar configuração** para guardar o novo resumo. Não há envio automático ao PesqBrasil nesta versão.

Permanecem disponíveis os cadastros com máscaras, dock reorganizável, avisos de atualização, agenda, financeiro, documentos, Central GPS e rede corporativa. O painel de advocacia e a consulta assistida ao CNA são preservados; as áreas jurídicas sinalizadas **Em desenvolvimento** continuam propostas sem operações ativas.

## Compatibilidade e verificação

Requer backend **1.1.2-rc.3-manutencao**, já instalado e confirmado no EC2. Quem já aplicou esse pacote não precisa atualizar o servidor novamente. Mantém o esquema local 12 e não exige migração destrutiva do banco.

Instalador verificado em máquina descartável: instalação limpa, atualização da rc.3 e bases anteriores compatíveis, preservação de dados e reparo de componentes. Os pacotes publicados são os mesmos verificados pelos testes, sem recompilação durante a publicação.

[Notas, manifestos e hashes](https://github.com/j4xmine/sistema-pescador-download/releases/tag/v1.1.2)

SHA-256 do instalador: `05c3a9d1892cea70d22793936c13dc57751d2973203cb9639d676386d0b50464`.

[Marlin 1.1.1 — versão anterior](https://github.com/j4xmine/sistema-pescador-download/releases/tag/v1.1.1)

[Histórico de versões](https://github.com/j4xmine/sistema-pescador-download/releases)
