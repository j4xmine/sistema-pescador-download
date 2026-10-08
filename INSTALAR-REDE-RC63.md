# Rede corporativa RC63 — instalação e teste integrado

A versão estável continua sendo RC62.2. O candidato RC63 acrescenta perfis, conexões e conversas privadas, e também usa o instalador completo para computador novo. Instale inicialmente em dois computadores de teste. Não desinstale o programa atual.

## 1. Atualizar o backend no EC2

Execute no mesmo terminal SSM usado nas atualizações anteriores. O serviço terá uma breve interrupção; conclua os atendimentos e envios antes de iniciar. O instalador aceita somente o backend RC60 conhecido, faz backup e restaura a versão anterior se a inicialização falhar.

```bash
(
  set -Eeuo pipefail
  mkdir -p "$HOME/atualizacao-rede-rc63"
  cd "$HOME/atualizacao-rede-rc63"
  release_url='https://github.com/j4xmine/sistema-pescador-download/releases/download/v1.0.0-rc.63-rede.1'
  for arquivo in sistema-pescador-backend-rede-corporativa.jar instalar-rede-corporativa.sh backend-manifest.json REDE-CORPORATIVA-RC63.md SHA256SUMS-backend.txt; do
    curl --fail --location --silent --show-error --retry 3 \
      "$release_url/$arquivo" --output "$arquivo"
  done
  sha256sum --check SHA256SUMS-backend.txt
  sudo bash ./instalar-rede-corporativa.sh \
    "$PWD/sistema-pescador-backend-rede-corporativa.jar"
)
```

O resultado esperado informa `REDE_CORPORATIVA_BACKEND_INSTALADO=True`, `REDE_CORPORATIVA_HABILITADA=True`, `API_AUTENTICADA_401=True`, `PAGINA_CAPTURA_200=True` e a pasta `BACKUP`. Guarde essa pasta. Se já estiver instalado, o script informa `REDE_CORPORATIVA_JA_INSTALADA=True`.

Confira o acesso externo à foto online, que deve continuar disponível:

```bash
curl --silent --show-error --output /dev/null \
  --write-out 'FOTO_ONLINE_HTTPS=%{http_code}\n' \
  --connect-timeout 10 --max-time 30 \
  https://api.sistemapescador.com.br/foto-online/
```

Esperado: `FOTO_ONLINE_HTTPS=200`. Essa verificação confirma o acesso à página; o teste autenticado da rede será feito no aplicativo.

## 2. Instalar o desktop candidato

Baixe `SistemaPescador-Setup-1.0.0-rc.63-rede.1.exe` na página desta versão. Feche o aplicativo nos dois computadores de teste e execute o instalador. Ele preserva o caminho existente e faz backup em `C:\Sistema Pescador\Backups`. Não exige RC30/RC31. Os outros computadores podem continuar usando RC62.2 com o novo backend.

No aplicativo, abra **Rede corporativa** pelo menu, dock ou botão superior. Cada integrante precisa entrar com sua própria conta ativa de administrador da entidade ou funcionário. Não reutilize a mesma conta para testar uma conversa entre pessoas.

## 3. Conferir o fluxo entre dois integrantes

1. Nos dois computadores, ative **Meu perfil**. A participação é opcional.
2. Copie o código de conexão de um integrante. No outro, use **Adicionar conexão**, cole o código e envie o convite.
3. Aceite o convite na aba **Convites**. Abra **Conversar** e envie mensagens nos dois sentidos.
4. Confira histórico, indicação **Enviada/Lida** e contador de mensagens não lidas. Feche e reabra a conversa para conferir o histórico.
5. Minimize o aplicativo e envie outra mensagem. Deve surgir um aviso; ao clicar, ele abre a rede. O aplicativo precisa estar aberto e as notificações do Windows permitidas.
6. Use **Silenciar conversa** e confira que ela continua recebendo mensagens sem aviso sonoro. O sino geral controla os avisos deste usuário neste computador.
7. Interrompa a conexão à internet durante um envio. Ao reconectar, use **Verificar envio**, se aparecer. A mensagem deve ser confirmada uma única vez.
8. Confira bloqueio/remoção e logout: uma conversa sem autorização deixa de exibir o histórico. Desativar/reativar o perfil cria outro código e exige novas conexões.
9. Faça uma conferência breve da agenda compartilhada, foto online e abertura de um cadastro, para validar o ambiente real.

Teste também entre duas entidades, se for esse o uso esperado. Conexões não compartilham pescadores, senhas, documentos ou permissões da entidade. Esta versão oferece mensagens de texto; não inclui grupos, anexos ou mural.

## Retorno do servidor

Se for necessário voltar, use exatamente a pasta `BACKUP` informada pelo instalador, não uma pasta de outra atualização. Pare `sistema-pescador.service`, restaure o JAR e o drop-in conforme `REDE-CORPORATIVA-RC63.md`, execute `systemctl daemon-reload` e inicie o serviço. Não exclua as coleções da rede.

Antes de promover o candidato para os demais computadores, registre o resultado desse teste e eventuais mensagens de erro. Não envie senhas, tokens ou documentos no diagnóstico.
