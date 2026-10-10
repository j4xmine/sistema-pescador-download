# Sistema Pescador — Downloads

## Versão estável: v1.1.1 — Marlin

[Baixar instalador completo para Windows](https://github.com/j4xmine/sistema-pescador-download/releases/download/v1.1.1/SistemaPescador-Setup-1.1.1.exe)

O mesmo pacote serve para **computadores novos e atualizações**. Não é necessário
instalar versões intermediárias. Inclui GuiaBridge 0.5.58, ScannerBridge 2.0.2 e
runtime Microsoft. Setup e Atualizacao têm conteúdo idêntico.

Salve o trabalho, conclua sincronizações e emissões, feche o programa e execute o
instalador **sem desinstalar a versão atual**. Você também pode usar **Verificar
atualizações** no aplicativo. Atualiza Marlin 1.1.0/1.1.1-rc.1, Barracuda, Advocacia rc.1/rc.2 e as bases
anteriores compatíveis listadas no catálogo.

A 1.1.1 melhora o visual dos cadastros e as máscaras de CPF, CNPJ, CEP e telefone;
permite reorganizar o dock por conta e entidade; e avisa sobre novas atualizações
com opção de adiar. O aviso não instala nem fecha o aplicativo automaticamente.

Marlin traz um painel renovado para **escritórios de advocacia e advogados
autônomos**, cadastro profissional, equipe, inscrições OAB e consulta pública
assistida ao CNA. O aplicativo abre o portal no Edge/Chrome, o operador pesquisa
e seleciona a ficha e confirma a importação. A foto da OAB é opcional.

As áreas **Atendimento online com cliente**, **Casos e processos**, **Prazos e
audiências**, **Documentos e assinaturas** e **Honorários e contratos** aparecem
somente na advocacia e estão marcadas **Em desenvolvimento**. São propostas,
sem envio de mensagens ou documentos, criação de casos ou acesso do cliente
nesta versão. As funções existentes das colônias, agenda, financeiro, documentos,
GPS e rede corporativa continuam disponíveis.

Requer o backend **1.1.0-rc.1-advocacia**, já instalado e confirmado no EC2.
Não exige nova migração de banco. Mantém esquema local 12.

Validação: 760 testes na suíte completa, testes Windows, navegador real
com respostas CNA sintéticas, compilação e testes de instalação nova, atualização,
reparo e preservação de arquivos de teste. O pacote publicado é o mesmo validado,
sem recompilação. O uso real do CNA/reCAPTCHA depende do portal e da máquina do
operador; a conferência de eSocial/GOV.BR e scanner físico não é substituída por
estes testes.

[Notas, revisão, manifesto e hashes](https://github.com/j4xmine/sistema-pescador-download/releases/tag/v1.1.1)

SHA-256 do instalador: `fd25cc90a781216ddfaf8ab379cb225ed1291714d636eed9de9d562f6576cbc2`.

[Marlin 1.1.0 — versão anterior](https://github.com/j4xmine/sistema-pescador-download/releases/tag/v1.1.0)

[Barracuda — histórico](https://github.com/j4xmine/sistema-pescador-download/releases/tag/v1.0.0)

[Histórico de versões](https://github.com/j4xmine/sistema-pescador-download/releases)
