# Sistema Pescador — Downloads

## Versão estável: v1.0.0 — Barracuda

[Baixar instalador completo para Windows](https://github.com/j4xmine/sistema-pescador-download/releases/download/v1.0.0/SistemaPescador-Setup-1.0.0.exe)

O mesmo pacote serve para **computadores novos e atualizações**. Não é necessário instalar uma versão intermediária. Inclui GuiaBridge 0.5.58, ScannerBridge 2.0.2 e o runtime Microsoft necessário.

Para atualizar, salve seu trabalho, espere as operações terminarem, feche o sistema e execute o instalador **sem desinstalar a versão atual**. O aplicativo também oferece **Verificar atualizações**. Os arquivos Setup e Atualizacao são idênticos; o segundo nome mantém a compatibilidade com os atualizadores existentes.

A Barracuda reúne cadastro, documentos, financeiro, atendimento, produção e GPS, agenda compartilhada, múltiplas abas, perfis e rede corporativa. Traz chat renovado, fotos de perfil e @username; agenda e conversa alternam sem sobreposição. A revisão também corrigiu a saída durante sincronização, notificações ao trocar de sessão, retorno ao login dentro de abas e proteção de dados exportados em CSV.

Requer o backend RC63.2 já instalado no EC2. Esta atualização desktop não exige nova instalação do backend nem altera suas configurações de duas etapas. Mantém o esquema local 12.

Validação: 707 testes Flutter na suíte completa, 310 testes do backend existente, análise Dart sem erros, regressões Windows, compilação Windows e instalação em máquina descartável. Foram conferidas instalação nova, atualização desde as bases RC30/RC31/RC57/RC61/RC62/RC63, reinstalação, reparo de componentes, preservação de arquivos sintéticos e interrupção quando o backup não pode ser realizado. O pacote publicado é o mesmo testado, sem recompilação.

Os testes usam dados sintéticos e não substituem a conferência de emissões reais no eSocial/GOV.BR nem de scanner físico. Consulte o relatório da revisão para conhecer a cobertura e seus limites.

[Notas, relatório da revisão, manifesto e hashes](https://github.com/j4xmine/sistema-pescador-download/releases/tag/v1.0.0)

SHA-256 do instalador: `375215a97cd73c2ac41b8ed9ef57d7ced4164aeb7cebfcfbbf7e9001acf37fa4`.

[Histórico de versões](https://github.com/j4xmine/sistema-pescador-download/releases)
