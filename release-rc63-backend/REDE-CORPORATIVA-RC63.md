# RC63 — Rede corporativa com conversas privadas

Candidato para teste com duas contas autorizadas. Requer desktop RC63; mantém foto online, agenda, MFA e operações existentes. Não substitui o canal estável antes do teste integrado.

Perfis profissionais com adesão explícita, convites por código, aceitar/recusar/cancelar, remover/bloquear, texto privado de até 4.000 caracteres, histórico paginado, indicação de leitura, contagem de não lidas e silenciar por conversa. Contas e entidades são revalidadas em cada operação. Uma conexão não concede acesso aos pescadores, documentos ou agenda de outra entidade. Reativar o perfil ou transferir entidade gera novo código e impede acesso ao histórico do vínculo anterior.

Mensagens usam IDs de reenvio e uma fila durável dentro da conexão: autorizar/reservar uma mensagem é uma atualização atômica. Interrupções entre reserva e gravação são recuperadas na próxima consulta. O histórico tem sequência única; o mesmo ID não pode trocar o texto. Compatível com MongoDB standalone e Atlas. O aceite, remoção e bloqueio concorrem pela mesma revisão; mensagens já reservadas antes do bloqueio podem permanecer no histórico, mas o bloqueio impede consultá-lo enquanto vigente.

Coleções novas: rede_perfis_v1, rede_conexoes_v1, rede_mensagens_v1, rede_limites_v1. Cria índices de consulta e sequência, sem migrar coleções anteriores. Limites: 20 tentativas de convite e 60 mensagens novas por minuto por integrante. O contador mostrado é limitado a 999+ para conversas muito extensas.

## Instalação do candidato

Conferir `SHA256SUMS.txt` antes de executar. No EC2: `sudo bash ./instalar-rede-corporativa.sh "$PWD/sistema-pescador-backend-rede-corporativa.jar"`. O script aceita somente o backend RC60 já validado, faz backup e habilita exclusivamente `REDE_CORPORATIVA_HABILITADA=true` em um drop-in próprio do serviço. Em falha de inicialização, restaura JAR e configuração anterior. Não altera MFA ou chaves existentes.

Depois, instalar o desktop candidato RC63 em duas máquinas de teste. Ativar os dois perfis, copiar um código, enviar convite, aceitar, conversar nos dois sentidos, marcar leitura, minimizar a janela e conferir aviso. Desconectar/reconectar a internet durante um envio e usar **Verificar envio**; deve aparecer uma única mensagem. Conferir silenciamento, bloqueio, logout e perfis de entidades diferentes.

Os avisos do Windows dependem do aplicativo aberto e das configurações de notificações do computador. Não há serviço para receber mensagens com o aplicativo encerrado. Somente texto nesta versão; anexos, grupos e mural são evoluções posteriores.

## Retorno ao backend anterior

O script imprime a pasta BACKUP. Para retorno manual, parar o serviço, restaurar `sistema-pescador.jar` dessa pasta e o `rede-dropin.conf` se existir; se não existir, remover apenas `/etc/systemd/system/sistema-pescador.service.d/99-rede-corporativa.conf`. Executar `systemctl daemon-reload` e iniciar o serviço. As coleções da rede ficam preservadas para diagnóstico, sem serem usadas pelo RC60.
