# Sistema Pescador RC62 — Interface compacta

Busca por nome/CPF e cidade sempre visíveis. Filtros de pagamentos, categoria, ordenação, meses e progresso GPS reunidos no botão Filtros. O painel começa recolhido, informa a quantidade de filtros adicionais ativos e tem rolagem própria. Limpar apenas os filtros adicionais preserva nome/CPF e cidade.

Fechar todas as abas disponível ao lado do botão +. Pede uma única confirmação de descarte de alterações não salvas e mantém o Dashboard. Operações protegidas bloqueiam o fechamento, inclusive se começarem enquanto a confirmação estiver aberta.

Consolida o dock inferior, a agenda compartilhada e a foto 3x4 online. GuiaBridge permanece 0.5.58 e o banco local permanece no esquema 12. Não inclui a nova rede corporativa, prevista para a próxima etapa.

## Atualização

Aguarde as operações terminarem, salve seu trabalho, feche o sistema e execute o instalador sem desinstalar a versão atual. Depois, abra Pescadores para conferir a nova organização. O dock continua em Configurações → Menu → Local do menu.

Não exige atualização adicional do backend RC60 já confirmado no servidor. Agenda compartilhada e foto online dependem desse backend. Dados locais, documentos e configurações são preservados.

Validação: análise Dart, suíte Flutter completa, testes específicos de filtros e fechamento de abas, prévia visual com dados sintéticos, compilação Windows e instalação/reinstalação sobre RC60 e RC61 em runner descartável. A inspeção no notebook do usuário permanece pendente. Publicação estável solicitada pelo usuário; o pacote público será o mesmo arquivo validado, conferido por SHA-256, sem recompilação.
