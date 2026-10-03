# Sistema Pescador RC56 — validado

Versão 1.0.0-rc.56-acessos.1, com GuiaBridge 0.5.53 no mesmo instalador.

A versão foi validada pelo responsável em 02/10/2026, após instalar o backend RC56, e autorizada para atualização dos outros computadores. O executável publicado é exatamente o mesmo candidato testado, sem recompilação.

## Novidades
- Alternância entre Entidade Admin e Plataforma Admin na mesma conta, mediante autorização adicional concedida por outro administrador da plataforma.
- Foto própria de perfil: escolher, substituir e remover JPG/PNG de até 2 MB.
- Inclui as melhorias anteriores de painel, boas-vindas, indicação de situação financeira, filtro de pagamentos e administração da plataforma.

## Atualização
1. No aplicativo, clique em Verificar atualizações e abra o download; ou baixe o instalador desta página.
2. Conclua as operações em andamento e feche o Sistema Pescador.
3. Execute o instalador sobre a versão atual, sem desinstalar.
4. Abra o aplicativo e confira a versão RC56.

O instalador inclui o GuiaBridge 0.5.53 e preserva os dados locais. É destinado aos computadores que já têm o sistema instalado. O backend RC56 já foi instalado no servidor em uso; não é necessário repetir a atualização da EC2 em cada computador.

O acesso adicional à plataforma precisa ser concedido pelo superusuário atual. A instalação não concede privilégios nem ativa a autenticação em duas etapas automaticamente.

## Validação e integridade
- Backend: 271 testes aprovados, incluindo autorização, revogação e fotos.
- Aplicativo: análise, testes RC56 e regressões aprovados.
- Compilação Windows e instalação sintética, incluindo RC55 e preservação de dados, aprovadas.
- A validação realizada não representa teste operacional já executado nos outros computadores.
- Código do aplicativo: 0f867bb3e7d8589c05f0b9a5c567a6509f9a7de4.
- Build: 37048531141.
- SHA-256 do instalador: 3f3f98de177e7f7f60c57638e14657e08619d8a4d91294012117a12dde7676cd.

Os manifestos originais acompanham o pacote. SHA256SUMS.txt confere os arquivos desta publicação.
